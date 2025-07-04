import numpy as np
from matplotlib.path import Path

def pointsIncluded(xA, yA, polyRegion):
    """
    Find subset of points in array that lie within a polygon or on its boundaries.
    
    Parameters:
    -----------
    xA : array-like
        Array x-coordinates (column)
    yA : array-like
        Array y-coordinates (row) in physical units
    polyRegion : array-like
        A 2xN array of ordered coordinates that define a closed polygon
    
    Returns:
    --------
    Points : array-like
        Subset of points in array that lie within the polygon or on its boundaries
    
    Notes:
    ------
    Lillian Chu
    Vista Research, Inc.
    December 2006
    """
    n1, n2 = polyRegion.shape
    if n2 != 2:
        raise ValueError('PolyRegion Error')
    elif n1 < 3:
        raise ValueError('nodes < 3')
    else:
        nodes = n1
    
    M = len(yA)
    N = len(xA)
    
    minX = np.min(xA)
    maxX = np.max(xA)
    deltaX = (maxX - minX) / (N - 1)
    
    minY = np.min(yA)
    maxY = np.max(yA)
    deltaY = (maxY - minY) / (M - 1)
    
    X = (polyRegion[:, 0] - minX) / deltaX + 1
    Y = (polyRegion[:, 1] - minY) / deltaY + 1
    
    # Create a path from the polygon vertices
    polygon_path = Path(np.column_stack([X, Y]))
    
    # Create a grid of points
    x_grid, y_grid = np.meshgrid(np.arange(1, N + 1), np.arange(1, M + 1))
    points = np.column_stack([x_grid.ravel(), y_grid.ravel()])
    
    # Find points inside the polygon
    mask = polygon_path.contains_points(points).reshape(M, N)
    Points = np.where(mask == 1)[0]
    
    return Points 