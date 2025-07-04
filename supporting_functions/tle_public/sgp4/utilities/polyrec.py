import numpy as np
from scipy.special import comb

def polyrec(Ps, MU):
    """
    Recover original polynomial coefficients from call to [Ps,S,MU]=polyfit(x,y,N).
    
    Parameters:
    -----------
    Ps : array-like
        Scaled polynomial coefficients
    MU : array-like
        Scaling parameters [mu1, mu2]
    
    Returns:
    --------
    P : array-like
        Original polynomial coefficients
    """
    N = len(Ps) - 1
    
    # Coefficients are stored in descending order of n
    PsN = np.zeros(N + 1)
    for in_idx in range(N + 1):
        n = N - in_idx
        PsN[in_idx] = Ps[in_idx] / MU[1]**n
    
    P = np.zeros(N + 1)
    P[0] = -PsN[0]
    SN = -1
    
    for in_idx in range(1, N + 1):  # Current index
        m = N - in_idx  # Current power [N-1:-1:0]
        P[in_idx] = 0
        S = -1
        
        for l in range(N - m + 1):
            S = S * SN
            P[in_idx] = P[in_idx] + S * PsN[l] * C(N - l + 1, m) * MU[0]**(N - l + 1 - m)
        
        P[in_idx] = (-1)**(N - m) * P[in_idx]
    
    return P

def C(n, m):
    """
    Binomial coefficient function.
    
    Parameters:
    -----------
    n : int
        Total number of items
    m : int
        Number of items to choose
    
    Returns:
    --------
    result : int
        Binomial coefficient C(n,m)
    """
    if m == 0:
        result = 1
    elif m == 1:
        result = n
    else:
        result = int(comb(n, m))
    
    return result 