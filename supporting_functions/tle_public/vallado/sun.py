import numpy as np

def sun(jd):
    """
    Calculates the geocentric equatorial position vector of the sun given the Julian date.
    Returns: rsun (AU), rtasc (rad), decl (rad)
    """
    twopi = 2.0 * np.pi
    deg2rad = np.pi / 180.0
    tut1 = (jd - 2451545.0) / 36525.0
    meanlong = 280.460 + 36000.77 * tut1
    meanlong = np.remainder(meanlong, 360.0)
    ttdb = tut1
    meananomaly = 357.5277233 + 35999.05034 * ttdb
    meananomaly = np.remainder(meananomaly * deg2rad, twopi)
    if meananomaly < 0.0:
        meananomaly = twopi + meananomaly
    eclplong = meanlong + 1.914666471 * np.sin(meananomaly) + 0.019994643 * np.sin(2.0 * meananomaly)
    eclplong = np.remainder(eclplong, 360.0)
    obliquity = 23.439291 - 0.0130042 * ttdb
    eclplong = eclplong * deg2rad
    obliquity = obliquity * deg2rad
    magr = 1.000140612 - 0.016708617 * np.cos(meananomaly) - 0.000139589 * np.cos(2.0 * meananomaly)
    rsun = np.zeros(3)
    rsun[0] = magr * np.cos(eclplong)
    rsun[1] = magr * np.cos(obliquity) * np.sin(eclplong)
    rsun[2] = magr * np.sin(obliquity) * np.sin(eclplong)
    rtasc = np.arctan(np.cos(obliquity) * np.tan(eclplong))
    if eclplong < 0.0:
        eclplong = eclplong + twopi
    if abs(eclplong - rtasc) > np.pi * 0.5:
        rtasc = rtasc + 0.5 * np.pi * np.round((eclplong - rtasc) / (0.5 * np.pi))
    decl = np.arcsin(np.sin(obliquity) * np.sin(eclplong))
    return rsun, rtasc, decl 