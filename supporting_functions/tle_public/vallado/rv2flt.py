import numpy as np

def rv2flt(r, v, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps):
    """
    Transforms a position and velocity vector into the flight elements - latgc, lon, fpa, az, position and velocity magnitude.
    """
    def mag(vec):
        return np.linalg.norm(vec)
    def eci2ecef(r, v, a, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps):
        return np.zeros(3), np.zeros(3), np.zeros(3)
    twopi = 2.0 * np.pi
    small = 1e-8
    magr = mag(r)
    magv = mag(v)
    a = np.zeros(3)
    recef, vecef, aecef = eci2ecef(r, v, a, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps)
    temp = np.sqrt(recef[0] ** 2 + recef[1] ** 2)
    if temp < small:
        lon = np.arctan2(vecef[1], vecef[0])
    else:
        lon = np.arctan2(recef[1], recef[0])
    latgc = np.arcsin(recef[2] / magr)
    temp2 = np.sqrt(r[0] ** 2 + r[1] ** 2)
    if temp2 < small:
        rtasc = np.arctan2(v[1], v[0])
    else:
        rtasc = np.arctan2(r[1], r[0])
    decl = np.arcsin(r[2] / magr)
    h = np.cross(r, v)
    hmag = mag(h)
    rdotv = np.dot(r, v)
    fpav = np.arctan2(hmag, rdotv)
    fpa = np.pi * 0.5 - fpav
    hcrossr = np.cross(h, r)
    az = np.arctan2(r[0] * hcrossr[1] - r[1] * hcrossr[0], hcrossr[2] * magr)
    return magr, magv, latgc, lon, fpa, az 