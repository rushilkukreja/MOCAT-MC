import numpy as np

def rot1(vec, xval):
    # This function performs a rotation about the 1st axis.
    c = np.cos(xval)
    s = np.sin(xval)
    outvec = np.zeros(3)
    outvec[2] = c * vec[2] - s * vec[1]
    outvec[1] = c * vec[1] + s * vec[2]
    outvec[0] = vec[0]
    return outvec 