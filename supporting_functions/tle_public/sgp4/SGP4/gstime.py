import numpy as np

def gstime(jdut1):
    """
    Compute Greenwich sidereal time.
    
    Parameters:
    -----------
    jdut1 : float
        Julian date in UT1
    
    Returns:
    --------
    gst : float
        Greenwich sidereal time in radians
    """
    # Algorithm from Vallado's Fundamentals of Astrodynamics and Applications
    tut1 = (jdut1 - 2451545.0) / 36525.0
    
    # Mean sidereal time
    gst = -6.2e-6 * tut1**3 + 0.093104 * tut1**2 + 876600.0 * 3600.0 + 8640184.812866 * tut1 + 307.0
    
    # Convert to radians
    gst = (gst / 240.0) % 360.0  # Convert to degrees and normalize
    gst = gst * np.pi / 180.0    # Convert to radians
    
    return gst 