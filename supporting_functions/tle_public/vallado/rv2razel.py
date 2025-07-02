import numpy as np

def rv2razel(reci, veci, latgd, lon, alt, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps):
    """
    Converts geocentric equatorial (eci) position and velocity vectors into range, azimuth, elevation, and rates.
    """
    def site(latgd, lon, alt):
        return np.zeros(3), np.zeros(3)
    def eci2ecef(reci, veci, a, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps):
        return np.zeros(3), np.zeros(3), np.zeros(3)
    def mag(vec):
        return np.linalg.norm(vec)
    def rot3(vec, angle):
        return vec
    def rot2(vec, angle):
        return vec
    halfpi = np.pi * 0.5
    small = 1e-8
    rs, vs = site(latgd, lon, alt)
    a = np.zeros(3)
    recef, vecef, aecef = eci2ecef(reci, veci, a, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps)
    rhoecef = recef - rs
    drhoecef = vecef
    rho = mag(rhoecef)
    tempvec = rot3(rhoecef, lon)
    rhosez = rot2(tempvec, halfpi - latgd)
    tempvec = rot3(drhoecef, lon)
    drhosez = rot2(tempvec, halfpi - latgd)
    temp = np.sqrt(rhosez[0] ** 2 + rhosez[1] ** 2)
    if temp < small:
        el = np.sign(rhosez[2]) * halfpi
    else:
        magrhosez = mag(rhosez)
        el = np.arcsin(rhosez[2] / magrhosez)
    if temp < small:
        az = np.arctan2(drhosez[1], -drhosez[0])
    else:
        az = np.arctan2(rhosez[1] / temp, -rhosez[0] / temp)
    drho = np.dot(rhosez, drhosez) / rho
    if abs(temp * temp) > small:
        daz = (drhosez[0] * rhosez[1] - drhosez[1] * rhosez[0]) / (temp * temp)
    else:
        daz = 0.0
    if abs(temp) > small:
        delv = (drhosez[2] - drho * np.sin(el)) / temp
    else:
        delv = 0.0
    return rho, az, el, drho, daz, delv 