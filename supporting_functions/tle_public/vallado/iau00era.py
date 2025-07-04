"""
----------------------------------------------------------------------------

    iau00era.py

    This function calculates the transformation matrix that accounts for the
    effects of sidereal time via the earth rotation angle.

    Author        : David Vallado (original MATLAB)
    Python port   : OpenAI Assistant, 2024

    Inputs:
        jdut1     - julian date of ut1             days

    Outputs:
        st        - transformation matrix for pef-ire

    References:
        Vallado 2004, 212
----------------------------------------------------------------------------
"""
import numpy as np

def iau00era(jdut1):
    twopi = 2.0 * np.pi
    
    # Julian centuries of ut1
    tut1d = jdut1 - 2451545.0
    
    # Earth rotation angle
    era = twopi * (0.7790572732640 + 1.00273781191135448 * tut1d)
    era = era % twopi
    
    # Transformation matrix
    st = np.array([
        [np.cos(era), -np.sin(era), 0.0],
        [np.sin(era), np.cos(era), 0.0],
        [0.0, 0.0, 1.0]
    ])
    
    return st 