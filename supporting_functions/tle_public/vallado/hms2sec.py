import numpy as np

def hms2sec(hr, min_val, sec):
    """
    This function converts hours, minutes and seconds into seconds from the
    beginning of the day.
    
    Author: David Vallado 719-573-2600 27 may 2002
    
    Inputs:
        hr - hours (0 .. 24)
        min - minutes (0 .. 59)
        sec - seconds (0.0 .. 59.99)
    
    Outputs:
        utsec - seconds (0.0 .. 86400.0)
    """
    # Implementation
    utsec = hr * 3600.0 + min_val * 60.0 + sec
    
    return utsec 