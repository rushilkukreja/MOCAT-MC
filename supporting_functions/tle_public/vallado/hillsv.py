import numpy as np

def hillsv(r, alt, dts, mu, re):
    """
    Calculates initial velocity for hills equations.
    r: initial position vector (m)
    alt: altitude of target satellite (km)
    dts: desired time (s)
    mu: gravitational parameter (consistent units)
    re: radius of central body (consistent units)
    Returns:
        v: initial velocity vector (m/s)
    """
    radius = re + alt
    omega = np.sqrt(mu / (radius ** 3))
    nt = omega * dts
    cosnt = np.cos(nt)
    sinnt = np.sin(nt)
    numkm = ((6.0 * r[0] * (nt - sinnt) - r[1]) * omega * sinnt - 2.0 * omega * r[0] * (4.0 - 3.0 * cosnt) * (1.0 - cosnt))
    denom = (4.0 * sinnt - 3.0 * nt) * sinnt + 4.0 * (1.0 - cosnt) * (1.0 - cosnt)
    v = np.zeros(3)
    if abs(denom) > 1e-6:
        v[1] = numkm / denom
    else:
        v[1] = 0.0
    if abs(sinnt) > 1e-6:
        v[0] = -(omega * r[0] * (4.0 - 3.0 * cosnt) + 2.0 * (1.0 - cosnt) * v[1]) / sinnt
    else:
        v[0] = 0.0
    v[2] = -r[2] * omega / np.tan(nt) if abs(np.tan(nt)) > 1e-6 else 0.0
    return v 