import numpy as np

def rv2rsw(reci, veci):
    """
    Converts position and velocity vectors into radial, tangential (in-track), and normal (cross-track) coordinates (RSW system).
    """
    def unit(vec):
        magv = np.linalg.norm(vec)
        return vec / magv if magv > 1e-6 else np.zeros_like(vec)
    def matvecmult(mat, vec, n):
        return mat @ vec
    rvec = unit(reci)
    wvec = np.cross(reci, veci)
    wvec = unit(wvec)
    svec = np.cross(wvec, rvec)
    svec = unit(svec)
    transmat = np.vstack([rvec, svec, wvec])
    rrsw = matvecmult(transmat, reci, 3)
    vrsw = matvecmult(transmat, veci, 3)
    return rrsw, vrsw, transmat 