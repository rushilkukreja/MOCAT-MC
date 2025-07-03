import numpy as np

def mag(vec):
    return np.linalg.norm(vec)

def rot1(vec, xval):
    # Placeholder for rot1 rotation about the 1st axis
    # This should be replaced with the actual implementation
    return vec

def rv2ell(rijk, vijk):
    # position and velocity to ecliptic latitude longitude
    # dav 28 mar 04
    # [rr,ecllon,ecllat,drr,decllon,decllat] = rv2ell (rijk,vijk)
    small = 1e-10
    obliquity = 0.40909280  # 23.439291 /rad
    r = rot1(rijk, obliquity)
    v = rot1(vijk, obliquity)
    rr = mag(r)
    temp = np.sqrt(r[0]**2 + r[1]**2)
    if temp < small:
        temp1 = np.sqrt(v[0]**2 + v[1]**2)
        if abs(temp1) > small:
            ecllon = np.arctan2(v[1], v[0])
        else:
            ecllon = 0.0
    else:
        ecllon = np.arctan2(r[1], r[0])
    ecllat = np.arcsin(r[2] / rr)
    temp1 = -r[1]**2 - r[0]**2  # different now
    drr = np.dot(r, v) / rr
    if abs(temp1) > small:
        decllon = (v[0]*r[1] - v[1]*r[0]) / temp1
    else:
        decllon = 0.0
    if abs(temp) > small:
        decllat = (v[2] - drr * np.sin(ecllat)) / temp
    else:
        decllat = 0.0
    return rr, ecllon, ecllat, drr, decllon, decllat 