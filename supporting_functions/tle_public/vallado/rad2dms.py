# -----------------------------------------------------------------------------
#
#                           function rad2dms
#
#  this function converts radians to degrees, minutes and seconds.
#
#  author        : david vallado                  719-573-2600   27 may 2002
#
#  revisions
#                -
#
#  inputs          description                    range / units
#    dms         - result                         rad
#
#  outputs       :
#    deg         - degrees                        0 .. 360
#    min         - minutes                        0 .. 59
#    sec         - seconds                        0.0 .. 59.99
#
#  locals        :
#    temp        - temporary variable
#
#  coupling      :
#    none.
#
#  references    :
#    vallado       2001, 199, alg 17 alg 18, ex 3-8
#
# [deg,min,sec] = rad2dms( dms );
# -----------------------------------------------------------------------------

import numpy as np

def rad2dms(dms):
    """
    Convert radians to degrees, minutes and seconds.
    
    Args:
        dms: result (rad)
        
    Returns:
        deg: degrees (0 .. 360)
        min: minutes (0 .. 59)
        sec: seconds (0.0 .. 59.99)
    """
    rad2deg = 180.0 / np.pi
    
    # ------------------------  implementation   ------------------
    temp = dms * rad2deg
    deg = int(temp)
    min_val = int((temp - deg) * 60.0)
    sec = (temp - deg - min_val / 60.0) * 3600.0
    
    return deg, min_val, sec 