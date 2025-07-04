import numpy as np

def jday(year, mon, day, hr, minute, sec):
    """
    Convert calendar date to Julian day number.
    
    Parameters:
    -----------
    year : int
        Year (e.g., 2021)
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
    
    Returns:
    --------
    jd : float
        Julian day number
    jdfrac : float
        Fractional part of Julian day
    """
    # Algorithm from Vallado's Fundamentals of Astrodynamics and Applications
    if year < 1900:
        year = year + 1900
    
    if mon <= 2:
        year = year - 1
        mon = mon + 12
    
    jd = np.floor(365.25 * (year + 4716)) + np.floor(30.6001 * (mon + 1)) + day - 1524.5
    
    # Add time of day
    jdfrac = hr / 24.0 + minute / 1440.0 + sec / 86400.0
    
    return jd + jdfrac, jdfrac 