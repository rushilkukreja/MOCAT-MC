import numpy as np

def sidereal(jdut1, deltapsi, meaneps, omega, lod, eqeterms):
    """
    Calculates the transformation matrix that accounts for the effects of sidereal time.
    """
    def gstime(jdut1):
        return 0.0
    gmst = gstime(jdut1)
    if (jdut1 > 2450449.5) and (eqeterms > 0):
        ast = gmst + deltapsi * np.cos(meaneps) + 0.00264 * np.pi / (3600 * 180) * np.sin(omega) + 0.000063 * np.pi / (3600 * 180) * np.sin(2.0 * omega)
    else:
        ast = gmst + deltapsi * np.cos(meaneps)
    ast = np.remainder(ast, 2 * np.pi)
    thetasa = 7.29211514670698e-05 * (1.0 - lod / 86400.0)
    omegaearth = thetasa
    st = np.zeros((3, 3))
    st[0, 0] = np.cos(ast)
    st[0, 1] = -np.sin(ast)
    st[1, 0] = np.sin(ast)
    st[1, 1] = np.cos(ast)
    st[2, 2] = 1.0
    stdot = np.zeros((3, 3))
    stdot[0, 0] = -omegaearth * np.sin(ast)
    stdot[0, 1] = -omegaearth * np.cos(ast)
    stdot[1, 0] = omegaearth * np.cos(ast)
    stdot[1, 1] = -omegaearth * np.sin(ast)
    return st, stdot 