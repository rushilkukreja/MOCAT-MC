"""
Collision fragmentation model following NASA EVOLVE 4.0 standard breakup model
Based on frag_col_SBM_vec.m
"""

import numpy as np
from func_Am import func_Am
from func_dv import func_dv
from func_create_tlesv2_vec import func_create_tlesv2_vec

def frag_col_SBM_vec(ep, p1_in, p2_in, param):
    """
    Collision model following NASA EVOLVE 4.0 standard breakup model (2001)
    
    Parameters:
    -----------
    ep : float
        Epoch
    p1_in : array-like
        [mass, radius, r_x, r_y, r_z, v_x, v_y, v_z, objectclass]
    p2_in : array-like
        [mass, radius, r_x, r_y, r_z, v_x, v_y, v_z, objectclass]
    param : dict
        Parameter dictionary containing max_frag, mu, req, maxID
        
    Returns:
    --------
    debris1 : array-like
        Debris fragments from object 1
    debris2 : array-like
        Debris fragments from object 2
    """
    
    LB = 0.1  # 10 cm lower bound; L_c
    
    # Ensure p1_mass > p2_mass, or p1_radius > p2_radius if p1_mass == p2_mass
    if p1_in[0] < p2_in[0] or (p1_in[0] == p2_in[0] and p1_in[1] < p2_in[1]):
        temp1 = p1_in.copy()
        temp2 = p2_in.copy()
        p1_in = temp2
        p2_in = temp1
    
    p1_mass = p1_in[0]
    p1_radius = p1_in[1]
    p1_r = p1_in[2:5]
    p1_v = p1_in[5:8]
    p1_objclass = p1_in[8]
    
    p2_mass = p2_in[0]
    p2_radius = p2_in[1]
    p2_r = p2_in[2:5]
    p2_v = p2_in[5:8]
    p2_objclass = p2_in[8]
    
    # Calculate relative velocity
    dv = np.linalg.norm(p1_v - p2_v)  # km/s
    
    # Calculate catastrophic ratio (specific energy)
    catastrophRatio = (p2_mass * (dv * 1000)**2) / (2 * p1_mass * 1000)  # J/g
    
    # Determine if catastrophic collision (> 40 J/g)
    if catastrophRatio < 40:
        M = p2_mass * dv**2  # Non-catastrophic
        isCatastrophic = 0
    else:
        M = p1_mass + p2_mass  # Catastrophic
        isCatastrophic = 1
    
    # Calculate number of fragments
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
    
    # Handle mass constraints and create fragments
    if np.sum(m) < M:
        if isCatastrophic:
            # Catastrophic collision - complex mass distribution
            largeidx = (d > p2_radius*2 | m > p2_mass) & (d < p1_radius*2)
            m_assigned_large = np.max([0, np.sum(m[largeidx])])
            
            if m_assigned_large > p1_mass:
                # Sort by mass and keep smallest objects
                idx_large = np.where(largeidx)[0]
                sort_idx = np.argsort(m[idx_large])
                cumsum_m1 = np.cumsum(m[idx_large[sort_idx]])
                lastidx1 = np.max([0, np.where(cumsum_m1 < p1_mass)[0][-1] if len(np.where(cumsum_m1 < p1_mass)[0]) > 0 else -1])
                
                # Remove excess fragments
                remove_idx = idx_large[sort_idx[lastidx1+1:]]
                m = np.delete(m, remove_idx)
                d = np.delete(d, remove_idx)
                A = np.delete(A, remove_idx)
                Am = np.delete(Am, remove_idx)
                largeidx = np.delete(largeidx, remove_idx)
                
                if lastidx1 == 0:
                    m_assigned_large = 0
                else:
                    m_assigned_large = cumsum_m1[lastidx1]
            
            # Calculate remnant mass
            m_remSum = M - np.sum(m)
            if m_remSum > 0:
                # Create remnant fragments
                num_rem = np.random.randint(2, 9)
                remDist = np.random.random(num_rem)
                m_rem = m_remSum * remDist / np.sum(remDist)
                
                # Calculate remnant properties
                d_rem_approx = (m_rem / p1_mass * p1_radius**3)**(1/3) * 2
                Am_rem = func_Am(d_rem_approx, p1_objclass)
                A_rem = m_rem * Am_rem
                d_rem = d_rem_approx
            else:
                m_rem = np.array([])
                d_rem = np.array([])
                A_rem = np.array([])
                Am_rem = np.array([])
        else:
            # Non-catastrophic collision
            m_remSum = M - np.sum(m)
            if m_remSum > 0:
                m_rem = m_remSum
                d_rem_approx = (m_rem / p1_mass * p1_radius**3)**(1/3) * 2
                Am_rem = func_Am(d_rem_approx, p1_objclass)
                A_rem = m_rem * Am_rem
                d_rem = d_rem_approx
            else:
                m_rem = np.array([])
                d_rem = np.array([])
                A_rem = np.array([])
                Am_rem = np.array([])
    else:
        # Sort by mass and keep smallest objects until mass constraint is met
        sort_idx = np.argsort(m)
        cumsum_m = np.cumsum(m[sort_idx])
        lastidx = np.where(cumsum_m < M)[0]
        if len(lastidx) > 0:
            lastidx = lastidx[-1]
            valid_idx = sort_idx[:lastidx+1]
            m = m[valid_idx]
            d = d[valid_idx]
            A = A[valid_idx]
            Am = Am[valid_idx]
        
        # Calculate remnant
        m_rem = M - np.sum(m)
        if m_rem > M/1000:
            d_rem_approx = (m_rem / p1_mass * p1_radius**3)**(1/3) * 2
            Am_rem = func_Am(d_rem_approx, p1_objclass)
            A_rem = m_rem * Am_rem
            d_rem = d_rem_approx
        else:
            m_rem = np.array([])
            d_rem = np.array([])
            A_rem = np.array([])
            Am_rem = np.array([])
    
    # Calculate velocity changes
    dv = func_dv(np.concatenate([Am, Am_rem]), 'col') / 1000  # km/s
    
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
    
    # Distribute fragments between parent objects
    # Simplified distribution: assign based on mass ratio
    total_mass = p1_mass + p2_mass
    p1_ratio = p1_mass / total_mass
    
    # Randomly assign fragments
    n_frag = len(fragments)
    p1_fragments = fragments[:int(n_frag * p1_ratio)]
    p2_fragments = fragments[int(n_frag * p1_ratio):]
    
    # Create debris objects
    debris1 = func_create_tlesv2_vec(ep, p1_r, p1_v, p1_objclass, p1_fragments, 
                                    param['max_frag'], param['mu'], param['req'], param['maxID'])
    
    param['maxID'] = param['maxID'] + len(debris1)
    
    debris2 = func_create_tlesv2_vec(ep, p2_r, p2_v, p2_objclass, p2_fragments, 
                                    param['max_frag'], param['mu'], param['req'], param['maxID'])
    
    return debris1, debris2 