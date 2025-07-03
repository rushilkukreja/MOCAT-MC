import numpy as np

def rot1mat(xval):
    # This function sets up a rotation matrix for an input angle about the first axis.
    c = np.cos(xval)
    s = np.sin(xval)
    outmat = np.zeros((3, 3))
    outmat[0, 0] = 1.0
    outmat[0, 1] = 0.0
    outmat[0, 2] = 0.0
    outmat[1, 0] = 0.0
    outmat[1, 1] = c
    outmat[1, 2] = s
    outmat[2, 0] = 0.0
    outmat[2, 1] = -s
    outmat[2, 2] = c
    return outmat 