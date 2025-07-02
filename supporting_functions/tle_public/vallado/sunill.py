import numpy as np

def sunill(jd, lat, lon, sunaz=None, sunel=None):
    """
    Calculates the illumination due to the sun.
    """
    deg2rad = 0.01745329251994
    # Placeholder for sun and lstime
    def sun(jd):
        return np.zeros(3), 0.0, 0.0
    def lstime(lon, jd):
        return 0.0, 0.0
    rsun, srtasc, sdecl = sun(jd)
    lst, gst = lstime(lon, jd)
    lha = lst - srtasc
    sunel = np.arcsin(np.sin(sdecl) * np.sin(lat) + np.cos(sdecl) * np.cos(lat) * np.cos(lha))
    sinv = -np.sin(lha) * np.cos(sdecl) * np.cos(lat) / (np.cos(sunel) * np.cos(lat))
    cosv = (np.sin(sdecl) - np.sin(sunel) * np.sin(lat)) / (np.cos(sunel) * np.cos(lat))
    sunaz = np.arctan2(sinv, cosv)
    sunel = sunel / deg2rad
    if sunel > -18.01:
        x = sunel / 90.0
        if sunel >= 20:
            l0, l1, l2, l3 = 3.74, 3.97, -4.07, 1.47
        elif 5.0 <= sunel < 20.0:
            l0, l1, l2, l3 = 3.05, 13.28, -45.98, 64.33
        elif -0.8 <= sunel < 5.0:
            l0, l1, l2, l3 = 2.88, 22.26, -207.64, 1034.30
        elif -5.0 <= sunel < -0.8:
            l0, l1, l2, l3 = 2.88, 21.81, -258.11, -858.36
        elif -12.0 <= sunel < -5.0:
            l0, l1, l2, l3 = 2.70, 12.17, -431.69, -1899.83
        elif -18.0 <= sunel < -12.0:
            l0, l1, l2, l3 = 13.84, 262.72, 1447.42, 2797.93
        else:
            l0, l1, l2, l3 = 0.0, 0.0, 0.0, 0.0
        l1 = l0 + l1 * x + l2 * x * x + l3 * x * x * x
        sunillum = 10.0 ** l1
        if (sunillum < -1e36) or (sunillum > 999.999):
            sunillum = 0.0
    else:
        sunillum = 0.0
    return sunillum 