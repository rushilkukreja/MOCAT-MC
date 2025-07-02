"""
Configuration for MC run
Python version of setup_MCconfig.m

setup_MCconfig:
configures constants, scenarios parameters, propagation
time, launch models, propagator selection, collision mode, atmosphere
data, animation, and output files.
"""

import numpy as np
import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent / 'supporting_functions'))

from cfgMC_constants import get_cfgMC_constants
from initSim import initSim
from fillin_atmosphere import fillin_atmosphere

def setup_MCconfig(rngseed, ICfile):
    """
    Setup scenario configuration for MOCAT-MC
    
    Parameters:
    -----------
    rngseed : int
        Random seed for reproducibility
    ICfile : str
        Initial conditions file containing initial condition matrix
        which follows standard mat_sats matrix form
        
    Returns:
    --------
    cfgMC : dict
        Configuration dictionary for function main_mc
        
    Notes:
    ------
    mat_sats matrix indices (0-based):
    idx_a = 0; idx_ecco = 1; idx_inclo = 2; idx_nodeo = 3; idx_argpo = 4; 
    idx_mo = 5; idx_bstar = 6; idx_mass = 7; idx_radius = 8; idx_error = 9; 
    idx_controlled = 10; idx_a_desired = 11; idx_missionlife = 12; 
    idx_constel = 13; idx_date_created = 14; idx_launch_date = 15;
    idx_r = [16 17 18]; idx_v = [19 20 21]; idx_objectclass = 22; idx_ID = 23;
    """
    
    cfgMC = get_cfgMC_constants()
    
    cfgMC['PMD'] = 0.95
    cfgMC['alph'] = 0.01
    cfgMC['alph_a'] = 0
    cfgMC['orbtol'] = 5
    cfgMC['step_control'] = 2
    cfgMC['P_frag'] = 0
    cfgMC['P_frag_cutoff'] = 18
    cfgMC['altitude_limit_low'] = 200
    cfgMC['altitude_limit_up'] = 2000
    cfgMC['missionlifetime'] = 8

    t0_prop = 0
    nyears = 10
    tf_prop = cfgMC['YEAR2MIN'] * nyears
    cfgMC['n_time'] = 730
    cfgMC['tsince'] = np.linspace(t0_prop, tf_prop, cfgMC['n_time'])
    cfgMC['dt_days'] = (cfgMC['tsince'][1] - cfgMC['tsince'][0]) / cfgMC['DAY2MIN']
    
    Simulation = 'TLE'
    launch_model = 'no_launch'
    
    cfgMC['launchRepeatYrs'] = [2018, 2022]
    cfgMC['launchRepeatSmooth'] = 0

    cfgMC = initSim(cfgMC, Simulation, launch_model, ICfile)
    
    paramSSEM = {}
    paramSSEM['N_shell'] = 36
    paramSSEM['h_min'] = cfgMC['altitude_limit_low'] 
    paramSSEM['h_max'] = cfgMC['altitude_limit_up']
    paramSSEM['R02'] = np.linspace(paramSSEM['h_min'], paramSSEM['h_max'], paramSSEM['N_shell'] + 1)
    paramSSEM['re'] = cfgMC['radiusearthkm']
    cfgMC['paramSSEM'] = paramSSEM

    cfgMC['use_sgp4'] = False

    cfgMC['skipCollisions'] = 0
    cfgMC['max_frag'] = np.inf
    
    cfgMC['CUBE_RES'] = 50
    cfgMC['collision_alt_limit'] = 45000
    
    cfgMC = fillin_atmosphere(cfgMC)

    cfgMC['animation'] = 'no'

    cfgMC['save_diaryName'] = ''
    cfgMC['save_output_file'] = 0
    cfgMC['saveMSnTimesteps'] = 146

    if 'time0' in cfgMC:
        filename_save = f'TLEIC_year{cfgMC["time0"].year}_rand{rngseed}.npz'
    else:
        filename_save = f'TLEIC_year2020_rand{rngseed}.npz'
    cfgMC['filename_save'] = filename_save
    cfgMC['n_save_checkpoint'] = np.inf
    
    return cfgMC 