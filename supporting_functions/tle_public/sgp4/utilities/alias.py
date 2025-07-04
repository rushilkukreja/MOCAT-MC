import numpy as np

def alias(f, fNyq):
    """
    Compute aliased frequencies.
    
    Parameters:
    -----------
    f : array-like
        Input frequency array
    fNyq : float
        Nyquist frequency
    
    Returns:
    --------
    falias : array-like
        Aliased frequency array
    m : int
        Aliasing parameter
    """
    nf = len(f)
    falias = np.zeros(nf)
    
    for n in range(nf):
        err = 1e12
        m = 0
        while err > fNyq / 2:
            err = abs(f[n] - m * fNyq)
            m += 1
        falias[n] = f[n] - (m - 1) * fNyq
    
    return falias, m 