import numpy as np

def invjday(jd):
    """
    Convert Julian day number to calendar date.
    
    Parameters:
    -----------
    jd : float
        Julian day number
    
    Returns:
    --------
    year : int
        Year
    mon : int
        Month (1-12)
    day : int
        Day of month (1-31)
    hr : int
        Hour (0-23)
    minute : int
        Minute (0-59)
    sec : float
        Second (0-59.999...)
    """
    # Algorithm from Vallado's Fundamentals of Astrodynamics and Applications
    jd_frac = jd + 0.5
    z = np.floor(jd_frac)
    f = jd_frac - z
    
    if z < 2299161:
        a = z
    else:
        alpha = np.floor((z - 1867216.25) / 36524.25)
        a = z + 1 + alpha - np.floor(alpha / 4)
    
    b = a + 1524
    c = np.floor((b - 122.1) / 365.25)
    d = np.floor(365.25 * c)
    e = np.floor((b - d) / 30.6001)
    
    day = b - d - np.floor(30.6001 * e) + f
    
    if e < 14:
        mon = e - 1
    else:
        mon = e - 13
    
    if mon > 2:
        year = c - 4716
    else:
        year = c - 4715
    
    # Extract time components
    hr = np.floor(f * 24)
    minute = np.floor((f * 24 - hr) * 60)
    sec = (f * 24 - hr - minute / 60) * 3600
    
    return int(year), int(mon), int(day), int(hr), int(minute), sec 