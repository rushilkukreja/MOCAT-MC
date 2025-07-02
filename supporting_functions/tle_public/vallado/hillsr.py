import numpy as np

def hillsr(r, v, alt, dts, mu, re):
    """
    Calculates various position information for hills equations.
    r: initial position vector (m)
    v: initial velocity vector (m/s)
    alt: altitude of target satellite (m)
    dts: desired time (s)
    mu: gravitational parameter (consistent units)
    re: radius of central body (consistent units)
    Returns:
        rint: final position vector (m)
        vint: final velocity vector (m/s)
    """
    radius = re + alt
    omega = np.sqrt(mu / (radius ** 3))
    nt = omega * dts
    cosnt = np.cos(nt)
    sinnt = np.sin(nt)
    rint = np.zeros(3)
    rint[0] = (v[0] / omega) * sinnt - ((2.0 * v[1] / omega) + 3.0 * r[0]) * cosnt + ((2.0 * v[1] / omega) + 4.0 * r[0])
    rint[1] = (2.0 * v[0] / omega) * cosnt + ((4.0 * v[1] / omega) + 6.0 * r[0]) * sinnt + (r[1] - (2.0 * v[0] / omega)) - (3.0 * v[1] + 6.0 * omega * r[0]) * dts
    rint[2] = r[2] * cosnt + (v[2] / omega) * sinnt
    vint = np.zeros(3)
    vint[0] = v[0] * cosnt + (2.0 * v[1] + 3.0 * omega * r[0]) * sinnt
    vint[1] = -2.0 * v[0] * sinnt + (4.0 * v[1] + 6.0 * omega * r[0]) * cosnt - (3.0 * v[1] + 6.0 * omega * r[0])
    vint[2] = -r[2] * omega * np.sin(nt) + v[2] * cosnt
    return rint, vint 