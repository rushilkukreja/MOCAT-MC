import numpy as np

def site(latgd, lon, alt):
    """
    Finds the position and velocity vectors for a site in the geocentric equatorial (ecef) coordinate system.
    """
    # Placeholder constants
    re = 6378.137
    eccearthsqrd = 0.006694385
    sinlat = np.sin(latgd)
    cearth = re / np.sqrt(1.0 - (eccearthsqrd * sinlat * sinlat))
    rdel = (cearth + alt) * np.cos(latgd)
    rk = ((1.0 - eccearthsqrd) * cearth + alt) * sinlat
    rs = np.array([rdel * np.cos(lon), rdel * np.sin(lon), rk])
    vs = np.zeros(3)
    return rs, vs 