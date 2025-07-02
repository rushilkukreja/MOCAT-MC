"""
Orbit control vectorized
Python version of orbcontrol_vec.m
"""

import numpy as np
from datetime import timedelta
from astropy.time import Time

def orbcontrol_vec(mat_sat_in, tsince, time0, orbtol, PMD, DAY2MIN, YEAR2DAY, param):
    """
    Orbit control for satellites
    
    Parameters:
    -----------
    mat_sat_in : array-like
        Input satellite data [a,ecco,inclo,nodeo,argpo,mo,controlled,a_desired,missionlife,launched,r,v]
    tsince : float
        Time since epoch [minutes]
    time0 : datetime
        Initial time
    orbtol : float
        Orbit tolerance [km]
    PMD : float
        Post mission disposal probability
    DAY2MIN : float
        Minutes per day
    YEAR2DAY : float
        Days per year
    param : dict
        Parameters dictionary
        
    Returns:
    --------
    mat_sat_out : array-like
        Output satellite data [a,controlled,r,v]
    deorbit : array-like
        Indices of deorbited satellites
    """
    
    # Convert to numpy array if needed
    mat_sat_in = np.asarray(mat_sat_in)
    
    # Calculate current time
    current_time = time0 + timedelta(minutes=tsince)
    
    # Extract input data
    controlled = mat_sat_in[:, 6]
    a_desired = mat_sat_in[:, 7]
    missionlife = mat_sat_in[:, 8]
    launched = mat_sat_in[:, 9]
    
    a_out = mat_sat_in[:, 0].copy()
    r_out = mat_sat_in[:, 10:13].copy()
    v_out = mat_sat_in[:, 13:16].copy()
    
    # Find controlled satellites
    is_controlled = np.where(controlled == 1)[0]
    
    if len(is_controlled) > 0:
        a_current = a_out[is_controlled]  # semi-major axis of controlled satellites
        
        # Identify controlled satellites beyond tolerance
        tolerance_mask = np.abs(a_current - a_desired[is_controlled]) > (orbtol / param['req'])
        find_control = is_controlled[tolerance_mask]
        
        if len(find_control) > 0:
            # Reset semi-major axis of controlled satellites beyond tolerance
            a_out[find_control] = a_desired[find_control]
            
            # Compute new osculating elements
            # TODO: Implement mean2osc_m_vec properly
            # For now, use simple conversion
            osc_oe = simple_mean2osc([a_out[find_control] * param['req'], 
                                    mat_sat_in[find_control, 1:6]], param)
            
            # Reset position and velocity
            # TODO: Implement oe2rv_vec properly
            r_new, v_new = simple_oe2rv_control(osc_oe, param)
            r_out[find_control, :] = r_new
            v_out[find_control, :] = v_new
        
        # Satellites past their mission life
        current_jd = Time(current_time).jd
        launched_jd = launched[is_controlled]
        mission_years = (current_jd - launched_jd) / YEAR2DAY
        life_exceeded = mission_years > missionlife[is_controlled]
        find_life = is_controlled[life_exceeded]
        
        if len(find_life) > 0:
            # Generate random number for each satellite beyond life
            rand_life = np.random.random(len(find_life))
            check_PMD = PMD < rand_life  # check if PMD is fulfilled
            
            # From active becomes inactive
            controlled[find_life[check_PMD]] = 0
            
            # Deorbited satellites
            deorbit = find_life[~check_PMD]
        else:
            deorbit = np.array([])
    else:
        deorbit = np.array([])
    
    # Combine output
    mat_sat_out = np.column_stack([a_out, controlled, r_out, v_out])
    
    return mat_sat_out, deorbit

def simple_mean2osc(mean_oe, param):
    """
    Simple mean to osculating conversion (placeholder)
    """
    # For now, just return mean elements as osculating
    return mean_oe

def simple_oe2rv_control(oe, param):
    """
    Simple orbital elements to position/velocity conversion for control
    """
    # This is a simplified version
    n_objects = len(oe)
    r_eci = np.zeros((n_objects, 3))
    v_eci = np.zeros((n_objects, 3))
    
    # Simple conversion (placeholder)
    for i in range(n_objects):
        a, e, i, omega, w, M = oe[i, :]
        mu = param['mu']
        
        # Convert to position and velocity (simplified)
        r_eci[i, 0] = a * (1 - e**2) / (1 + e * np.cos(M))
        r_eci[i, 1] = 0
        r_eci[i, 2] = 0
        
        v_eci[i, 0] = 0
        v_eci[i, 1] = np.sqrt(mu / a) * (1 + e * np.cos(M))
        v_eci[i, 2] = 0
    
    return r_eci, v_eci 