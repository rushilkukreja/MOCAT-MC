"""
Cross product of vectors
Python version of cross_vec.m
"""

import numpy as np

def cross_vec(a, b):
    """
    Compute cross product of input vectors
    
    Parameters:
    -----------
    a : array-like
        First vector(s), shape (n, 3)
    b : array-like
        Second vector(s), shape (n, 3)
        
    Returns:
    --------
    c : array-like
        Cross product, shape (n, 3)
    """
    
    a = np.asarray(a)
    b = np.asarray(b)
    
    c = np.cross(a, b, axis=1)
    
    return c 