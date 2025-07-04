import numpy as np

def dB20(A):
    """
    Compute 20*log10(A).
    
    Parameters:
    -----------
    A : array-like
        Input amplitude vector
    
    Returns:
    --------
    IdB : array-like
        dB values if A > 0, else NaN
    
    Notes:
    ------
    Chuck Rino
    Rino Consulting
    July 2010
    """
    IdB = np.full_like(A, np.nan)
    iOK = np.where(np.abs(A) > 0)[0]
    IdB[iOK] = 20 * np.log10(np.abs(A[iOK]))
    return IdB 