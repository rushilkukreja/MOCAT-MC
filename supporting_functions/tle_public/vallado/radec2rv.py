import numpy as np

def rv2radec(rr, rtasc, decl, drr, drtasc, ddecl):
    # This function converts the right ascension and declination values with
    # position and velocity vectors of a satellite. Uses velocity vector to
    # find the solution of singular cases.
    small = 1e-8
    r = np.zeros(3)
    v = np.zeros(3)
    r[0] = rr * np.cos(decl) * np.cos(rtasc)
    r[1] = rr * np.cos(decl) * np.sin(rtasc)
    r[2] = rr * np.sin(decl)
    v[0] = drr * np.cos(decl) * np.cos(rtasc) - rr * np.sin(decl) * np.cos(rtasc) * ddecl \
           - rr * np.cos(decl) * np.sin(rtasc) * drtasc
    v[1] = drr * np.cos(decl) * np.sin(rtasc) - rr * np.sin(decl) * np.sin(rtasc) * ddecl \
           + rr * np.cos(decl) * np.cos(rtasc) * drtasc
    v[2] = drr * np.sin(decl) + rr * np.cos(decl) * ddecl
    return r, v 