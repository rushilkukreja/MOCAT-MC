import numpy as np

def angl_vec(vec1, vec2):
    """
    Compute the angle between two vectors (vectorized version).
    
    Parameters:
    -----------
    vec1 : array-like
        First vector(s) - can be 1D or 2D array
    vec2 : array-like
        Second vector(s) - can be 1D or 2D array
    
    Returns:
    --------
    angle : float or array
        Angle(s) between vectors in radians
    """
    # Handle both single vectors and arrays of vectors
    if vec1.ndim == 1 and vec2.ndim == 1:
        # Single vector case
        cos_angle = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        return np.arccos(cos_angle)
    else:
        # Vectorized case
        # Normalize vectors
        vec1_norm = vec1 / np.linalg.norm(vec1, axis=0, keepdims=True)
        vec2_norm = vec2 / np.linalg.norm(vec2, axis=0, keepdims=True)
        
        # Compute dot products
        cos_angles = np.sum(vec1_norm * vec2_norm, axis=0)
        cos_angles = np.clip(cos_angles, -1.0, 1.0)
        return np.arccos(cos_angles) 