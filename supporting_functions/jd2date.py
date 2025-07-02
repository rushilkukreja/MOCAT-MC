"""
Julian date to Gregorian calendar date conversion
Python version of jd2date.m
"""

import numpy as np
from astropy.time import Time
from datetime import datetime

def jd2date(jd):
    """
    Convert Julian day number to Gregorian calendar date
    
    Parameters:
    -----------
    jd : float or array-like
        Julian day number(s)
        
    Returns:
    --------
    year : int or array
        Year
    month : int or array  
        Month (1-12)
    day : int or array
        Day (1-31)
    hour : int or array, optional
        Hour (0-23) - only returned if requested
    minute : int or array, optional
        Minute (0-59) - only returned if requested  
    second : float or array, optional
        Second (0-59.999...) - only returned if requested
        
    Notes:
    ------
    Start of the JD (Julian day) count is from 0 at 12 noon 1 JAN -4712
    (4713 BC), Julian proleptic calendar. This day count conforms with the
    astronomical convention starting the day at noon, in contrast with the
    civil practice where the day starts with midnight.
    """
    
    jd = np.asarray(jd)
    
    t = Time(jd, format='jd')
    
    year = t.datetime.year
    month = t.datetime.month  
    day = t.datetime.day
    hour = t.datetime.hour
    minute = t.datetime.minute
    second = t.datetime.second + t.datetime.microsecond / 1e6
    
    if jd.ndim == 0:
        return year, month, day, hour, minute, second
    else:
        return year, month, day, hour, minute, second

def jd2date_simple(jd):
    """
    Simplified version that returns only year, month, day
    """
    year, month, day, _, _, _ = jd2date(jd)
    return year, month, day 