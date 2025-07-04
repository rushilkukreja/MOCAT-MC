import numpy as np

def boxcar_avg(v, nspan):
    """
    Compute M-point running average.
    
    Parameters:
    -----------
    v : array-like
        Input vector
    nspan : int
        Span size for averaging
    
    Returns:
    --------
    vbar : array-like
        Running average of input vector
    """
    npts = len(v)
    nmid = int(np.floor(nspan / 2)) + 1
    nupd = nmid - 1
    vbar = np.zeros_like(v)
    
    for m in range(npts):
        mspan = np.arange(max(0, m - nupd), min(m + nupd + 1, npts))
        ntot = len(mspan)
        vbar[m] = np.sum(v[mspan]) / ntot
    
    return vbar 