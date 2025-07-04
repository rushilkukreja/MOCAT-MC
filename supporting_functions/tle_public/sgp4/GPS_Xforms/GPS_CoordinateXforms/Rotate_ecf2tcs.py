import numpy as np

def Rotate_ecf2tcs(origin):
    """
    Rotate free ECF vector into alignment with TCS.
    Parameters
    ----------
    origin : array-like
        Origin [latitude, longitude, ...] in radians
    Returns
    -------
    D : np.ndarray
        3x3 rotation matrix
    """
    clat = np.cos(origin[0])
    slat = np.sin(origin[0])
    clon = np.cos(origin[1])
    slon = np.sin(origin[1])
    D = np.array([
        [-slon, clon, 0],
        [-slat*clon, -slat*slon, clat],
        [clat*clon, clat*slon, slat]
    ])
    return D 