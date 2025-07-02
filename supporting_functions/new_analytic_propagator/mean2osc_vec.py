import numpy as np

def mean2osc_vec(oemean, param):
    """
    Convert mean classical orbital elements to osculating classical orbital elements (vectorized).
    oemean: ndarray, shape (N,6)
    param: object with required attributes
    Returns:
        oeosc: ndarray, shape (N,6)
    """
    pi2 = 2.0 * np.pi
    # compute j2 effect on orbital elements
    doe = delm(oemean, param)
    oeosc = oemean + doe
    oeosc[:, 2:6] = np.mod(oeosc[:, 2:6] + pi2, pi2)
    return oeosc

def delm(x, param):
    mu = param.mu
    req = param.req
    j2 = param.j2
    pi2 = 2.0 * np.pi
    a = x[:, 0]
    e = x[:, 1]
    ai = x[:, 2]
    an = x[:, 3]
    w = x[:, 4]
    am = x[:, 5]
    f = anomly(2, am, e)
    f = np.mod(f + pi2, pi2)
    am = np.mod(am + pi2, pi2)
    si = np.sin(ai)
    ci = np.cos(ai)
    ti = si / ci
    si2 = si * si
    ci2 = ci * ci
    sf = np.sin(f)
    cf = np.cos(f)
    s2f = np.sin(2.0 * f)
    u = f + w
    e2 = e * e
    esf = e * sf
    d1 = 1.0 - e2
    d2 = np.sqrt(d1)
    d3 = e * cf
    d4 = 1.0 + d3
    d42 = d4 * d4
    d5 = 1.0 + d2
    d6 = (3.0 * ci2 - 1.0) / d5
    p = a * d1
    d7 = np.sqrt(mu / p)
    r = p / d4
    rdot = d7 * esf
    twou = 2.0 * u
    twow = 2.0 * w
    s2u = np.sin(twou)
    c2u = np.cos(twou)
    sf2w = np.sin(f + twow)
    d8 = 3.0 * f + twow
    s3f2w = np.sin(d8)
    cf2w = np.cos(f + twow)
    c3f2w = np.cos(d8)
    q1 = j2 * (req / p)**2
    di = 0.75 * q1 * si * ci * (c2u + e * cf2w + e / 3.0 * c3f2w)
    dp = 2.0 * p * ti * di
    dummy1 = f - am + esf - 0.5 * s2u - 0.5 * e * sf2w - e * s3f2w / 6.0
    dn = -1.5 * q1 * ci * dummy1
    dr = -0.25 * p * q1 * ((3.0 * ci2 - 1.0) * (2.0 * d2 / d4 + d3 / d5 + 1.0) - si2 * c2u)
    drdot = 0.25 * d7 * q1 * (d6 * esf * (d2 * d5 + d42) - 2.0 * si2 * d42 * s2u)
    du = -0.125 * q1 * (6.0 * (1.0 - 5.0 * ci2) * (f - am) + 4.0 * esf * ((1.0 - 6.0 * ci2) - d6) - d6 * e2 * s2f + 2.0 * (5.0 * ci2 - 2.0) * e * sf2w + (7.0 * ci2 - 1.0) * s2u + 2.0 * ci2 * e * s3f2w)
    pnw = p + dp
    ainw = ai + di
    annw = an + dn
    rnw = r + dr
    rdotnw = rdot + drdot
    unw = u + du
    aa = pnw / rnw - 1.0
    bb = np.sqrt(pnw / mu) * rdotnw
    enw2 = aa * aa + bb * bb
    enw = np.sqrt(enw2)
    xfnw = np.arctan2(bb, aa)
    anw = pnw / (1.0 - enw2)
    wnw = unw - xfnw
    amnw = anomly(5, xfnw, enw)
    dx = np.zeros((a.size, 6))
    dx[:, 0] = anw - a
    dx[:, 1] = enw - e
    dx[:, 2] = ainw - ai
    dx[:, 3] = annw - an
    dx[:, 4] = wnw - w
    dx[:, 5] = amnw - am
    return dx

def anomly(nflg, ain, e):
    # orbital anomaly function
    if nflg in [1, 2]:
        am = ain
    if nflg in [3, 4]:
        ea = ain
    if nflg in [5, 6]:
        f = ain
    if nflg in [1, 2]:
        ea = kepler1(am, e)[0]
    if nflg in [2, 4]:
        f = 2.0 * np.arctan(np.sqrt((1.0 + e) / (1.0 - e)) * np.tan(ea / 2.0))
    if nflg in [5, 6]:
        ea = 2.0 * np.arctan(np.sqrt((1.0 - e) / (1.0 + e)) * np.tan(f / 2.0))
    if nflg in [5, 3]:
        am = ea - e * np.sin(ea)
    if nflg in [1, 6]:
        return ea
    if nflg in [2, 4]:
        return f
    if nflg in [3, 5]:
        return am

def kepler1(manom, ecc):
    # Placeholder for kepler1 function, should be replaced with actual implementation
    # Returns (eanom, tanom)
    return manom, manom  # Dummy implementation 