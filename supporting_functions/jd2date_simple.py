"""
Julian date to Gregorian calendar date conversion (Simplified)
Python version of jd2date.m - No external dependencies
"""

import math
from datetime import datetime, timedelta

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
    
    # Convert to list if needed
    if hasattr(jd, '__iter__') and not isinstance(jd, str):
        jd_list = list(jd)
        results = []
        for jd_val in jd_list:
            results.append(_jd2date_single(jd_val))
        return results
    else:
        return _jd2date_single(jd)

def _jd2date_single(jd):
    """Convert single Julian day to date"""
    
    # Adding 0.5 to JD and taking FLOOR ensures that the date is correct
    ijd = int(jd + 0.5)  # integer part
    fjd = jd - ijd + 0.5  # fraction part
    
    # Convert fraction to time
    total_seconds = int(fjd * 24 * 3600)
    hour = total_seconds // 3600
    minute = (total_seconds % 3600) // 60
    second = total_seconds % 60
    
    # The following algorithm is from the Calendar FAQ
    a = ijd + 32044
    b = (4 * a + 3) // 146097
    c = a - (b * 146097) // 4
    
    d = (4 * c + 3) // 1461
    e = c - (1461 * d) // 4
    m = (5 * e + 2) // 153
    
    day = e - (153 * m + 2) // 5 + 1
    month = m + 3 - 12 * (m // 10)
    year = b * 100 + d - 4800 + (m // 10)
    
    return year, month, day, hour, minute, second

def jd2date_simple(jd):
    """
    Simplified version that returns only year, month, day
    """
    result = jd2date(jd)
    if isinstance(result, list):
        return [(r[0], r[1], r[2]) for r in result]
    else:
        return result[0], result[1], result[2] 