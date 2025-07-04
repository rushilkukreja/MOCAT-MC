import numpy as np

gh = None  # This should be set globally before calling igrf11syn

def igrf11syn(fyears, alt, nlat, elong):
    """
    Synthesize geomagnetic field values from IGRF11 coefficients.
    Parameters
    ----------
    fyears : float
        Date in fractional years (e.g., 2009.5)
    alt : float
        Altitude in km
    nlat : float
        Latitude (degrees, positive north)
    elong : float
        Longitude (degrees, positive east)
    Returns
    -------
    B : np.ndarray
        [B_North, B_East, B_Up] in nano Teslas
    """
    global gh
    isv = 0
    itype = 1
    colat = 90 - nlat
    cl = np.full(13, np.nan)
    sl = np.full(13, np.nan)
    x = 0.0
    y = 0.0
    z = 0.0
    if fyears < 1900 or fyears > 2020:
        raise ValueError('Date >=1900 & <=2020')
    if fyears > 2015:
        print('Warning: This version of IGRF intended for use only to 2015')
    if fyears < 2010:
        t = 0.2 * (fyears - 1900.0)
        ll = int(np.floor(t))
        one = ll
        t = t - one
        if fyears < 1995.0:
            nmx = 10
            nc = nmx * (nmx + 2)
            ll = nc * ll
            kmx = int((nmx + 1) * (nmx + 2) / 2)
        else:
            nmx = 13
            nc = nmx * (nmx + 2)
            ll = int(np.floor(0.2 * (fyears - 1995)))
            ll = 120 * 19 + nc * ll
            kmx = int((nmx + 1) * (nmx + 2) / 2)
        tc = 1 - t
        if isv == 1:
            tc = -0.2
            t = 0.2
    else:
        t = fyears - 2010
        tc = 1
        if isv == 1:
            t = 1
            tc = 0
        ll = 2865
        nmx = 13
        nc = nmx * (nmx + 2)
        kmx = int((nmx + 1) * (nmx + 2) / 2)
    r = alt
    one = colat * np.pi / 180.0
    ct = np.cos(one)
    st = np.sin(one)
    one = elong * np.pi / 180.0
    cl[0] = np.cos(one)
    sl[0] = np.sin(one)
    cd = 1.0
    sd = 0.0
    l = 1
    m = 1
    n = 0
    if itype == 1:
        a2 = 40680631.6
        b2 = 40408296.0
        one = a2 * st * st
        two = b2 * ct * ct
        three = one + two
        rho = np.sqrt(three)
        r = np.sqrt(alt * (alt + 2.0 * rho) + (a2 * one + b2 * two) / three)
        cd = (alt + rho) / r
        sd = (a2 - b2) / rho * ct * st / r
        one = ct
        ct = ct * cd - st * sd
        st = st * cd + one * sd
    ratio = 6371.2 / r
    rr = ratio * ratio
    p = np.full(kmx, np.nan)
    q = np.full(kmx, np.nan)
    p[0] = 1.0
    p[2] = st
    q[0] = 0.0
    q[2] = ct
    for k in range(1, kmx):
        if n < m:
            m = 0
            n = n + 1
            rr = rr * ratio
            fn = n
            gn = n - 1
        fm = m
        if m == n and k != 2:
            one = np.sqrt(1.0 - 0.5 / fm)
            j = k - n - 1
            p[k] = one * st * p[j]
            q[k] = one * (st * q[j] + ct * p[j])
            cl[m] = cl[m - 1] * cl[0] - sl[m - 1] * sl[0]
            sl[m] = sl[m - 1] * cl[0] + cl[m - 1] * sl[0]
        if m != n and k != 2:
            gmm = m * m
            one = np.sqrt(fn * fn - gmm)
            two = np.sqrt(gn * gn - gmm) / one
            three = (fn + gn) / one
            i = k - n
            j = i - n + 1
            p[k] = three * ct * p[i] - two * p[j]
            q[k] = three * (ct * q[i] - st * p[i]) - two * q[j]
        lm = ll + l
        one = (tc * gh[lm] + t * gh[lm + nc]) * rr
        if m != 0:
            two = (tc * gh[lm + 1] + t * gh[lm + nc + 1]) * rr
            three = one * cl[m] + two * sl[m]
            x = x + three * q[k]
            z = z - (fn + 1.0) * three * p[k]
            if st != 0:
                y = y + (one * sl[m] - two * cl[m]) * fm * p[k] / st
            else:
                y = y + (one * sl[m] - two * cl[m]) * q[k] * ct
            l = l + 2
        else:
            x = x + one * q[k]
            z = z - (fn + 1.0) * one * p[k]
            l = l + 1
        m = m + 1
    one = x
    x = x * cd + z * sd
    z = z * cd - one * sd
    B = np.array([x, y, z])
    return B 