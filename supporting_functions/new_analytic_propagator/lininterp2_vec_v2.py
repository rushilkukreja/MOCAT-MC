import numpy as np

def lininterp2_vec_v2(X, Y, V, x, y):
    """
    Vectorized 2D linear interpolation (v2), given set of X, Y, and V values, and an x, y query.
    Assumes X and Y values are in strictly increasing order.
    Extends values off the ends instead of giving NaN.
    """
    X = np.asarray(X).flatten()
    Y = np.asarray(Y).flatten()
    V = np.asarray(V)
    x = np.asarray(x).flatten()
    y = np.asarray(y).flatten()
    if X.shape[0] != V.shape[0] or Y.shape[0] != V.shape[1]:
        raise ValueError('[length(X), length(Y)] does not match size(V)')
    pindexx = np.searchsorted(X, x, side='right') - 1
    indexx = pindexx + 1
    indexx = np.clip(indexx, 0, len(X) - 1)
    pindexx = np.clip(pindexx, 0, len(X) - 1)
    slopex = (x - X[pindexx]) / (X[indexx] - X[pindexx])
    pindexy = np.searchsorted(Y, y, side='right') - 1
    indexy = pindexy + 1
    indexy = np.clip(indexy, 0, len(Y) - 1)
    pindexy = np.clip(pindexy, 0, len(Y) - 1)
    slopey = (y - Y[pindexy]) / (Y[indexy] - Y[pindexy])
    num_rows = V.shape[0]
    v = (V[pindexx, pindexy] * (1 - slopex) * (1 - slopey) +
         V[indexx, pindexy] * slopex * (1 - slopey) +
         V[pindexx, indexy] * (1 - slopex) * slopey +
         V[indexx, indexy] * slopex * slopey)
    return v 