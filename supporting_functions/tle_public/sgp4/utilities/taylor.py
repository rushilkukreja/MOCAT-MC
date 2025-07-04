import numpy as np

def taylor(nx, slldb):
    """
    Generate Taylor window weights.
    
    Parameters:
    -----------
    nx : int
        Number of data samples
    slldb : float
        Sidelobe suppression in dB
    
    Returns:
    --------
    weight : array-like
        Column vector of real weights
    
    Notes:
    ------
    Chris Wilson 20 August 2001
    """
    weight = np.ones(nx)  # default weights
    x = np.linspace(-(nx-1)/2, (nx-1)/2, nx) / nx  # scaled positions of data samples
    a = np.arccosh(10**(abs(slldb)/20)) / np.pi  # scale parameter
    nbar = round(2*a**2 + 0.5)  # number of terms in sum
    
    if nbar < 2:
        return weight
    
    sigmasq = nbar**2 / (a**2 + (nbar - 0.5)**2)
    
    # NOTE: vectorizing causes errors for extremely large nx!
    f = np.zeros(nbar - 1)
    for m in range(nbar - 1):
        f[m] = (-1)**(m + 1) / 2
        for n in range(nbar - 1):
            f[m] = f[m] * (1 - m**2 / sigmasq / (a**2 + (n - 0.5)**2))
            if m != n:
                f[m] = f[m] / (1 - (m/n)**2)
        weight = weight + 2 * f[m] * np.cos(2 * np.pi * m * x)
    
    fsum = 1 + 2 * np.sum(f)
    weight = weight / fsum
    
    return weight 