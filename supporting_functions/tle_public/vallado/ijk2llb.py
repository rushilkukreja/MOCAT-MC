import numpy as np

def ijk2llb(r):
    """
    Converts a geocentric equatorial (ijk) position vector into latitude and longitude.
    r: ijk position vector (km)
    Returns:
        latgc: geocentric latitude (rad)
        latgd: geodetic latitude (rad)
        lon: longitude (rad)
        hellp: height above the ellipsoid (km)
    """
    def gd2gc(latgd):
        return latgd  # Placeholder
    twopi = 2.0 * np.pi
    small = 1e-8
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
    a = 6378.1363
    b = np.sign(r[2]) * 6356.75160056
    atemp = 1.0 / (a * temp)
    e = (b * r[2] - a * a + b * b) * atemp
    f = (b * r[2] + a * a - b * b) * atemp
    third = 1.0 / 3.0
    p = 4.0 * third * (e * f + 1.0)
    q = 2.0 * (e * e - f * f)
    d = p * p * p + q * q
    if d > 0.0:
        nu = (np.sqrt(d) - q) ** third - (np.sqrt(d) + q) ** third
    else:
        sqrtp = np.sqrt(-p)
        nu = 2.0 * sqrtp * np.cos(third * np.arccos(q / (p * sqrtp)))
    g = 0.5 * (np.sqrt(e * e + nu) + e)
    t = np.sqrt(g * g + (f - nu * g) / (2.0 * g - e)) - g
    latgd = np.arctan(a * (1.0 - t * t) / (2.0 * b * t))
    hellp = (temp - a * t) * np.cos(latgd) + (r[2] - b) * np.sin(latgd)
    latgc = gd2gc(latgd)
    return latgc, latgd, lon, hellp 