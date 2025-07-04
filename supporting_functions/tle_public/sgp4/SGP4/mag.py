import numpy as np

def mag(vector):
    """
    Compute the magnitude of a vector.
    
    Parameters:
    -----------
    vector : array-like
        Input vector (1D, 2D, or 3D)
    
    Returns:
    --------
    magnitude : float
        Magnitude of the vector
    """
    return np.linalg.norm(vector) 