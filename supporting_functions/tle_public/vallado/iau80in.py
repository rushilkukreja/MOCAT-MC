import numpy as np

def iau80in():
    """
    Initializes the nutation matrices needed for reduction calculations (FK5 1980).
    Returns:
        iar80: integer array
        rar80: real array (converted to degrees)
    """
    # Placeholder for loading nut80.dat
    # nut80 = np.loadtxt('nut80.dat')
    nut80 = np.zeros((106, 9))  # Dummy placeholder
    iar80 = nut80[:, 0:5]
    rar80 = nut80[:, 5:9]
    convrt = 0.0001 / 3600.0
    for i in range(rar80.shape[0]):
        for j in range(rar80.shape[1]):
            rar80[i, j] = rar80[i, j] * convrt
    return iar80, rar80 