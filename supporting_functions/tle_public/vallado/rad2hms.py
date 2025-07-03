# -----------------------------------------------------------------------------
#
#                           function rad2hms
#
#  this function converts radians to hours, minutes and seconds.  notice
#    the conversion 0.2617 is simply the radian equivalent of 15 degrees.
#
#  author        : david vallado                  719-573-2600   27 may 2002
#
#  revisions
#                -
#
#  inputs          description                    range / units
#    hms         - result                         rad
#
#  outputs       :
#    hr          - hours                          0 .. 24
#    min         - minutes                        0 .. 59
#    sec         - seconds                        0.0 .. 59.99
#
#  locals        :
#    temp        - conversion from hours to rad   0.261799
#
#  coupling      :
#    none.
#
#  references    :
#    vallado       2001, 200, alg 19 alg 20, ex 3-9
#
# [hr,min,sec] = rad2hms( hms );
# -----------------------------------------------------------------------------

import numpy as np

def rad2hms(hms):
    """
    Convert radians to hours, minutes and seconds. Notice the conversion 
    0.2617 is simply the radian equivalent of 15 degrees.
    
    Args:
        hms: result (rad)
        
    Returns:
        hr: hours (0 .. 24)
        min: minutes (0 .. 59)
        sec: seconds (0.0 .. 59.99)
    """
    # ------------------------  implementation   ------------------
    temp = 15.0 * np.pi / 180.0
    
    temp = hms / temp
    hr = int(temp)
    min_val = int((temp - hr) * 60.0)
    sec = (temp - hr - min_val / 60.0) * 3600.0
    
    return hr, min_val, sec 