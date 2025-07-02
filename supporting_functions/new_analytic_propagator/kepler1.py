import numpy as np

def kepler1(manom, ecc):
    """
    Solve Kepler's equation for circular, elliptic, and hyperbolic orbits using Danby's method.
    manom: float or ndarray (mean anomaly in radians)
    ecc: float or ndarray (eccentricity)
    Returns:
        eanom: eccentric anomaly (radians)
        tanom: true anomaly (radians)
    """
    manom = np.asarray(manom)
    ecc = np.asarray(ecc)
    pi2 = 2.0 * np.pi
    xma = manom - pi2 * np.floor(manom / pi2)
    # Initial guess
    eanom = np.where(ecc == 0.0, xma, np.where(ecc < 1.0, xma + 0.85 * np.sign(np.sin(xma)) * ecc, np.log(2.0 * xma / ecc + 1.8)))
    # Iteration
    niter = 0
    ktol = 1.0e-10
    converged = np.zeros_like(xma, dtype=bool)
    while not np.all(converged) and niter < 20:
        idx = ~converged
        if np.any(ecc[idx] < 1):
            s = ecc[idx] * np.sin(eanom[idx])
            c = ecc[idx] * np.cos(eanom[idx])
            f = eanom[idx] - s - xma[idx]
            fp = 1 - c
            fpp = s
            fppp = c
        else:
            s = ecc[idx] * np.sinh(eanom[idx])
            c = ecc[idx] * np.cosh(eanom[idx])
            f = s - eanom[idx] - xma[idx]
            fp = c - 1
            fpp = s
            fppp = c
        delta = -f / fp
        deltastar = -f / (fp + 0.5 * delta * fpp)
        deltak = -f / (fp + 0.5 * deltastar * fpp + deltastar ** 2 * fppp / 6)
        eanom[idx] = eanom[idx] + deltak
        converged[idx] = np.abs(f) <= ktol
        niter += 1
    # True anomaly
    if np.any(ecc < 1):
        sta = np.sqrt(1 - ecc ** 2) * np.sin(eanom)
        cta = np.cos(eanom) - ecc
    else:
        sta = np.sqrt(ecc ** 2 - 1) * np.sinh(eanom)
        cta = ecc - np.cosh(eanom)
    tanom = np.arctan2(sta, cta)
    return eanom, tanom 