"""
----------------------------------------------------------------------------

    gstime0.py

    This function finds the Greenwich sidereal time at the beginning of a year.
    This formula is derived from the astronomical almanac and is good only
    0 hr ut1, jan 1 of a year.

    Author        : David Vallado (original MATLAB)
    Python port   : OpenAI Assistant, 2024

    Inputs:
        year      - year                           1998, 1999, etc.

    Outputs:
        gst0      - greenwich sidereal time        0 to 2pi rad

    References:
        Vallado 2007, 195, Eq 3-46
----------------------------------------------------------------------------
"""
import numpy as np

def gstime0(year):
    twopi = 2.0 * np.pi
    
    # Implementation
    jd = (367.0 * year - np.floor((7 * (year + np.floor(10/12))) * 0.25) + 
          np.floor(275/9) + 1721014.5)
    tut1 = (jd - 2451545.0) / 36525.0
    
    temp = (-6.2e-6 * tut1**3 + 0.093104 * tut1**2 + 
            (876600.0 * 3600.0 + 8640184.812866) * tut1 + 67310.54841)
    
    # Check quadrants
    temp = temp % twopi
    if temp < 0.0:
        temp = temp + twopi
    
    gst0 = temp
    
    return gst0 