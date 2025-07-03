# ------------------------------------------------------------------------------
#
#                            function rot3
#
#  this function performs a rotation about the 3rd axis.
#
#  author        : david vallado                  719-573-2600   27 may 2002
#
#  revisions
#                -
#
#  inputs          description                    range / units
#    vec         - input vector
#    xval        - angle of rotation              rad
#
#  outputs       :
#    outvec      - vector result
#
#  locals        :
#    c           - cosine of the angle xval
#    s           - sine of the angle xval
#    temp        - temporary extended value
#
#  coupling      :
#    none.
#
# [outvec] = rot3 ( vec, xval );
# -----------------------------------------------------------------------------

import numpy as np

def rot3(vec, xval):
    """
    Perform a rotation about the 3rd axis.
    
    Args:
        vec: input vector
        xval: angle of rotation (rad)
        
    Returns:
        outvec: vector result
    """
    temp = vec[1]
    c = np.cos(xval)
    s = np.sin(xval)
    
    outvec = np.zeros(3)
    outvec[1] = c * vec[1] - s * vec[0]
    outvec[0] = c * vec[0] + s * temp
    outvec[2] = vec[2]
    
    return outvec 