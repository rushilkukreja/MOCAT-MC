import numpy as np

def freqs1(nsamp, fspan, iout):
    """
    Generate DFT frequency vector.
    
    Parameters:
    -----------
    nsamp : int
        Number of samples
    fspan : float
        Frequency span (2*fNyq=1/dt)
    iout : int
        0 => natural order (-fNyq:fNyq-df)
        1 => fft order ([0:fNyq,-fNyq:-df])
    
    Returns:
    --------
    f : array-like
        Frequency vector
    
    Notes:
    ------
    Chuck Rino
    Rino Consulting
    July 2010
    """
    if 2 * (nsamp // 2) == nsamp:
        # nsamp is even
        ff = (np.arange(nsamp) / nsamp - 1/2) * fspan
        if iout == 1:
            f = np.zeros(nsamp)
            f[:nsamp//2] = ff[nsamp//2:]
            f[nsamp//2:] = ff[:nsamp//2]
        else:
            f = ff
    else:
        # nsamp is odd
        ff = (np.arange(nsamp) - (nsamp - 1) / 2) * fspan / nsamp
        if iout == 1:
            f = np.zeros(nsamp)
            f[:(nsamp-1)//2+1] = ff[(nsamp-1)//2:]
            f[(nsamp-1)//2+1:] = ff[:(nsamp-1)//2]
        else:
            f = ff
    
    return f 