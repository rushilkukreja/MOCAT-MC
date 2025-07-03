import numpy as np

def dms2rad(deg, min_val, sec):
    """
    This function converts degrees, minutes and seconds into radians.
    
    Author: David Vallado 719-573-2600 27 may 2002
    
    Inputs:
        deg - degrees (0 .. 360)
        min - minutes (0 .. 59)
        sec - seconds (0.0 .. 59.99)
    
    Outputs:
        dms - result (rad)
    
    References:
        Vallado 2007, 203, alg 17 alg 18, ex 3-8
    """
    deg2rad = np.pi / 180.0
    
    # Implementation
    dms = (deg + min_val / 60.0 + sec / 3600.0) * deg2rad
    
    return dms 