import numpy as np

def lininterp1_vec(X, V, x):
    """
    Vectorized linear interpolation, given set of X and V values, and an x query.
    Assumes X values are in strictly increasing order.
    Extends values off the ends instead of giving NaN.
    """
    X = np.asarray(X).flatten()
    V = np.asarray(V).flatten()
    x = np.asarray(x).flatten()
    if X.shape[0] != V.shape[0]:
        raise ValueError('X and V sizes do not match')
    pindex = np.searchsorted(X, x, side='right') - 1
    index = np.searchsorted(X, x, side='left')
    # Handle out-of-bounds
    pindex = np.clip(pindex, 0, len(X) - 1)
    index = np.clip(index, 0, len(X) - 1)
    slope = np.zeros_like(x, dtype=float)
    mask = pindex != index
    Xp = X[pindex[mask]]
    slope[mask] = (x[mask] - Xp) / (X[index[mask]] - Xp)
    v = V[pindex] * (1 - slope) + V[index] * slope
    return v 