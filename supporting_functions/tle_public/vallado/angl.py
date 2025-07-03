# ------------------------------------------------------------------------------
#
#                            function angl
#
#  this function calculates the angle between two vectors.  the output is
#    set to 999999.1 to indicate an undefined value.  be sure to check for
#    this at the output phase.
#
#  author        : david vallado                  719-573-2600   27 may 2002
#
#  revisions
#    vallado     - fix tolerances                                 5 sep 2002
#
#  inputs          description                    range / units
#    vec1        - vector number 1
#    vec2        - vector number 2
#
#  outputs       :
#    theta       - angle between the two vectors  -pi to pi
#
#  locals        :
#    temp        - temporary real variable
#
#  coupling      :
#
# [theta] = angl ( vec1,vec2 );
# -----------------------------------------------------------------------------

import numpy as np

def angl(vec1, vec2):
    """
    Calculate the angle between two vectors. The output is set to 999999.1 
    to indicate an undefined value. Be sure to check for this at the output phase.
    
    Args:
        vec1: vector number 1
        vec2: vector number 2
        
    Returns:
        theta: angle between the two vectors (-pi to pi)
    """
    small = 0.00000001
    undefined = 999999.1
    
    # TODO: Implement mag function
    # magv1 = mag(vec1)
    # magv2 = mag(vec2)
    magv1 = np.linalg.norm(vec1)
    magv2 = np.linalg.norm(vec2)
    
    if magv1 * magv2 > small**2:
        # TODO: Implement dot function
        # temp = dot(vec1, vec2) / (magv1 * magv2)
        temp = np.dot(vec1, vec2) / (magv1 * magv2)
        if abs(temp) > 1.0:
            temp = np.sign(temp) * 1.0
        theta = np.arccos(temp)
    else:
        theta = undefined
    
    return theta 