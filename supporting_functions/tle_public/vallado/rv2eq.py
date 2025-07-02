import numpy as np

def rv2eq(r, v):
    """
    Transforms a position and velocity vector into the flight elements - latgc, lon, fpa, az, position and velocity magnitude.
    """
    def rv2coe(r, v):
        return [1]*11  # Placeholder
    def cot(x):
        return 1 / np.tan(x)
    mu = 398600.4418
    small = 1e-8
    p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = rv2coe(r, v)
    fr = 1
    if abs(incl - np.pi) < small:
        fr = -1
    if ecc < small:
        if incl < small or abs(incl - np.pi) < small:
            argp = 0.0
            omega = 0.0
        else:
            argp = 0.0
    else:
        if incl < small or abs(incl - np.pi) < small:
            argp = lonper
            omega = 0.0
    af = ecc * np.cos(fr * omega + argp)
    ag = ecc * np.sin(fr * omega + argp)
    if fr > 0:
        chi = np.tan(incl * 0.5) * np.sin(omega)
        psi = np.tan(incl * 0.5) * np.cos(omega)
    else:
        chi = cot(incl * 0.5) * np.sin(omega)
        psi = cot(incl * 0.5) * np.cos(omega)
    n = np.sqrt(mu / (a * a * a))
    meanlon = fr * omega + argp + m
    meanlon = np.remainder(meanlon, 2.0 * np.pi)
    return af, ag, meanlon, n, chi, psi 