import numpy as np

def ijk2lle(r, jd):
    """
    Converts a geocentric equatorial (ijk) position vector into latitude and longitude.
    r: ijk position vector (km)
    jd: Julian date (days from 4713 BC)
    Returns:
        latgc: geocentric latitude (rad)
        latgd: geodetic latitude (rad)
        lon: longitude (rad)
        hellp: height above the ellipsoid (km)
    """
    def mag(vec):
        return np.linalg.norm(vec)
    def dsign(x):
        return np.sign(x)
    def gstime(jd):
        return 0.0  # Placeholder
    def gd2gc(latgd):
        return latgd  # Placeholder
    twopi = 2.0 * np.pi
    small = 1e-8
    eesqrd = 0.006694385
    magr = mag(r)
    oneminuse2 = 1.0 - eesqrd
    temp = np.sqrt(r[0] ** 2 + r[1] ** 2)
    if abs(temp) < small:
        rtasc = dsign(r[2]) * np.pi * 0.5
    else:
        rtasc = np.arctan2(r[1], r[0])
    gst = gstime(jd)
    lon = rtasc - gst
    if abs(lon) >= np.pi:
        if lon < 0.0:
            lon = twopi + lon
        else:
            lon = lon - twopi
    decl = np.arcsin(r[2] / magr)
    latgc = decl
    deltalat = 100.0
    rsqrd = magr ** 2
    i = 1
    olddelta = deltalat
    while abs(olddelta - deltalat) >= small and i < 10:
        olddelta = deltalat
        rsite = np.sqrt(oneminuse2 / (1.0 - eesqrd * (np.cos(latgc)) ** 2))
        latgd = np.arctan(np.tan(latgc) / oneminuse2)
        temp2 = latgd - latgc
        sintemp = np.sin(temp2)
        hellp = np.sqrt(rsqrd - rsite * rsite * sintemp * sintemp) - rsite * np.cos(temp2)
        deltalat = np.arcsin(hellp * sintemp / magr)
        latgc = decl - deltalat
        i += 1
    if i >= 10:
        print('ijktolatlon did not converge')
    return latgc, latgd, lon, hellp 