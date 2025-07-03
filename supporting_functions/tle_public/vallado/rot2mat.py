# ------------------------------------------------------------------------------
#
#                                  rot2mat
#
#  this function sets up a rotation matrix for an input angle about the second
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
# [outmat] = rot2mat ( xval );
# -----------------------------------------------------------------------------

import numpy as np

def rot2mat(xval):
    """
    Set up a rotation matrix for an input angle about the second axis.
    
    Args:
        xval: angle of rotation (rad)
        
    Returns:
        outmat: matrix result
    """
    c = np.cos(xval)
    s = np.sin(xval)
    
    outmat = np.zeros((3, 3))
    outmat[0, 0] = c
    outmat[0, 1] = 0.0
    outmat[0, 2] = -s
    
    outmat[1, 0] = 0.0
    outmat[1, 1] = 1.0
    outmat[1, 2] = 0.0
    
    outmat[2, 0] = s
    outmat[2, 1] = 0.0
    outmat[2, 2] = c
    
    return outmat 