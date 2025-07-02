import numpy as np

def rvs2raz(rhosez, drhosez):
    """
    Converts range, azimuth, and elevation values with slant range and velocity vectors for a satellite from a radar site in the topocentric horizon (sez) system.
    """
    halfpi = np.pi * 0.5
    small = 1e-8
    def mag(vec):
        return np.linalg.norm(vec)
    temp = np.sqrt(rhosez[0] ** 2 + rhosez[1] ** 2)
    if abs(rhosez[1]) < small:
        if temp < small:
            az = np.arctan2(drhosez[1], -drhosez[0])
        else:
            if rhosez[0] > 0.0:
                az = np.pi
            else:
                az = 0.0
    else:
        az = np.arctan2(rhosez[1], -rhosez[0])
    if temp < small:
        el = np.sign(rhosez[2]) * halfpi
    else:
        el = np.arcsin(rhosez[2] / rhosez[3])
    rho = mag(rhosez)
    drho = np.dot(rhosez, drhosez) / rho
    if abs(temp * temp) > small:
        daz = (drhosez[0] * rhosez[1] - drhosez[1] * rhosez[0]) / (temp * temp)
    else:
        daz = 0.0
    if abs(temp) > small:
        delv = (drhosez[2] - drho * np.sin(el)) / temp
    else:
        delv = 0.0
    return rho, az, el, drho, daz, delv 