import numpy as np
from EarthModel import EarthModel

def GHorizon(bearing, source, height):
    """
    Compute surface ellipsoid intercept of ray to surface.
    Parameters
    ----------
    bearing : float or np.ndarray
        Bearing angle(s) to surface (radians)
    source : np.ndarray
        Source location in llh (3xN or 3, in radians/meters)
    height : float
        Height of surface above ellipsoid (meters)
    Returns
    -------
    range : np.ndarray
        Range to geometric horizon
    stheta : np.ndarray
        Sine of depression angle
    ctheta : np.ndarray
        Cosine of depression angle
    """
    a, f = EarthModel()
    a = a + height
    b = a * (1 - f)
    aob2 = (a / b) ** 2
    bearing = np.atleast_1d(bearing)
    sz_b = bearing.shape
    # Placeholder: actual computation would go here
    # For now, return zeros of appropriate shape
    range_ = np.zeros(sz_b)
    stheta = np.zeros(sz_b)
    ctheta = np.zeros(sz_b)
    return range_, stheta, ctheta 