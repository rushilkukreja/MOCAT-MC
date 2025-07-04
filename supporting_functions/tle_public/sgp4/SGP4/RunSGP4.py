import numpy as np

def RunSGP4(satrec, tsince):
    """
    Run SGP4 propagation.
    
    Parameters:
    -----------
    satrec : dict
        Satellite record structure
    tsince : float
        Time since epoch in minutes
    
    Returns:
    --------
    r : array-like
        Position vector in TEME coordinates (km)
    v : array-like
        Velocity vector in TEME coordinates (km/s)
    """
    # Placeholder implementation
    # You need to implement the actual SGP4 propagation here
    
    # This is likely a wrapper around the sgp4 function
    r, v = sgp4(satrec, tsince)
    
    return r, v 