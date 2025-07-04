"""
----------------------------------------------------------------------------

    getgravc.py

    This function gets constants for the propagator. Note that mu is identified to
    facilitate comparisons with newer models.

    Author        : David Vallado (original MATLAB)
    Python port   : OpenAI Assistant, 2024

    Inputs:
        whichconst - which set of constants to use  721, 72, 84

    Outputs:
        tumin      - minutes in one time unit
        mu         - earth gravitational parameter
        radiusearthkm - radius of the earth in km
        xke        - reciprocal of tumin
        j2, j3, j4 - un-normalized zonal harmonic values
        j3oj2      - j3 divided by j2

    References:
        NORAD Spacetrack Report #3
        Vallado, Crawford, Hujsak, Kelso  2006
----------------------------------------------------------------------------
"""
import numpy as np

def getgravc(whichconst):
    if whichconst == 721:
        # WGS-72 low precision str#3 constants
        mu = 398600.79964  # in km³/s²
        radiusearthkm = 6378.135  # km
        xke = 0.0743669161
        tumin = 1.0 / xke
        j2 = 0.001082616
        j3 = -0.00000253881
        j4 = -0.00000165597
        j3oj2 = j3 / j2
    
    elif whichconst == 72:
        # WGS-72 constants
        mu = 398600.8  # in km³/s²
        radiusearthkm = 6378.135  # km
        xke = 60.0 / np.sqrt(radiusearthkm**3 / mu)
        tumin = 1.0 / xke
        j2 = 0.001082616
        j3 = -0.00000253881
        j4 = -0.00000165597
        j3oj2 = j3 / j2
    
    elif whichconst == 84:
        # WGS-84 constants
        mu = 398600.5  # in km³/s²
        radiusearthkm = 6378.137  # km
        xke = 60.0 / np.sqrt(radiusearthkm**3 / mu)
        tumin = 1.0 / xke
        j2 = 0.00108262998905
        j3 = -0.00000253215306
        j4 = -0.00000161098761
        j3oj2 = j3 / j2
    
    else:
        raise ValueError(f"Unknown gravity option ({whichconst})")
    
    return tumin, mu, radiusearthkm, xke, j2, j3, j4, j3oj2 