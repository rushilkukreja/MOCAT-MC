"""
Velocity change calculation function
Calculates velocity changes for fragments based on area-to-mass ratio
"""

import numpy as np

def func_dv(Am, frag_type):
    """
    Calculate velocity changes for fragments
    
    Parameters:
    -----------
    Am : array-like
        Area-to-mass ratio in m²/kg
    frag_type : str
        Fragment type ('col' for collision, 'exp' for explosion)
        
    Returns:
    --------
    dv : array-like
        Velocity change in m/s
    """
    
    Am = np.array(Am)
    
    if frag_type.lower() == 'col':
        # Collision velocity changes
        # Based on NASA SBM for collisions
        dv = 0.1 * Am**(-0.5)  # m/s
    elif frag_type.lower() == 'exp':
        # Explosion velocity changes
        # Based on NASA SBM for explosions
        dv = 0.05 * Am**(-0.5)  # m/s
    else:
        raise ValueError("frag_type must be 'col' or 'exp'")
    
    # Ensure minimum velocity change
    dv = np.maximum(dv, 1.0)  # Minimum 1 m/s
    
    return dv 