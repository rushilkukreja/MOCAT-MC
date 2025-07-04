import numpy as np

def position2index(ipos, n1):
    """
    Invert ipos=(i2-1)*n1+i1.
    
    Parameters:
    -----------
    ipos : array-like
        Position indices
    n1 : int
        First dimension size
    
    Returns:
    --------
    i1 : array-like
        First dimension indices
    i2 : array-like
        Second dimension indices
    """
    nn = len(ipos)
    i1 = np.zeros(nn)
    i2 = np.zeros(nn)
    
    for n in range(nn):
        i1[n] = ipos[n] % n1
        if i1[n] == 0:
            i1[n] = n1
        i2[n] = (ipos[n] - i1[n]) / n1 + 1
    
    return i1, i2 