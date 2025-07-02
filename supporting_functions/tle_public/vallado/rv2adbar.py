import numpy as np

def rv2adbar(r, v):
    """
    Transforms a position and velocity vector into the adbarv elements - rtasc, decl, fpav, azimuth, position and velocity magnitude.
    """
    twopi = 2.0 * np.pi
    small = 1e-8
    def mag(vec):
        return np.linalg.norm(vec)
    rmag = mag(r)
    vmag = mag(v)
    temp = np.sqrt(r[0] ** 2 + r[1] ** 2)
    if temp < small:
        temp1 = np.sqrt(v[0] ** 2 + v[1] ** 2)
        if abs(temp1) > small:
            rtasc = np.arctan2(v[1], v[0])
        else:
            rtasc = 0.0
    else:
        rtasc = np.arctan2(r[1], r[0])
    decl = np.arcsin(r[2] / rmag)
    h = np.cross(r, v)
    hmag = mag(h)
    rdotv = np.dot(r, v)
    fpav = np.arctan2(hmag, rdotv)
    hcrossr = np.cross(h, r)
    az = np.arctan2(r[0] * hcrossr[1] - r[1] * hcrossr[0], hcrossr[2] * rmag)
    return rmag, vmag, rtasc, decl, fpav, az 