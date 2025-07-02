import numpy as np

def rv2ntw(r, v):
    """
    Converts position and velocity vectors into normal (in-radial), tangential (velocity), and normal (cross-track) coordinates (NTW system).
    """
    def mag(vec):
        return np.linalg.norm(vec)
    def unit(vec):
        magv = mag(vec)
        return vec / magv if magv > 1e-6 else np.zeros_like(vec)
    def matvecmult(mat, vec, n):
        return mat @ vec
    vmag = mag(v)
    tvec = v / vmag
    wvec = np.cross(r, v)
    wvec = unit(wvec)
    nvec = np.cross(tvec, wvec)
    nvec = unit(nvec)
    transmat = np.vstack([nvec, tvec, wvec])
    rntw = matvecmult(transmat, r, 3)
    vntw = matvecmult(transmat, v, 3)
    return rntw, vntw, transmat 