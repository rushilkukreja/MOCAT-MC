import numpy as np

def nicefftnum(n):
    """
    Find a highly composite even number >= n.
    
    Parameters:
    -----------
    n : int
        Input number
    
    Returns:
    --------
    nfft : int
        Highly composite even number >= n
    
    Notes:
    ------
    C. Wilson 10 October 1999
    """
    testvalues = [1, 3, 5, 9, 15, 25, 27]
    nt = 2.0 ** np.maximum(1, np.ceil(np.log2(n / np.array(testvalues)))) * np.array(testvalues)
    nfft = int(np.min(nt))
    return nfft 