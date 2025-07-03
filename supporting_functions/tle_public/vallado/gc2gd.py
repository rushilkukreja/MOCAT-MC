import numpy as np

def gc2gd(latgc):
    """
    This function converts from geodetic to geocentric latitude for positions
    on the surface of the earth. Notice that (1-f) squared = 1-esqrd.
    
    Author: David Vallado 719-573-2600 21 jun 2002
    
    Inputs:
        latgc - geocentric latitude (-pi to pi rad)
    
    Outputs:
        latgd - geodetic latitude (-pi to pi rad)
    
    References:
        Vallado 2001, 146, eq 3-11
    """
    eesqrd = 0.006694385000  # Eccentricity of earth sqrd
    
    # Implementation
    latgd = np.arctan(np.tan(latgc) / (1.0 - eesqrd))
    
    return latgd 