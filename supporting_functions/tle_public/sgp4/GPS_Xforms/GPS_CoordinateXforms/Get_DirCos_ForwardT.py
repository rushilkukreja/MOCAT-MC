import numpy as np

YAW_TYPE = 1
PITCH_TYPE = 2
ROLL_TYPE = 3

def Get_DirCos_ForwardT(A, MatrixFlavor):
    """
    Fills a direction cosine matrix defined by positive right-hand rule Euler angles.
    Transforms from an INS type basis to a body type basis.
    Parameters
    ----------
    A : float or np.ndarray
        Angle(s) in radians
    MatrixFlavor : int
        Axis type: YAW_TYPE, PITCH_TYPE, or ROLL_TYPE
    Returns
    -------
    DC : np.ndarray
        Direction cosine matrix (3x3 or 3x3xN)
    """
    A = np.atleast_1d(A)
    N = A.size
    DC = np.zeros((3, 3, N))
    for i, angle in enumerate(A):
        if MatrixFlavor == YAW_TYPE:
            DC[:, :, i] = np.array([
                [np.cos(angle), -np.sin(angle), 0],
                [np.sin(angle),  np.cos(angle), 0],
                [0, 0, 1]
            ])
        elif MatrixFlavor == PITCH_TYPE:
            DC[:, :, i] = np.array([
                [np.cos(angle), 0, np.sin(angle)],
                [0, 1, 0],
                [-np.sin(angle), 0, np.cos(angle)]
            ])
        elif MatrixFlavor == ROLL_TYPE:
            DC[:, :, i] = np.array([
                [1, 0, 0],
                [0, np.cos(angle), -np.sin(angle)],
                [0, np.sin(angle),  np.cos(angle)]
            ])
        else:
            raise ValueError('Unknown MatrixFlavor')
    if N == 1:
        return DC[:, :, 0]
    return DC 