import numpy as np

def line12(x, xy1, xy2):
    """
    Calculate y-coordinate for a non-vertical line given x-coordinate and two points.
    
    Parameters:
    -----------
    x : float or array-like
        x-coordinate(s) for which to find y-coordinate(s)
    xy1 : array-like
        First point coordinates [x1, y1]
    xy2 : array-like
        Second point coordinates [x2, y2]
    
    Returns:
    --------
    y : float or array-like
        y-coordinate(s) corresponding to the given x-coordinate(s)
    
    Raises:
    -------
    ValueError
        If the line is vertical (x1 == x2)
    """
    if xy1[0] == xy2[0]:
        raise ValueError('Use line21 for vertical lines')
    else:
        y = (xy2[1] - xy1[1]) * (x - xy1[0]) / (xy2[0] - xy1[0]) + xy1[1]
    return y 