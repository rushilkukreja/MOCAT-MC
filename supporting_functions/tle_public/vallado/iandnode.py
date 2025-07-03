import numpy as np

def iandnode(iinit, deltaomega, ifinal, vinit, fpa):
    """
    This procedure calculates the delta v's for a change in inclination and
    longitude of ascending node.
    
    Author: David Vallado 719-573-2600 1 mar 2001
    
    Inputs:
        vinit - initial velocity vector (er/tu)
        iinit - initial inclination (rad)
        fpa - flight path angle (rad)
        deltaomega - change in node (rad)
        deltai - change in inclination (rad)
        rfinal - final position magnitude (er)
    
    Outputs:
        ifinal - final inclination (rad)
        deltav - change in velocity (er/tu)
    
    References:
        Vallado 2007, 350, alg 41, ex 6-6
    """
    rad = 57.29577951308230
    deltai = iinit - ifinal
    theta = np.arccos(np.cos(iinit) * np.cos(ifinal) + 
                      np.sin(iinit) * np.sin(ifinal) * np.cos(deltaomega))
    deltav = 2.0 * vinit * np.cos(fpa) * np.sin(0.5 * theta)
    
    arglat = np.arccos((np.sin(ifinal) * np.cos(deltaomega) - 
                        np.cos(theta) * np.sin(iinit)) / (np.sin(theta) * np.cos(iinit)))
    arglat1 = np.arccos((np.cos(iinit) * np.sin(ifinal) - 
                         np.sin(iinit) * np.cos(ifinal) * np.cos(deltaomega)) / np.sin(theta))
    
    return deltav 