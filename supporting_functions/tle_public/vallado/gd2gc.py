"""
-----------------------------------------------------------------------------

    gd2gc.py

    This function converts from geodetic to geocentric latitude for positions
    on the surface of the earth. Notice that (1-f) squared = 1-esqrd.

    Author        : David Vallado (original MATLAB)
    Python port   : OpenAI Assistant, 2024

    Inputs:
        latgd     - geodetic latitude              -pi to pi rad

    Outputs:
        latgc     - geocentric latitude            -pi to pi rad

    References:
        Vallado 2001, 146, eq 3-11
-----------------------------------------------------------------------------
"""
import numpy as np

def gd2gc(latgd):
    eesqrd = 0.006694385000  # eccentricity of earth squared
    
    # Implementation
    latgc = np.arctan((1.0 - eesqrd) * np.tan(latgd))
    
    return latgc 