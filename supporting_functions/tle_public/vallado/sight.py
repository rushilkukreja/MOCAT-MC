import numpy as np

def sight(r1, r2, whichkind='e'):
    """
    Determines if there is line-of-sight between two satellites.
    r1, r2: position vectors (km)
    whichkind: 's' for spherical, 'e' for ellipsoidal earth (default)
    Returns: 'yes' or 'no '
    """
    eesqrd = 0.006694385
    re = 6378.137
    tr1 = np.array(r1, dtype=float)
    tr2 = np.array(r2, dtype=float)
    magr1 = np.linalg.norm(tr1)
    magr2 = np.linalg.norm(tr2)
    if whichkind == 'e':
        temp = 1.0 / np.sqrt(1.0 - eesqrd)
    else:
        temp = 1.0
    tr1[2] = tr1[2] * temp
    tr2[2] = tr2[2] * temp
    bsqrd = magr2 * magr2
    asqrd = magr1 * magr1
    adotb = np.dot(tr1, tr2)
    if abs(asqrd + bsqrd - 2.0 * adotb) < 0.0001:
        tmin = 0.0
    else:
        tmin = (asqrd - adotb) / (asqrd + bsqrd - 2.0 * adotb)
    if (tmin < 0.0) or (tmin > 1.0):
        los = 'yes'
    else:
        distsqrd = ((1.0 - tmin) * asqrd + adotb * tmin) / re ** 2
        if distsqrd > 1.0:
            los = 'yes'
        else:
            los = 'no '
    return los 