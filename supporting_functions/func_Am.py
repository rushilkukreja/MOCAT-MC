"""
Area-to-mass ratio calculation function
Based on NASA's new breakup model of evolve 4.0
"""

import numpy as np

def func_Am(d, ObjClass):
    """
    Calculate area-to-mass ratio for fragments
    
    Parameters:
    -----------
    d : array-like
        Diameter in meters
    ObjClass : int or array-like
        Object class (1=Satellite, 2=Debris, 5=Rocket Body, etc.)
        
    Returns:
    --------
    Am : array-like
        Area-to-mass ratio in m²/kg
    """
    
    numObj = len(d)
    logds = np.log10(d)  # d in meters
    amsms = np.full((numObj, 5), np.nan)  # store alpha,mu1,sig1,mu2,sig2
    
    # Check if ObjClass is scalar or array
    if np.isscalar(ObjClass):
        ObjClass = np.full(numObj, ObjClass)
    
    # Rocket-body related objects (class 5-8)
    rocket_mask = (ObjClass > 4.5) & (ObjClass < 8.5)
    
    for ind in range(numObj):
        logd = logds[ind]
        
        if rocket_mask[ind]:
            # Rocket body parameters
            # alpha
            if logd <= -1.4:
                alpha = 1
            elif -1.4 < logd < 0:
                alpha = 1 - 0.3571 * (logd + 1.4)
            else:  # >= 0
                alpha = 0.5
            
            # mu1
            if logd <= -0.5:
                mu1 = -0.45
            elif -0.5 < logd < 0:
                mu1 = -0.45 - 0.9 * (logd + 0.5)
            else:  # >= 0
                mu1 = -0.9
            
            # sigma1
            sigma1 = 0.55
            
            # mu2
            mu2 = -0.9
            
            # sigma2
            if logd <= -1.0:
                sigma2 = 0.28
            elif -1 < logd < 0.1:
                sigma2 = 0.28 - 0.1636 * (logd + 1)
            else:  # >= 0.1
                sigma2 = 0.1
                
        else:
            # Satellite/Debris parameters
            # alpha
            if logd <= -1.95:
                alpha = 1
            elif -1.95 < logd < 0.55:
                alpha = 1 - 0.4 * (logd + 1.95)
            else:  # >= 0.55
                alpha = 0.0
            
            # mu1
            if logd <= -0.55:
                mu1 = -0.3
            elif -0.55 < logd < 0.55:
                mu1 = -0.3 - 0.4 * (logd + 0.55)
            else:  # >= 0.55
                mu1 = -0.7
            
            # sigma1
            sigma1 = 0.4
            
            # mu2
            mu2 = -0.7
            
            # sigma2
            if logd <= -1.1:
                sigma2 = 0.28
            elif -1.1 < logd < 0.1:
                sigma2 = 0.28 - 0.1636 * (logd + 1.1)
            else:  # >= 0.1
                sigma2 = 0.1
        
        amsms[ind, :] = [alpha, mu1, sigma1, mu2, sigma2]
    
    # Calculate log10(Am) using the two-component lognormal distribution
    log10_Am = np.full(numObj, np.nan)
    
    for ind in range(numObj):
        alpha, mu1, sigma1, mu2, sigma2 = amsms[ind, :]
        
        # Generate random number
        rand_val = np.random.random()
        
        if rand_val < alpha:
            # First component
            log10_Am[ind] = np.random.normal(mu1, sigma1)
        else:
            # Second component
            log10_Am[ind] = np.random.normal(mu2, sigma2)
    
    # Convert to Am (m²/kg)
    Am = 10**log10_Am
    
    return Am 