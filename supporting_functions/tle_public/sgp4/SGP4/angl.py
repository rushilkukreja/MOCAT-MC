import numpy as np

def angl(vec1, vec2):
    """
    Compute the angle between two vectors.
    
    Parameters:
    -----------
    vec1 : array-like
        First vector
    vec2 : array-like
        Second vector
    
    Returns:
    --------
    angle : float
        Angle between vectors in radians
    """
    cos_angle = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    # Ensure cos_angle is within [-1, 1] to avoid numerical errors
    cos_angle = np.clip(cos_angle, -1.0, 1.0)
    return np.arccos(cos_angle) 