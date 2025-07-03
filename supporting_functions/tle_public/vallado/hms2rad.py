import numpy as np

def hms2rad(hr, min_val, sec):
    """
    This function converts hours, minutes and seconds into radians. Notice
    the conversion 0.2617 is simply the radian equivalent of 15 degrees.
    
    Author: David Vallado 719-573-2600 27 may 2002
    
    Inputs:
        hr - hours (0 .. 24)
        min - minutes (0 .. 59)
        sec - seconds (0.0 .. 59.99)
    
    Outputs:
        hms - result (rad)
    
    References:
        Vallado 2007, 204, alg 19 alg 20, ex 3-9
    """
    # Implementation
    temp = 15.0 * np.pi / 180.0
    
    hms = (hr + min_val / 60.0 + sec / 3600.0) * temp
    
    return hms 