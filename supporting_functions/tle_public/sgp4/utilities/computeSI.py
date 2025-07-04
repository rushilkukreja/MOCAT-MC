import numpy as np

def computeSI(I, nspan):
    """
    Compute symmetric boxcar average with reflected end corrections.
    
    Parameters:
    -----------
    I : array-like
        Input intensity array
    nspan : int
        Span size for averaging
    
    Returns:
    --------
    SI : array-like
        Scintillation index
    Ibar : array-like
        Averaged intensity
    """
    npts = len(I)
    nmid = int(np.floor(nspan / 2)) + 1
    nupd = nmid - 1
    Ibar = np.zeros_like(I)
    SI = np.zeros_like(I)
    
    for m in range(npts):
        mspan = np.arange(max(0, m - nupd), min(m + nupd + 1, npts))
        ntot = len(mspan)
        Ibar[m] = np.sum(I[mspan]) / ntot
        SI[m] = np.sqrt(np.sum(I[mspan]**2) / (ntot * Ibar[m]**2) - 1)
    
    return SI, Ibar 