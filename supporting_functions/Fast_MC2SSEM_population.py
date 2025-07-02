"""
Fast MC to SSEM population calculation
Converts Monte Carlo simulation results to SSEM population format
"""

import numpy as np

def Fast_MC2SSEM_population(sats_info, paramSSEM):
    """
    Convert Monte Carlo simulation results to SSEM population format
    
    Parameters:
    -----------
    sats_info : list
        [object_class, semi_major_axis, controlled_status]
    paramSSEM : dict
        SSEM parameters including R02 (altitude bins)
        
    Returns:
    --------
    S_MC : array
        Satellite population in each altitude bin
    D_MC : array
        Derelict population in each altitude bin
    N_MC : array
        Debris population in each altitude bin
    """
    
    objclass = sats_info[0]
    a = sats_info[1]
    controlled = sats_info[2]
    
    # Calculate altitudes (convert from Earth radii to km)
    altitudes = (a - 1) * paramSSEM['re']  # km
    
    # Initialize population arrays
    n_bins = len(paramSSEM['R02']) - 1
    S_MC = np.zeros(n_bins)
    D_MC = np.zeros(n_bins)
    N_MC = np.zeros(n_bins)
    
    # Categorize objects by altitude and type
    for i in range(len(objclass)):
        alt = altitudes[i]
        obj_type = objclass[i]
        is_controlled = controlled[i]
        
        # Find altitude bin
        bin_idx = np.where((paramSSEM['R02'][:-1] <= alt) & (alt < paramSSEM['R02'][1:]))[0]
        if len(bin_idx) > 0:
            bin_idx = bin_idx[0]
            
            # Categorize by object type and control status
            if obj_type == 1 and is_controlled:  # Active satellite
                S_MC[bin_idx] += 1
            elif obj_type == 1 and not is_controlled:  # Derelict satellite
                D_MC[bin_idx] += 1
            elif obj_type == 2:  # Debris
                N_MC[bin_idx] += 1
            elif obj_type == 5:  # Rocket body
                D_MC[bin_idx] += 1
    
    return S_MC, D_MC, N_MC 