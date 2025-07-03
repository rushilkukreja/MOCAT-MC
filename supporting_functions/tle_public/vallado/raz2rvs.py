import numpy as np

def raz2rvs(rho, az, el, drho, daz, del_):
    # This function converts range, azimuth, and elevation values with slant
    # range and velocity vectors for a satellite from a radar site in the
    # topocentric horizon (sez) system.
    sinel = np.sin(el)
    cosel = np.cos(el)
    sinaz = np.sin(az)
    cosaz = np.cos(az)
    rhosez = np.zeros(3)
    drhosez = np.zeros(3)
    # SEZ range vector
    rhosez[0] = -rho * cosel * cosaz
    rhosez[1] =  rho * cosel * sinaz
    rhosez[2] =  rho * sinel
    # SEZ velocity vector
    drhosez[0] = -drho * cosel * cosaz + rhosez[2] * del_ * cosaz + rhosez[1] * daz
    drhosez[1] =  drho * cosel * sinaz - rhosez[2] * del_ * sinaz - rhosez[0] * daz
    drhosez[2] =  drho * sinel + rho * del_ * cosel
    return rhosez, drhosez 