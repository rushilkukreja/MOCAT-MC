"""
Collision probability vector calculation
Python version of collision_prob_vec.m
"""

import numpy as np

def collision_prob_vec(p1_radius, p1_v, p2_radius, p2_v, CUBE_RES):
    """
    Calculate collision probability between objects
    
    Parameters:
    -----------
    p1_radius : array-like
        Radius of first object(s) [m]
    p1_v : array-like
        Velocity of first object(s) [km/s], shape (n_sats, 3)
    p2_radius : array-like
        Radius of second object(s) [m]  
    p2_v : array-like
        Velocity of second object(s) [km/s], shape (n_sats, 3)
    CUBE_RES : float
        Cube resolution [km]
        
    Returns:
    --------
    pr : array-like
        Collision probability
    """
    
    p1_radius = np.asarray(p1_radius)
    p1_v = np.asarray(p1_v)
    p2_radius = np.asarray(p2_radius)
    p2_v = np.asarray(p2_v)
    
    sigma = (p1_radius + p2_radius)**2 * (np.pi / 1e6)
    
    dU = CUBE_RES**3
    
    Vimp = np.sqrt(np.sum((p1_v - p2_v)**2, axis=1))
    
    pr = Vimp / dU * sigma
    
    return pr 