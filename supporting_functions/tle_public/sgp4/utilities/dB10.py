import numpy as np

def dB10(I):
    """
    Compute 10*log10(I).
    
    Parameters:
    -----------
    I : array-like
        Input intensity vector
    
    Returns:
    --------
    IdB : array-like
        dB values if I > 0, else NaN
    
    Notes:
    ------
    Chuck Rino
    Rino Consulting
    July 2010
    """
    IdB = np.full_like(I, np.nan)
    iOK = np.where(np.abs(I) > 0)[0]
    IdB[iOK] = 10 * np.log10(np.abs(I[iOK]))
    return IdB 