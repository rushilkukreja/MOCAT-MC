"""
MIT propagator vectorized
Python version of prop_mit_vec.m
"""

import numpy as np

def prop_mit_vec(mat_sat_in, t, param):
    """
    MIT propagator for orbital elements
    
    Parameters:
    -----------
    mat_sat_in : array-like
        Input orbital elements [a,ecco,inclo,nodeo,argpo,mo,Bstar,controlled]
    t : float
        Propagation time [seconds]
    param : dict
        Propagation parameters
        
    Returns:
    --------
    mat_sat_out : array-like
        Output orbital elements and state vectors [a,ecco,inclo,nodeo,argpo,mo,errors,r_eci,v_eci]
    """
    
    mat_sat_in = np.asarray(mat_sat_in)
    
    req = param['req']
    
    param['t'] = t
    param['t_0'] = 0
    
    n_sat = mat_sat_in.shape[0]
    
    in_mean_oe = np.column_stack([req * mat_sat_in[:, 0], mat_sat_in[:, 1:6]])
    
    Bstar = np.abs(mat_sat_in[:, 6])
    Bstar[Bstar < 1e-12] = 9.7071e-05
    
    out_mean_oe = np.zeros((n_sat, 6))
    errors = np.zeros(n_sat)
    
    idx_notdecay = in_mean_oe[:, 0] * (1 - in_mean_oe[:, 1]) > req + 150
    idx_controlled = mat_sat_in[:, 7] == 1
    idx_propagate = idx_notdecay & ~idx_controlled
    
    if np.any(idx_propagate):
        param['Bstar'] = Bstar[idx_propagate]
        out_mean_oe[idx_propagate, :], errors[idx_propagate] = simple_keplerian_propagation(
            in_mean_oe[idx_propagate, :], param)
    
    out_mean_oe[~idx_propagate, :] = in_mean_oe[~idx_propagate, :]
    
    controlled_mask = idx_controlled & idx_notdecay
    if np.any(controlled_mask):
        mean_motion = np.sqrt(param['mu'] / out_mean_oe[controlled_mask, 0]**3)
        out_mean_oe[controlled_mask, 5] += mean_motion * t
    
    check_alt_ecc = (out_mean_oe[:, 0] * (1 - out_mean_oe[:, 1]) > req + 150) & (out_mean_oe[:, 1] < 1)
    errors[~check_alt_ecc] = 1
    
    osc_oe = np.zeros((n_sat, 6))
    E_osc = np.zeros(n_sat)
    
    if np.any(check_alt_ecc):
        osc_oe[check_alt_ecc, :] = out_mean_oe[check_alt_ecc, :]
        E_osc[check_alt_ecc] = out_mean_oe[check_alt_ecc, 5]
    
    out_mean_oe[:, 0] = out_mean_oe[:, 0] / req
    osc_oe[~check_alt_ecc, :] = out_mean_oe[~check_alt_ecc, :]
    
    r_eci = np.zeros((n_sat, 3))
    v_eci = np.zeros((n_sat, 3))
    
    if np.any(check_alt_ecc):
        valid_indices = np.where(check_alt_ecc)[0]
        r_temp, v_temp = simple_oe2rv(
            osc_oe[valid_indices, :], E_osc[valid_indices], param)
        r_eci[valid_indices, :] = r_temp
        v_eci[valid_indices, :] = v_temp
    
    mat_sat_out = np.column_stack([out_mean_oe, errors, r_eci, v_eci])
    
    return mat_sat_out

def simple_keplerian_propagation(mean_oe, param):
    """
    Simple Keplerian propagation (placeholder for analytic_propagation_vec)
    """
    out_oe = mean_oe.copy()
    errors = np.zeros(len(mean_oe))
    
    mean_motion = np.sqrt(param['mu'] / mean_oe[:, 0]**3)
    out_oe[:, 5] += mean_motion * param['t']
    
    return out_oe, errors

def simple_oe2rv(oe, E, param):
    """
    Simple orbital elements to position/velocity conversion (placeholder for oe2rv_vec)
    """
    n_objects = len(oe)
    r_eci = np.zeros((n_objects, 3))
    v_eci = np.zeros((n_objects, 3))
    
    for i in range(n_objects):
        a, e, i_ang, omega, w, M = oe[i, :]
        mu = param['mu']
        
        r_eci[i, 0] = a * (1 - e**2) / (1 + e * np.cos(M))
        r_eci[i, 1] = 0
        r_eci[i, 2] = 0
        
        v_eci[i, 0] = 0
        v_eci[i, 1] = np.sqrt(mu / a) * (1 + e * np.cos(M))
        v_eci[i, 2] = 0
    
    return r_eci, v_eci 