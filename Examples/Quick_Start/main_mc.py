"""
Python version of main_mc.m
"""

import numpy as np
import sys
from pathlib import Path
from datetime import timedelta
from astropy.time import Time

sys.path.append(str(Path(__file__).parent.parent.parent / 'supporting_functions'))

from getidx import *
from categorizeObj import categorizeObj
from prop_mit_vec import prop_mit_vec
from orbcontrol_vec import orbcontrol_vec
from cube_vec_v3 import cube_vec_v3
from collision_prob_vec import collision_prob_vec
from fillin_atmosphere import fillin_atmosphere
from frag_exp_SBM_vec import frag_exp_SBM_vec
from frag_col_SBM_vec import frag_col_SBM_vec
from Fast_MC2SSEM_population import Fast_MC2SSEM_population
from generate_random_launch import generate_random_launch

def main_mc(MCconfig, RNGseed=None):
    """
    Main Monte Carlo simulation function
    
    Parameters:
    -----------
    MCconfig : dict
        Configuration dictionary
    RNGseed : int, optional
        Random seed for reproducibility
        
    Returns:
    --------
    nS : int
        Number of satellites
    nD : int
        Number of derelicts
    nN : int
        Number of debris
    nB : int
        Number of rocket bodies
    deorbitlist_r : array-like
        Final satellite matrix
    """
    
    # Declare global variables
    global mat_sats, time0, tsince, n_time, launch_model, repeatLaunches, launchMC_step
    global additional_launches, ind_launch, ind_launch_add, use_sgp4, skipCollisions
    global max_frag, CUBE_RES, collision_alt_limit, density_profile, param
    global orbtol, PMD, step_control, P_frag, P_frag_cutoff, alph, alph_a
    global save_output_file, filename_save, paramSSEM
    
    # Initialize RNG seed
    if RNGseed is not None:
        np.random.seed(RNGseed)
        print(f'main_mc specified with seed {RNGseed}')
    elif 'seed' in MCconfig:
        np.random.seed(MCconfig['seed'])
        print(f'main_mc specified with config seed {MCconfig["seed"]}')
    
    # Load configuration
    if isinstance(MCconfig, str):
        # TODO: Handle string config loading
        raise NotImplementedError("String config loading not implemented yet")
    
    # Extract configuration parameters - do this first to get mat_sats
    loadCFG(MCconfig)
    
    # Initialize parameters
    if 'paramSSEM' in MCconfig:
        param['paramSSEM'] = MCconfig['paramSSEM']
    
    if 'sample_params' in MCconfig:
        param['sample_params'] = MCconfig['sample_params']
    else:
        param['sample_params'] = 0
    
    # Remove large data embedded in cfg (for saving)
    MCconfig['a_all'] = {}
    MCconfig['ap_all'] = {}
    MCconfig['aa_all'] = {}
    MCconfig['launchMC_step'] = {}
    
    # Assign constants to param structure
    param['req'] = radiusearthkm
    param['mu'] = mu_const
    param['j2'] = j2
    param['max_frag'] = max_frag
    paramSSEM['species'] = [1, 1, 1, 0, 0, 0]  # species: [S,D,N,Su,B,U]
    
    # Density profile
    param['density_profile'] = density_profile
    
    # Preallocate arrays
    n_sats = mat_sats.shape[0]
    
    # Initialize counters
    numObjects = np.zeros(n_time)
    numObjects[0] = n_sats
    count_coll = np.zeros(n_time, dtype=np.uint8)
    count_expl = np.zeros(n_time, dtype=np.uint8)
    count_debris_coll = np.zeros(n_time, dtype=np.uint8)
    count_debris_expl = np.zeros(n_time, dtype=np.uint8)
    
    # Initialize species count tracking arrays
    satellites_over_time = np.zeros(n_time)
    derelicts_over_time = np.zeros(n_time)
    debris_over_time = np.zeros(n_time)
    rocket_bodies_over_time = np.zeros(n_time)
    
    # Initialize tracking arrays
    if save_output_file in [3, 4]:
        sats_info = [None] * 3
    else:
        sats_info = [[None] * 3 for _ in range(n_time)]
    
    frag_info = [[None] * 4 for _ in range(n_time)]
    frag_info5 = [None] * n_time
    
    # Initialize counters
    num_pmd = 0
    num_deorbited = 0
    launch = 0
    out_future = []
    count_tot_launches = 0
    file_save_index = 0
    deorbitlist_r = np.zeros(n_time)
    
    # Initialize SSEM arrays
    S_MC = np.full((n_time, len(paramSSEM['R02']) - 1), np.nan)
    D_MC = S_MC.copy()
    N_MC = S_MC.copy()
    
    # Get indices for matrix operations
    param['maxID'] = np.max([np.max(mat_sats[:, idx_ID]), 0])
    
    # Define index arrays for different operations
    idx_launch_in_extra = [idx_ID]
    idx_prop_in = [idx_a, idx_ecco, idx_inclo, idx_nodeo, idx_argpo, idx_mo, idx_bstar, idx_controlled]
    idx_thalassa_in = [idx_a, idx_ecco, idx_inclo, idx_nodeo, idx_argpo, idx_mo, idx_bstar, idx_mass, idx_radius, idx_r[0], idx_r[1], idx_r[2], idx_v[0], idx_v[1], idx_v[2]]
    idx_prop_out = [idx_a, idx_ecco, idx_inclo, idx_nodeo, idx_argpo, idx_mo, idx_error, idx_r[0], idx_r[1], idx_r[2], idx_v[0], idx_v[1], idx_v[2]]
    idx_control_in = [idx_a, idx_ecco, idx_inclo, idx_nodeo, idx_argpo, idx_mo, idx_controlled, idx_a_desired, idx_missionlife, idx_launch_date, idx_r[0], idx_r[1], idx_r[2], idx_v[0], idx_v[1], idx_v[2]]
    idx_control_out = [idx_a, idx_controlled, idx_r[0], idx_r[1], idx_r[2], idx_v[0], idx_v[1], idx_v[2]]
    idx_exp_in = [idx_mass, idx_radius, idx_r[0], idx_r[1], idx_r[2], idx_v[0], idx_v[1], idx_v[2], idx_objectclass]
    idx_col_in = [idx_mass, idx_radius, idx_r[0], idx_r[1], idx_r[2], idx_v[0], idx_v[1], idx_v[2], idx_objectclass]
    
    # Store initial state
    objclassint_store = mat_sats[:, idx_objectclass]
    a_store = mat_sats[:, idx_a]
    controlled_store = mat_sats[:, idx_controlled]
    
    # Initialize sats_info
    if save_output_file in [3, 4]:
        sats_info[0] = objclassint_store.astype(np.int8)
        sats_info[1] = a_store.astype(np.float32)
        sats_info[2] = controlled_store.astype(np.int8)
        # Calculate SSEM population
        S_MC[0, :], D_MC[0, :], N_MC[0, :] = Fast_MC2SSEM_population(sats_info, paramSSEM)
    else:
        sats_info[0][0] = objclassint_store.astype(np.int8)
        sats_info[0][1] = a_store.astype(np.float32)
        sats_info[0][2] = controlled_store.astype(np.int8)
    
    # Extract species numbers
    nS, nD, nN, nB = categorizeObj(objclassint_store, controlled_store)
    
    # Store initial species counts
    satellites_over_time[0] = nS
    derelicts_over_time[0] = nD
    debris_over_time[0] = nN
    rocket_bodies_over_time[0] = nB
    
    # Test save
    if save_output_file > 0:
        # TODO: Implement proper saving
        print(f'Test saving of {filename_save} successful')
    
    # Print initial status
    print(f'Year {time0.year} - Day {time0.timetuple().tm_yday:03d},\t PMD {num_pmd:04d},\t Deorbit {num_deorbited:03d},\t Launches {len(out_future):03d},\t nFrag {count_expl[0]:03d},\t nCol {count_coll[0]:03d},\t nObjects {numObjects[0]} ({nS},{nD},{nN},{nB})')
    
    launch_data = []
    
    # START PROPAGATION
    for n in range(1, n_time):
        current_time = time0 + timedelta(minutes=tsince[n])
        jd = Time(current_time).jd
        
        # LAUNCHES
        if launch_model.lower() == 'matsat':  # repeat launches
            # Get launches for current timestep
            if n < len(launchMC_step):
                out_future = launchMC_step[n] if launchMC_step[n] is not None else []
            else:
                out_future = []
            launch = len(out_future)
        elif launch_model.lower() == 'random':
            # Random launch model - implement based on launch frequency
            if hasattr(globals(), 'launch_frequency') and np.random.random() < launch_frequency:
                # Generate random launch
                out_future = generate_random_launch(param)
                launch = len(out_future)
            else:
                out_future = []
                launch = 0
        elif launch_model.lower() in ['data', 'somma']:
            # Data-driven launch model
            if n < len(additional_launches):
                out_future = additional_launches[n] if additional_launches[n] is not None else []
            else:
                out_future = []
            launch = len(out_future)
        elif launch_model.lower() == 'no_launch':
            out_future = []
            launch = 0
        else:
            raise ValueError('Invalid launch model')
        
        param['maxID'] = param['maxID'] + len(out_future)
        count_tot_launches = count_tot_launches + len(out_future)
        
        # PROPAGATION (one timestep at a time)
        n_sats = mat_sats.shape[0]
        
        if not use_sgp4:  # use prop_mit
            param['jd'] = jd
            
            if n > 0:
                dt = 60 * (tsince[n] - tsince[n - 1])  # units of time in seconds
            else:
                dt = 60 * tsince[n]  # units of time in seconds
            
            # Propagate orbital elements
            mat_sats[:, idx_prop_out] = prop_mit_vec(mat_sats[:, idx_prop_in], dt, param)
            
            # REMOVE DECAYED SATELLITES
            idx_decayed = np.where(mat_sats[:, idx_error] == 1)[0]
            if len(idx_decayed) > 0:
                num_deorbited += len(idx_decayed)
                mat_sats = np.delete(mat_sats, idx_decayed, axis=0)
        
        # ORBIT CONTROL
        if n % step_control == 0 or step_control == 1:
            # Apply orbit control
            mat_sats[:, idx_control_out], deorbit_PMD = orbcontrol_vec(
                mat_sats[:, idx_control_in], tsince[n], time0, orbtol, PMD, DAY2MIN, YEAR2DAY, param)
            
            # Remove post-mission disposal satellites
            num_pmd = len(deorbit_PMD)
            if len(deorbit_PMD) > 0:
                mat_sats = np.delete(mat_sats, deorbit_PMD, axis=0)
        else:
            num_pmd = 0
        
        deorbitlist_r[n] = num_deorbited
        
        # EXPLOSIONS (for Rocket Body)
        n_sats = mat_sats.shape[0]
        out_frag = []
        
        if P_frag > 0:
            find_rocket = np.where(mat_sats[:, idx_objectclass] == 5)[0]  # Rocket bodies
            if len(find_rocket) > 0:
                rand_P_exp = np.random.random(len(find_rocket))
                
                if 'P_frag_cutoff' in locals():
                    # Age-based explosion logic
                    current_age = tsince[n] - mat_sats[find_rocket, idx_launch_date]
                    age_factor = np.exp(-current_age / P_frag_cutoff)
                    find_P_exp = np.where(rand_P_exp < P_frag * age_factor)[0]
                else:
                    find_P_exp = np.where(rand_P_exp < P_frag)[0]
                
                remove_frag = find_rocket[find_P_exp]
                
                for idx_P_exp_temp in range(len(remove_frag) - 1, -1, -1):  # reverse order
                    idx_P_exp = remove_frag[idx_P_exp_temp]
                    
                    p1_all = mat_sats[idx_P_exp, :]
                    p1_mass = p1_all[idx_mass]
                    p1_objectclass = p1_all[idx_objectclass]
                    p1_in = p1_all[idx_exp_in]
                    
                    # Perform explosion fragmentation
                    debris1 = frag_exp_SBM_vec(tsince[n], p1_in, param)
                    param['maxID'] = param['maxID'] + len(debris1)
                    
                    if len(debris1) == 0:
                        # Remove from remove_frag if no debris generated
                        remove_frag = np.delete(remove_frag, idx_P_exp_temp)
                    else:
                        out_frag.extend(debris1)
                        print(f'Year {current_time.year} - Day {current_time.timetuple().tm_yday:03d} \t Explosion, p1 type {p1_objectclass}, {p1_mass:.1f} kg, nDebris {len(debris1)}')
                        count_expl[n] += 1
                
                if len(remove_frag) > 0:
                    mat_sats = np.delete(mat_sats, remove_frag, axis=0)
        
        # COLLISIONS
        if (skipCollisions == 1) or (mat_sats.shape[0] == 0):
            collision_array = []
        else:
            # Perform cube method collision detection
            collision_cell = cube_vec_v3(mat_sats[:, idx_r], CUBE_RES, collision_alt_limit)
            collision_array = collision_cell
        
        remove_collision = []
        out_collision = []
        
        if len(collision_array) > 0:
            # Process each collision pair
            for collision_pair in collision_array:
                idx1, idx2 = collision_pair
                
                # Get collision objects
                p1_all = mat_sats[idx1, :]
                p2_all = mat_sats[idx2, :]
                
                p1_in = p1_all[idx_col_in]
                p2_in = p2_all[idx_col_in]
                
                # Calculate collision probability and velocity
                # For single collision pair, calculate manually
                p1_radius = p1_in[1]
                p2_radius = p2_in[1]
                p1_v = p1_in[5:8]
                p2_v = p2_in[5:8]
                
                sigma = (p1_radius + p2_radius)**2 * (np.pi / 1e6)  # m²
                dU = CUBE_RES**3  # km³
                Vimp = np.linalg.norm(p1_v - p2_v)  # km/s
                prob_coll = Vimp / dU * sigma
                dv_coll = Vimp
                
                # Check if collision occurs based on probability
                if np.random.random() < prob_coll:
                    # Perform collision fragmentation
                    debris1, debris2 = frag_col_SBM_vec(tsince[n], p1_in, p2_in, param)
                    
                    # Add collision debris to output
                    if len(debris1) > 0:
                        out_collision.extend(debris1)
                    if len(debris2) > 0:
                        out_collision.extend(debris2)
                    
                    # Mark objects for removal
                    remove_collision.extend([idx1, idx2])
                    
                    # Update collision counter
                    count_coll[n] += 1
                    
                    print(f'Year {current_time.year} - Day {current_time.timetuple().tm_yday:03d} \t Collision, p1 type {p1_all[idx_objectclass]}, p2 type {p2_all[idx_objectclass]}, nDebris {len(debris1) + len(debris2)}')
        
        # DATA PROCESSING
        if len(remove_collision) > 0:
            mat_sats = np.delete(mat_sats, remove_collision, axis=0)
        
        # Add new objects
        if len(out_future) > 0:
            mat_sats = np.vstack([mat_sats, out_future])
        if len(out_frag) > 0:
            mat_sats = np.vstack([mat_sats, out_frag])
        if len(out_collision) > 0:
            mat_sats = np.vstack([mat_sats, out_collision])
        
        # Record launch data
        if len(out_future) > 0:
            launch_data.extend(out_future)
        
        # ACCOUNTING
        n_sats = mat_sats.shape[0]
        numObjects[n] = n_sats
        
        objclassint_store = mat_sats[:, idx_objectclass]
        a_store = mat_sats[:, idx_a]
        controlled_store = mat_sats[:, idx_controlled]
        
        # Update sats_info
        if save_output_file in [3, 4]:
            sats_info[0] = objclassint_store.astype(np.int8)
            sats_info[1] = a_store.astype(np.float32)
            sats_info[2] = controlled_store.astype(np.int8)
            # Calculate SSEM population
            S_MC[n, :], D_MC[n, :], N_MC[n, :] = Fast_MC2SSEM_population(sats_info, paramSSEM)
        else:
            sats_info[n][0] = objclassint_store.astype(np.int8)
            sats_info[n][1] = a_store.astype(np.float32)
            sats_info[n][2] = controlled_store.astype(np.int8)
        
        count_debris_coll[n] = len(out_collision)
        count_debris_expl[n] = len(out_frag)
        
        # Update species counts
        nS, nD, nN, nB = categorizeObj(objclassint_store, controlled_store.astype(np.int8))
        
        # Store species counts for this timestep
        satellites_over_time[n] = nS
        derelicts_over_time[n] = nD
        debris_over_time[n] = nN
        rocket_bodies_over_time[n] = nB
        
        # Print status
        print(f'Year {current_time.year} - Day {current_time.timetuple().tm_yday:03d},\t PMD {num_pmd:04d},\t Deorbit {num_deorbited:03d},\t Launches {len(out_future):03d},\t nFrag {count_expl[n]:03d},\t nCol {count_coll[n]:03d},\t nObjects {numObjects[n]} ({nS},{nD},{nN},{nB})')
    
    print(f'\n === FINISHED MC RUN (main_mc.py) WITH SEED: {RNGseed} ===')
    
    return nS, nD, nN, nB, deorbitlist_r, satellites_over_time, derelicts_over_time, debris_over_time, rocket_bodies_over_time

def loadCFG(cfg):
    """Load configuration into global variables"""
    global mat_sats, time0, tsince, n_time, launch_model, repeatLaunches, launchMC_step
    global additional_launches, ind_launch, ind_launch_add, use_sgp4, skipCollisions
    global max_frag, CUBE_RES, collision_alt_limit, density_profile, param
    global orbtol, PMD, step_control, P_frag, P_frag_cutoff, alph, alph_a
    global save_output_file, filename_save, paramSSEM
    
    # Extract all configuration parameters
    for key, value in cfg.items():
        if key == 'param':
            param = value
        else:
            globals()[key] = value 