"""
----------------------------------------------------------------------------

    gstime.py

    This function finds the Greenwich sidereal time (IAU-82).

    Author        : David Vallado (original MATLAB)
    Python port   : OpenAI Assistant, 2024

    Inputs:
        jdut1     - julian date of ut1             days from 4713 bc

    Outputs:
        gst       - greenwich sidereal time        0 to 2pi rad

    References:
        Vallado 2007, 193, Eq 3-43
----------------------------------------------------------------------------
"""
import numpy as np

def gstime(jdut1):
    twopi = 2.0 * np.pi
    deg2rad = np.pi / 180.0
    
    # Implementation
    tut1 = (jdut1 - 2451545.0) / 36525.0
    
    temp = (-6.2e-6 * tut1**3 + 0.093104 * tut1**2 + 
            (876600.0 * 3600.0 + 8640184.812866) * tut1 + 67310.54841)
    
    # 360/86400 = 1/240, to deg, to rad
    temp = (temp * deg2rad / 240.0) % twopi
    
    # Check quadrants
    if temp < 0.0:
        temp = temp + twopi
    
    gst = temp
    
    return gst 