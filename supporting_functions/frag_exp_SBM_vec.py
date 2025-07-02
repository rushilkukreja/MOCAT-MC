"""
Explosion fragmentation model following NASA EVOLVE 4.0 standard breakup model
Adapted from frag_col_SBM_vec.m for explosion events
"""

import numpy as np
from func_Am import func_Am
from func_dv import func_dv
from func_create_tlesv2_vec import func_create_tlesv2_vec
from filter_objclass_fragments_int import filter_objclass_fragments_int

def frag_exp_SBM_vec(ep, p1_in, param):
    """
    Explosion fragmentation model following NASA EVOLVE 4.0 standard breakup model
    
    Parameters:
    -----------
    ep : float
        Epoch
    p1_in : array-like
        [mass, radius, r_x, r_y, r_z, v_x, v_y, v_z, objectclass]
    param : dict
        Parameter dictionary containing max_frag, mu, req, maxID
        
    Returns:
    --------
    debris1 : array-like
        Debris fragments from explosion
    """
    
    LB = 0.1  # 10 cm lower bound; L_c
    
    p1_mass = p1_in[0]
    p1_radius = p1_in[1]
    p1_r = p1_in[2:5]
    p1_v = p1_in[5:8]
    p1_objclass = p1_in[8]
    
    # For explosions, use total mass of the object
    M = p1_mass
    
    # Calculate number of fragments based on NASA SBM
    num = int(np.floor(0.1 * M**(0.75) * LB**(-1.71) - 0.1 * M**(0.75) * min([1, 2*p1_radius])**(-1.71)))
    
    # Create diameter bins in log space
    dd_edges = np.logspace(np.log10(LB), np.log10(min([1, 2*p1_radius])), 200)
    log10_dd = np.log10(dd_edges)
    dd_means = 10**(log10_dd[:-1] + np.diff(log10_dd)/2)
    
    # Calculate fragment distribution
    nddcdf = 0.1 * M**(0.75) * dd_edges**(-1.71)
    ndd = np.maximum(0, -np.diff(nddcdf))
    floor_ndd = np.floor(ndd)
    rand_sampling = np.random.random(len(ndd))
    add_sampling = rand_sampling > (1 - (ndd - floor_ndd))
    d_pdf = np.repeat(dd_means, floor_ndd.astype(int) + add_sampling.astype(int))
    
    # Randomly sample diameters
    d = d_pdf[np.random.permutation(len(d_pdf))]
    
    # Calculate fragment properties
    A = 0.556945 * d**(2.0047077)  # Area calculation
    Am = func_Am(d, p1_objclass)   # Area-to-mass ratio
    m = A / Am                     # Mass calculation
    
    # Handle mass constraints
    if np.sum(m) < M:
        # Sort by mass and keep smallest objects until mass constraint is met
        sort_idx = np.argsort(m)
        cumsum_m = np.cumsum(m[sort_idx])
        last_idx = np.where(cumsum_m < M)[0]
        if len(last_idx) > 0:
            last_idx = last_idx[-1]
            valid_idx = sort_idx[:last_idx+1]
            m = m[valid_idx]
            d = d[valid_idx]
            A = A[valid_idx]
            Am = Am[valid_idx]
    
    # Calculate remaining mass for remnant
    m_rem = M - np.sum(m)
    if m_rem > M/1000:  # If remaining mass is significant
        d_rem_approx = (m_rem / p1_mass * p1_radius**3)**(1/3) * 2
        Am_rem = func_Am(d_rem_approx, p1_objclass)
        A_rem = m_rem * Am_rem
        d_rem = d_rem_approx
    else:
        d_rem = np.array([])
        A_rem = np.array([])
        Am_rem = np.array([])
        m_rem = np.array([])
    
    # Calculate velocity changes
    dv = func_dv(np.concatenate([Am, Am_rem]), 'exp') / 1000  # km/s
    
    # Random velocity directions
    u = np.random.random(len(dv)) * 2 - 1
    theta = np.random.random(len(dv)) * 2 * np.pi
    
    v = np.sqrt(1 - u**2)
    p = np.column_stack([v * np.cos(theta), v * np.sin(theta), u])
    dv_vec = p * dv[:, np.newaxis]
    
    # Create fragments array
    fragments = np.column_stack([
        np.concatenate([d, d_rem]),
        np.concatenate([A, A_rem]),
        np.concatenate([Am, Am_rem]),
        np.concatenate([m, m_rem]),
        dv,
        dv_vec[:, 0],
        dv_vec[:, 1],
        dv_vec[:, 2]
    ])
    
    # Remove fragments smaller than lower bound
    fragments = fragments[fragments[:, 0] >= LB]
    
    # Create debris objects
    debris1 = func_create_tlesv2_vec(ep, p1_r, p1_v, p1_objclass, fragments, 
                                    param['max_frag'], param['mu'], param['req'], param['maxID'])
    
    return debris1 