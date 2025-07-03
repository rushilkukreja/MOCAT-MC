import numpy as np

def hohmann(rinit, rfinal, einit, efinal, nuinit, nufinal):
    """
    This procedure calculates the delta v's for a hohmann transfer for either
    circle to circle, or ellipse to ellipse.
    
    Author: David Vallado 719-573-2600 1 mar 2001
    
    Inputs:
        rinit - initial position magnitude (er)
        rfinal - final position magnitude (er)
        einit - eccentricity of first orbit
        efinal - eccentricity of final orbit
        nuinit - true anomaly of first orbit (0 or pi rad)
        nufinal - true anomaly of final orbit (0 or pi rad)
    
    Outputs:
        deltava - change in velocity at point a (er/tu)
        deltavb - change in velocity at point b (er/tu)
        dttu - time of flight for the trans (tu)
    
    References:
        Vallado 2007, 327, alg 36, ex 6-1
    """
    # Initialize values
    mu = 1.0  # Canonical units
    ainit = (rinit * (1.0 + einit * np.cos(nuinit))) / (1.0 - einit * einit)
    atran = (rinit + rfinal) / 2.0
    afinal = (rfinal * (1.0 + efinal * np.cos(nufinal))) / (1.0 - efinal * efinal)
    deltava = 0.0
    deltavb = 0.0
    dttu = 0.0
    
    if (einit < 1.0) or (efinal < 1.0):
        # Find delta v at point a
        vinit = np.sqrt((2.0 * mu) / rinit - (mu / ainit))
        vtrana = np.sqrt((2.0 * mu) / rinit - (mu / atran))
        deltava = abs(vtrana - vinit)
        
        # Find delta v at point b
        vfinal = np.sqrt((2.0 * mu) / rfinal - (mu / afinal))
        vtranb = np.sqrt((2.0 * mu) / rfinal - (mu / atran))
        deltavb = abs(vfinal - vtranb)
        
        # Find transfer time of flight
        dttu = np.pi * np.sqrt((atran * atran * atran) / mu)
    
    return deltava, deltavb, dttu 