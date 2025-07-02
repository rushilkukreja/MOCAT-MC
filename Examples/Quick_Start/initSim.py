import numpy as np
import scipy.io as sio
from datetime import datetime
import sys
import re
from pathlib import Path

# Add supporting functions to path
sys.path.append(str(Path(__file__).parent.parent.parent / 'supporting_functions'))

from getidx import *
from jd2date import jd2date
from jd2date_simple import jd2date_simple
from getZeroGroups import getZeroGroups
from fillin_physical_parameters import fillin_physical_parameters

def initSim(cfg, Simulation, launch_model, ICfile):
    """
    Initialize simulation with initial conditions and launch configuration
    
    Parameters:
    -----------
    cfg : dict
        Configuration dictionary
    Simulation : str
        Simulation type ('TLE')
    launch_model : str
        Launch model: random, matsat (repeat launch based on matsat), 
        no_launch, data, Somma
    ICfile : str
        Initial conditions file
        
    Returns:
    --------
    cfgMCout : dict
        Updated configuration dictionary
    """
    
    # Parameters
    radiusearthkm = cfg['radiusearthkm']
    
    # TLEs-based initial population + random generation of the launch rate
    try:
        # Find file for initial condition
        fn = ICfile
        if not fn.endswith('.mat'):
            fn += '.mat'
            
        # Load .mat file
        mat_data = sio.loadmat(fn)
        mat_sats = mat_data['mat_sats']
        
        # Try to get time0 from the file, or infer from filename
        if 'time0' in mat_data:
            time0 = mat_data['time0'][0, 0]  # Extract datetime object
        else:
            # Infer time0 from filename (e.g., '2020.mat' -> 2020)
            year_match = re.search(r'(\d{4})\.mat$', fn)
            if year_match:
                year = int(year_match.group(1))
                time0 = datetime(year, 1, 1)  # January 1st of the year
            else:
                # Default to 2020 if we can't infer from filename
                time0 = datetime(2020, 1, 1)
        
        print(f'{mat_sats.shape[0]} satellite entries on {time0} loaded from {fn}')
        
        # Perigees and Apogees
        a_all = mat_sats[:, idx_a] * radiusearthkm
        e_all = mat_sats[:, idx_ecco]
        ap_all = a_all * (1 - e_all)
        aa_all = a_all * (1 + e_all)
        
    except Exception as e:
        print(f'Current path: {Path.cwd()}')
        raise Exception(f'Initial population (.mat) not found in path: {e}')

    # Exclude objects out of the desired altitude_limit_up and altitude_limit_low
    altitude_mask = (ap_all <= (cfg['altitude_limit_up'] + radiusearthkm)) & \
                   (ap_all >= (cfg['altitude_limit_low'] + radiusearthkm))
    mat_sats = mat_sats[altitude_mask, :]

    # Fill in missing DISCOS data if specified
    if 'fillMassRadius' not in cfg:
        fillin_physical_parameters(cfg)
        
    if cfg['fillMassRadius'] == 0:      # don't fill in missing DISCOS data
        g1, g2, g3 = getZeroGroups(mat_sats)  # just get indexes
    elif cfg['fillMassRadius'] == 1:    # ESA's method
        # TODO: Implement fillMassRadiusESA
        g1, g2, g3 = getZeroGroups(mat_sats)
    elif cfg['fillMassRadius'] == 2:    # resampling method
        # TODO: Implement fillMassRadiusResample
        g1, g2, g3 = getZeroGroups(mat_sats)
    else:
        raise ValueError('fillMassRadius must be 0, 1 or 2')
        
    # Mark old payloads as derelict (turn off 'controlled' flag)
    payloadInds = mat_sats[:, idx_objectclass] == 1
    mat_sats[payloadInds, idx_controlled] = 1      # set controlled flag on for all payloads
    derelict_threshold_year = time0.year - cfg['missionlifetime']  # threshold based on mission lifetime and initial condition year
    
    # Convert Julian dates to years for comparison - filter out invalid dates
    valid_mask = np.isfinite(mat_sats[:, idx_launch_date])
    valid_launch_dates = mat_sats[:, idx_launch_date][valid_mask]
    if len(valid_launch_dates) > 0:
        launch_years = np.array([jd2date_simple(jd)[0] for jd in valid_launch_dates])
        # Create a mask for derelicts among valid dates
        valid_derelict_mask = launch_years < derelict_threshold_year
        # Map back to original indices
        ind_derelicts = np.zeros(len(mat_sats), dtype=bool)
        ind_derelicts[valid_mask] = valid_derelict_mask
        # Also mark objects with invalid launch dates as derelict
        ind_derelicts = ind_derelicts | ~valid_mask
    else:
        # If no valid launch dates, mark all payloads as derelict
        ind_derelicts = payloadInds
    
    mat_sats[ind_derelicts, idx_controlled] = 0    # set controlled flag off for derelicts

    # Set launch_model
    if launch_model in ['no_launch', 'no']:  # no launch
        repeatLaunches = np.empty((0, 24))  # empty launches
        launchMC_step = np.empty((0, 24))
        additional_launches = np.empty((0, 24))
        ind_launch = []
        ind_launch_add = []
    elif launch_model in ['random', 'matsat']:  # random launch or repeat launches
        launchMC_step = np.empty((0, 24))
        additional_launches = np.empty((0, 24))
        ind_launch = []
        ind_launch_add = []
        
        if launch_model == 'matsat':
            jds = mat_sats[:, idx_launch_date]       # grab Julian Dates of matsats
            launch_years = np.array([jd2date(jd)[0] for jd in jds])
            ind_inlaunchwindow = (launch_years <= cfg['launchRepeatYrs'][1]) & \
                               (launch_years >= cfg['launchRepeatYrs'][0])
            
            # Create REPEATLAUNCHES based on past launch performance 
            # within the launch window specified by launchRepeatYrs(1) and launchRepeatYrs(2)
            repeatLaunches = mat_sats[ind_inlaunchwindow, :]
            
            # Handle constellations
            if 'constellationFile' in cfg and cfg['constellationFile']:  # with constellation
                ind_constellation = (mat_sats[:, idx_mass] == 260) | (mat_sats[:, idx_mass] == 148)
                repeatLaunches = repeatLaunches[~ind_constellation, :]
                print(f'TLE launch repeat selected \n\t {repeatLaunches.shape[0]} objects total over {cfg["launchRepeatYrs"][1] - cfg["launchRepeatYrs"][0] + 1} years ... \n\t omitting {np.sum(ind_constellation)} constellations from repeatlaunches ...\n\t constellations are launched via cfg.constellation from {cfg["constellationFile"]}')
            else:  # without constellation
                print(f'TLE launch repeat selected ({np.sum(ind_inlaunchwindow)} objects total over {cfg["launchRepeatYrs"][1] - cfg["launchRepeatYrs"][0] + 1} years)')
        else:
            repeatLaunches = np.empty((0, 24))
    elif launch_model in ['data', 'Somma']:
        # TODO: Implement prepare_launch_profile_vec
        repeatLaunches = np.empty((0, 24))
        launchMC_step = np.empty((0, 24))
        additional_launches = np.empty((0, 24))
        ind_launch = []
        ind_launch_add = []
    else:
        raise ValueError('launch_model must be [data] [Somma] [random] [matsat]')

    # Turn on constellation flag for Starlink and Oneweb
    ind_constellation = (mat_sats[:, idx_mass] == 260) | (mat_sats[:, idx_mass] == 148)
    mat_sats[ind_constellation, idx_constel] = 1
    
    if repeatLaunches.size > 0:  # only when repeatLaunches is not empty
        ind_constellation = (repeatLaunches[:, idx_mass] == 260) | (repeatLaunches[:, idx_mass] == 148)
        repeatLaunches[ind_constellation, idx_constel] = 1
        
    if additional_launches.size > 0:
        ind_constellation = (additional_launches[:, idx_mass] == 260) | (additional_launches[:, idx_mass] == 148)
        additional_launches[ind_constellation, idx_constel] = 1

    # Add in mission lifetime
    mat_sats[mat_sats[:, idx_controlled] == 1, idx_missionlife] = cfg['missionlifetime']
    if repeatLaunches.size > 0:  # only when repeatLaunches is not empty
        repeatLaunches[repeatLaunches[:, idx_controlled] == 1, idx_missionlife] = cfg['missionlifetime']
    if additional_launches.size > 0:
        additional_launches[additional_launches[:, idx_controlled] == 1, idx_missionlife] = cfg['missionlifetime']

    # Add in desired_a
    mat_sats[mat_sats[:, idx_controlled] == 1, idx_a_desired] = mat_sats[mat_sats[:, idx_controlled] == 1, idx_a]
    if repeatLaunches.size > 0:  # only when repeatLaunches is not empty
        repeatLaunches[repeatLaunches[:, idx_controlled] == 1, idx_a_desired] = repeatLaunches[repeatLaunches[:, idx_controlled] == 1, idx_a]
    if additional_launches.size > 0:
        additional_launches[additional_launches[:, idx_controlled] == 1, idx_a_desired] = additional_launches[additional_launches[:, idx_controlled] == 1, idx_a]

    # Recalculate Bstar  
    if cfg.get('physicalBstar', 0):
        # Recalculate Bstar as 1/2 * Cd * A/m * rho0;  rho0 = 0.157e6 kg/m^2/RE
        #   Physical def: C_0 = 1/2 * Cd * A/m * rho_0
        #   TLE's use     C_0 = Bstar / 0.157e6 * rho;  [] done in propagation code
        # see line 89 in analytic_propagation_vec.m
        mat_sats[:, idx_bstar] = 0.5 * 2.2 * mat_sats[:, idx_radius]**2 / mat_sats[:, idx_mass] * 0.157
        if repeatLaunches.size > 0:  # only when repeatLaunches is not empty
            repeatLaunches[:, idx_bstar] = 0.5 * 2.2 * repeatLaunches[:, idx_radius]**2 / repeatLaunches[:, idx_mass] * 0.157    

    # Outputs
    cfgMCout = cfg.copy()
    cfgMCout['a_all'] = a_all
    cfgMCout['ap_all'] = ap_all
    cfgMCout['aa_all'] = aa_all
    cfgMCout['mat_sats'] = mat_sats
    cfgMCout['repeatLaunches'] = repeatLaunches
    cfgMCout['time0'] = time0
    cfgMCout['launchMC_step'] = launchMC_step
    cfgMCout['additional_launches'] = additional_launches
    cfgMCout['ind_launch'] = ind_launch
    cfgMCout['ind_launch_add'] = ind_launch_add
    cfgMCout['launch_model'] = launch_model

    return cfgMCout 