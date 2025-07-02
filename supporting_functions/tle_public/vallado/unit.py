import numpy as np

def unit(vec):
    """
    Calculates a unit vector given the original vector. If a zero vector is input, the vector is set to zero.
    """
    small = 1e-6
    magv = np.linalg.norm(vec)
    if magv > small:
        outvec = vec / magv
    else:
        outvec = np.zeros_like(vec)
    return outvec 