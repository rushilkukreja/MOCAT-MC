import numpy as np
import matplotlib.pyplot as plt
from .line12 import line12
from .line21 import line21

def polyregion_add(polyRegion, ifig, *args):
    """
    Add polyRegion outline to current image.
    
    Parameters:
    -----------
    polyRegion : array-like
        A 2xN array of ordered coordinates that define a closed polygon
    ifig : int
        Figure handle
    *args : tuple
        Optional arguments:
        - iR: 1 for Upper, 2 for Lower region, [] for Upper & Lower
        - Col: Line color/style string
    
    Notes:
    ------
    This function requires matplotlib.pyplot to be imported and a figure to be active.
    """
    plt.figure(ifig)
    Col = 'w'
    
    if len(args) == 0:
        iR = []
    elif len(args) == 1:
        iR = args[0]
    else:
        iR = args[0]
        Col = args[1]
    
    n1, n2 = polyRegion.shape
    if n2 != 2:
        raise ValueError('PolyRegion Error')
    elif n1 < 3:
        raise ValueError('nodes < 3')
    else:
        nodes = n1
    
    # Remove redundant node
    polyRegion = polyRegion[:n1-1, :]
    nodes = n1 - 1
    
    xMin, nXmin = np.min(polyRegion[:, 0]), np.argmin(polyRegion[:, 0])
    xMax, nXmax = np.max(polyRegion[:, 0]), np.argmax(polyRegion[:, 0])
    
    # Start with minimum x node
    polyRegion = np.vstack([polyRegion[nXmin:nodes, :], polyRegion[:nXmin, :]])
    
    # Make cyclic
    polyRegion = np.vstack([polyRegion, polyRegion[0, :]])
    
    if iR is None or iR == 1:
        # Upper bounding segments
        for n in range(nXmax - 1):
            plt.hold(True)
            if polyRegion[n+1, 0] != polyRegion[n, 0]:
                xx = np.linspace(polyRegion[n, 0], polyRegion[n+1, 0], 100)
                plt.plot(xx, line12(xx, polyRegion[n, :], polyRegion[n+1, :]), Col)
            else:
                yy = np.linspace(polyRegion[n, 1], polyRegion[n+1, 1], 100)
                plt.plot(line21(yy, polyRegion[n, :], polyRegion[n+1, :]), yy, Col)
    
    if iR is None or iR == 2:
        # Lower bounding segments
        for n in range(nXmax, nodes):
            plt.hold(True)
            if polyRegion[n+1, 0] != polyRegion[n, 0]:
                xx = np.linspace(polyRegion[n, 0], polyRegion[n+1, 0], 100)
                plt.plot(xx, line12(xx, polyRegion[n, :], polyRegion[n+1, :]), Col)
            else:
                yy = np.linspace(polyRegion[n, 1], polyRegion[n+1, 1], 100)
                plt.plot(line21(yy, polyRegion[n, :], polyRegion[n+1, :]), yy, Col) 