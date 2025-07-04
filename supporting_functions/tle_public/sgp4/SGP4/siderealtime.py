import numpy as np

def siderealtime(jdut1, lon):
    """
    Compute local sidereal time.
    
    Parameters:
    -----------
    jdut1 : float
        Julian date in UT1
    lon : float
        Longitude in radians (positive east)
    
    Returns:
    --------
    lst : float
        Local sidereal time in radians
    """
    # Get Greenwich sidereal time
    gst = gstime(jdut1)
    
    # Add longitude to get local sidereal time
    lst = gst + lon
    
    # Normalize to [0, 2π)
    lst = lst % (2 * np.pi)
    
    return lst 