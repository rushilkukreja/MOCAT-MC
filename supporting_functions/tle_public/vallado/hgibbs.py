import numpy as np

def hgibbs(r1, r2, r3, jd1, jd2, jd3):
    """
    This function implements the herrick-gibbs approximation for orbit
    determination, and finds the middle velocity vector for the 3 given
    position vectors.
    
    Author: David Vallado 719-573-2600 1 mar 2001
    
    Inputs:
        r1 - ijk position vector #1 (km)
        r2 - ijk position vector #2 (km)
        r3 - ijk position vector #3 (km)
        jd1 - julian date of 1st sighting (days from 4713 bc)
        jd2 - julian date of 2nd sighting (days from 4713 bc)
        jd3 - julian date of 3rd sighting (days from 4713 bc)
    
    Outputs:
        v2 - ijk velocity vector for r2 (km/s)
        theta - angl between vectors (rad)
        error - flag indicating success ('ok',...)
    
    References:
        Vallado 2007, 462, alg 52, ex 7-4
    """
    def mag(vec):
        return np.linalg.norm(vec)
    
    def cross(vec1, vec2):
        return np.cross(vec1, vec2)
    
    def dot(vec1, vec2):
        return np.dot(vec1, vec2)
    
    def unit(vec):
        return vec / mag(vec)
    
    def angl(vec1, vec2):
        # Placeholder for angl function
        return np.arccos(dot(vec1, vec2) / (mag(vec1) * mag(vec2)))
    
    # Constants
    mu = 3.986004418e5
    
    error = '          ok'
    theta = 0.0
    theta1 = 0.0
    magr1 = mag(r1)
    magr2 = mag(r2)
    magr3 = mag(r3)
    v2 = np.zeros(3)
    
    tolangle = 0.01745329251994
    dt21 = (jd2 - jd1) * 86400.0
    dt31 = (jd3 - jd1) * 86400.0  # Differences in times
    dt32 = (jd3 - jd2) * 86400.0
    
    p = cross(r2, r3)
    pn = unit(p)
    r1n = unit(r1)
    copa = np.arcsin(dot(pn, r1n))
    
    if abs(dot(r1n, pn)) > 0.017452406:
        error = 'not coplanar'
    
    # Check the size of the angles between the three position vectors.
    # Herrick gibbs only gives "reasonable" answers when the
    # position vectors are reasonably close. 10 deg is only an estimate.
    theta = angl(r1, r2)
    theta1 = angl(r2, r3)
    
    if (theta > tolangle) or (theta1 > tolangle):
        error = '   angl > 1°'
    
    # Perform herrick-gibbs method to find v2
    term1 = -dt32 * (1.0 / (dt21 * dt31) + mu / (12.0 * magr1 * magr1 * magr1))
    term2 = (dt32 - dt21) * (1.0 / (dt21 * dt32) + mu / (12.0 * magr2 * magr2 * magr2))
    term3 = dt21 * (1.0 / (dt32 * dt31) + mu / (12.0 * magr3 * magr3 * magr3))
    
    v2 = term1 * r1 + term2 * r2 + term3 * r3
    
    return v2, theta, theta1, copa, error 