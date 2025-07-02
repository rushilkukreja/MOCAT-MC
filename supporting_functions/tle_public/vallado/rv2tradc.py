import numpy as np

def rv2tradc(reci, veci, latgd, lon, alt, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps):
    """
    Converts geocentric equatorial (eci) position and velocity vectors into range, topocentric right ascension, declination, and rates.
    """
    def site(latgd, lon, alt):
        return np.zeros(3), np.zeros(3)
    def ecef2eci(rs, vs, a, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps):
        return np.zeros(3), np.zeros(3), np.zeros(3)
    def mag(vec):
        return np.linalg.norm(vec)
    halfpi = np.pi * 0.5
    small = 1e-8
    rs, vs = site(latgd, lon, alt)
    a = np.zeros(3)
    rseci, vseci, aeci = ecef2eci(rs, vs, a, ttt, jdut1, lod, xp, yp, terms, ddpsi, ddeps)
    rhoeci = reci - rseci
    drhoeci = veci - vseci
    rho = mag(rhoeci)
    temp = np.sqrt(rhoeci[0] ** 2 + rhoeci[1] ** 2)
    if temp < small:
        trtasc = np.arctan2(drhoeci[1], drhoeci[0])
    else:
        trtasc = np.arctan2(rhoeci[1], rhoeci[0])
    if temp < small:
        tdecl = np.sign(rhoeci[2]) * halfpi
    else:
        magrhoeci = mag(rhoeci)
        tdecl = np.arcsin(rhoeci[2] / magrhoeci)
    temp1 = -rhoeci[1] * rhoeci[1] - rhoeci[0] * rhoeci[0]
    drho = np.dot(rhoeci, drhoeci) / rho
    if abs(temp1) > small:
        dtrtasc = (drhoeci[0] * rhoeci[1] - drhoeci[1] * rhoeci[0]) / temp1
    else:
        dtrtasc = 0.0
    if abs(temp) > small:
        dtdecl = (drhoeci[2] - drho * np.sin(tdecl)) / temp
    else:
        dtdecl = 0.0
    return rho, trtasc, tdecl, drho, dtrtasc, dtdecl 