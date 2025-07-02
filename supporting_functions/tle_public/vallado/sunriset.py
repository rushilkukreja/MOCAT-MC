import numpy as np

def sunriset(jd, latgd, lon, whichkind):
    """
    Finds the universal time for sunrise and sunset given the day and site location.
    Returns: utsunrise, utsunset, error
    """
    twopi = 2.0 * np.pi
    rad2deg = 180.0 / np.pi
    deg2rad = np.pi / 180.0
    # Placeholder for invjday and jday
    def invjday(jd):
        return 2000, 1, 1, 0, 0, 0.0
    def jday(year, month, day, hr, minute, sec):
        return 2451545.0
    # -------------- make sure lon is within +- 180 deg -----------
    if lon > np.pi:
        lon = lon - twopi
    if lon < -np.pi:
        lon = lon + twopi
    if whichkind == 's':
        sunangle = (90.0 + 50.0 / 60.0) * deg2rad
    elif whichkind == 'c':
        sunangle = 96.0 * deg2rad
    elif whichkind == 'n':
        sunangle = 102.0 * deg2rad
    elif whichkind == 'a':
        sunangle = 108.0 * deg2rad
    else:
        sunangle = 90.0 * deg2rad
    year, month, day, hr, minute, sec = invjday(jd)
    utsunrise = utsunset = error = None
    for opt in [1, 2]:
        error = 'ok'
        if opt == 1:
            jdtemp = jday(year, month, day, 6, 0, 0.0)
        else:
            jdtemp = jday(year, month, day, 18, 0, 0.0)
        jdtemp = jdtemp - lon * rad2deg / 15.0 / 24.0
        tut1 = (jdtemp - 2451545.0) / 36525.0
        meanlonsun = 280.4606184 + 36000.77005361 * tut1
        meananomalysun = 357.5277233 + 35999.05034 * tut1
        meananomalysun = np.remainder(meananomalysun * deg2rad, twopi)
        if meananomalysun < 0.0:
            meananomalysun = meananomalysun + twopi
        lonecliptic = meanlonsun + 1.914666471 * np.sin(meananomalysun) + 0.019994643 * np.sin(2.0 * meananomalysun)
        lonecliptic = np.remainder(lonecliptic * deg2rad, twopi)
        if lonecliptic < 0.0:
            lonecliptic = lonecliptic + twopi
        obliquity = 23.439291 - 0.0130042 * tut1
        obliquity = obliquity * deg2rad
        ra = np.arctan(np.cos(obliquity) * np.tan(lonecliptic))
        decl = np.arcsin(np.sin(obliquity) * np.sin(lonecliptic))
        if ra < 0.0:
            ra = ra + twopi
        if (lonecliptic > np.pi) and (ra < np.pi):
            ra = ra + np.pi
        if (lonecliptic < np.pi) and (ra > np.pi):
            ra = ra - np.pi
        lha = (np.cos(sunangle) - np.sin(decl) * np.sin(latgd)) / (np.cos(decl) * np.cos(latgd))
        if abs(lha) <= 1.0:
            lha = np.arccos(lha)
        else:
            error = 'not ok'
        if error == 'ok':
            if opt == 1:
                lha = twopi - lha
            gst = 1.75336855923327 + 628.331970688841 * tut1 + 6.77071394490334e-06 * tut1 * tut1 - 4.50876723431868e-10 * tut1 * tut1 * tut1
            gst = np.remainder(gst, twopi)
            if gst < 0.0:
                gst = gst + twopi
            uttemp = lha + ra - gst
            uttemp = uttemp * rad2deg / 15.0
            uttemp = np.remainder(uttemp, 24.0)
            if uttemp < 0.0:
                uttemp = uttemp + 24.0
                error = 'day before'
            if uttemp > 24.0:
                uttemp = uttemp - 24.0
                error = 'day after'
        else:
            uttemp = 99.99
        if opt == 1:
            utsunrise = uttemp
        else:
            utsunset = uttemp
    return utsunrise, utsunset, error 