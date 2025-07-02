"""
Cube method for collision detection v3
Python version of cube_vec_v3.m
"""

import numpy as np
import pandas as pd
from itertools import combinations

def cube_vec_v3(X, CUBE_RES, collision_alt_limit):
    """
    Cube method for collision detection - only consider RSO below collision_alt_limit
    
    Parameters:
    -----------
    X : array-like
        Position vectors, shape (n_objects, 3)
    CUBE_RES : float
        Cube resolution [km]
    collision_alt_limit : float
        Altitude limit for collision consideration [km]
        
    Returns:
    --------
    res : list
        List of collision pairs, each element contains indices of objects in same cube
    """
    
    # Convert to numpy array if needed
    X = np.asarray(X)
    
    # Only consider RSO below collision_alt_limit for collision
    idx_invalid = np.any(np.abs(X) > collision_alt_limit, axis=1)
    X[idx_invalid, :] = np.nan
    
    # Discretize positions
    X_dis = np.floor(X[:, :3] / CUBE_RES)
    
    # Shift origin such that X_dis is always positive
    shift_lim = np.max(np.abs(X_dis)) + 10
    X_dis = X_dis + shift_lim
    shift_lim2 = 2 * shift_lim
    
    # Create unique index for each cube
    X_idx = X_dis[:, 0] * (shift_lim2 * shift_lim2) + X_dis[:, 1] * shift_lim2 + X_dis[:, 2]
    
    # Find unique indices and duplicates
    unique_idx, unique_indices = np.unique(X_idx, return_index=True)
    duplicate_mask = np.isin(X_idx, X_idx[np.setdiff1d(np.arange(len(X_idx)), unique_indices)])
    duplicates = X_idx[duplicate_mask]
    duplicate_idx = np.where(duplicate_mask)[0]
    
    # Group duplicates
    if len(duplicates) > 0:
        # Use pandas for grouping (similar to splitapply in MATLAB)
        df = pd.DataFrame({'idx': duplicate_idx, 'val': duplicates})
        groups = df.groupby('val')['idx'].apply(list).tolist()
        
        # Generate collision pairs for each group
        res = []
        for group in groups:
            if len(group) > 1:
                # Generate all pairs of objects in the same cube
                pairs = list(combinations(group, 2))
                res.extend(pairs)
    else:
        res = []
    
    return res 