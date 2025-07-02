import numpy as np

def rv2radec(r, v):
    """
    Converts the right ascension and declination values with position and velocity vectors of a satellite.
    """
    small = 1e-8
    def mag(vec):
        return np.linalg.norm(vec)
    rr = mag(r)
    temp = np.sqrt(r[0] ** 2 + r[1] ** 2)
    if temp < small:
        rtasc = np.arctan2(v[1], v[0])
    else:
        rtasc = np.arctan2(r[1], r[0])
    decl = np.arcsin(r[2] / rr)
    temp1 = -r[1] * r[1] - r[0] * r[0]
    drr = np.dot(r, v) / rr
    if abs(temp1) > small:
        drtasc = (v[0] * r[1] - v[1] * r[0]) / temp1
    else:
        drtasc = 0.0
    if abs(temp) > small:
        ddecl = (v[2] - drr * np.sin(decl)) / temp
    else:
        ddecl = 0.0
    return rr, rtasc, decl, drr, drtasc, ddecl 