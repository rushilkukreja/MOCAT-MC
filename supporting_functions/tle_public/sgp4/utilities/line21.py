import numpy as np

def line21(y, xy1, xy2):
    """
    Calculate x-coordinate for a non-horizontal line given y-coordinate and two points.
    
    Parameters:
    -----------
    y : float or array-like
        y-coordinate(s) for which to find x-coordinate(s)
    xy1 : array-like
        First point coordinates [x1, y1]
    xy2 : array-like
        Second point coordinates [x2, y2]
    
    Returns:
    --------
    x : float or array-like
        x-coordinate(s) corresponding to the given y-coordinate(s)
    
    Raises:
    -------
    ValueError
        If the line is horizontal (y1 == y2)
    """
    if xy1[1] == xy2[1]:
        raise ValueError('Use line12 for horizontal lines')
    else:
        x = (xy2[0] - xy1[0]) * (y - xy1[1]) / (xy2[1] - xy1[1]) + xy1[0]
    return x 