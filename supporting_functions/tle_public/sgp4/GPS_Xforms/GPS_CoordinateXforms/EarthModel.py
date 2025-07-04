def EarthModel():
    """
    Define the constants for the WGS-84 ellipsoidal Earth model.
    Returns
    -------
    a : float
        Semi-major axis of the Earth ellipsoid model (meters)
    f : float
        Flattening
    """
    a = 6378137.0  # meters
    f = 1.0 / 298.257223563
    return a, f 