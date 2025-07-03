# ------------------------------------------------------------------------------
#
#                                  rot3mat
#
#  this function sets up a rotation matrix for an input angle about the third
#    axis.
#
#  author        : david vallado                  719-573-2600   10 jan 2003
#
#  revisions
#                -
#
#  inputs          description                    range / units
#    xval        - angle of rotation              rad
#
#  outputs       :
#    outmat      - matrix result
#
#  locals        :
#    c           - cosine of the angle xval
#    s           - sine of the angle xval
#
#  coupling      :
#    none.
#
# [outmat] = rot3mat ( xval );
# -----------------------------------------------------------------------------

import numpy as np

def rot3mat(xval):
    """
    Set up a rotation matrix for an input angle about the third axis.
    
    Args:
        xval: angle of rotation (rad)
        
    Returns:
        outmat: matrix result
    """
    c = np.cos(xval)
    s = np.sin(xval)
    
    outmat = np.zeros((3, 3))
    outmat[0, 0] = c
    outmat[0, 1] = s
    outmat[0, 2] = 0.0
    
    outmat[1, 0] = -s
    outmat[1, 1] = c
    outmat[1, 2] = 0.0
    
    outmat[2, 0] = 0.0
    outmat[2, 1] = 0.0
    outmat[2, 2] = 1.0
    
    return outmat 