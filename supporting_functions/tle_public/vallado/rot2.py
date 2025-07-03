# ------------------------------------------------------------------------------
#
#                            function rot2
#
#  this function performs a rotation about the 2nd axis.
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
# [outvec] = rot2 ( vec, xval );
# -----------------------------------------------------------------------------

import numpy as np

def rot2(vec, xval):
    """
    Perform a rotation about the 2nd axis.
    
    Args:
        vec: input vector
        xval: angle of rotation (rad)
        
    Returns:
        outvec: vector result
    """
    temp = vec[2]
    c = np.cos(xval)
    s = np.sin(xval)
    
    outvec = np.zeros(3)
    outvec[2] = c * vec[2] + s * vec[0]
    outvec[0] = c * vec[0] - s * temp
    outvec[1] = vec[1]
    
    return outvec 