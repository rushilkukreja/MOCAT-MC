import numpy as np

def ijk2ll(r):
    """
    Converts a geocentric equatorial position vector into latitude and longitude.
    r: ECEF position vector (km)
    Returns:
        latgc: geocentric latitude (rad)
        latgd: geodetic latitude (rad)
        lon: longitude (rad)
        hellp: height above the ellipsoid (km)
    """
    def mag(vec):
        return np.linalg.norm(vec)
    def gd2gc(latgd):
        return latgd  # Placeholder
    twopi = 2.0 * np.pi
    small = 1e-8
    re = 6378.137
    eesqrd = 0.006694385
    magr = mag(r)
    temp = np.sqrt(r[0] ** 2 + r[1] ** 2)
    if abs(temp) < small:
        rtasc = np.sign(r[2]) * np.pi * 0.5
    else:
        rtasc = np.arctan2(r[1], r[0])
    lon = rtasc
    if abs(lon) >= np.pi:
        if lon < 0.0:
            lon = twopi + lon
        else:
            lon = lon - twopi
    decl = np.arcsin(r[2] / magr)
    latgd = decl
    i = 1
    olddelta = latgd + 10.0
    while abs(olddelta - latgd) >= small and i < 10:
        olddelta = latgd
        sintemp = np.sin(latgd)
        c = re / (np.sqrt(1.0 - eesqrd * sintemp * sintemp))
        latgd = np.arctan((r[2] + c * eesqrd * sintemp) / temp)
        i += 1
    if (np.pi * 0.5 - abs(latgd)) > np.pi / 180.0:
        hellp = (temp / np.cos(latgd)) - c
    else:
        s = c * (1.0 - eesqrd)
        hellp = r[2] / np.sin(latgd) - s
    latgc = gd2gc(latgd)
    return latgc, latgd, lon, hellp 