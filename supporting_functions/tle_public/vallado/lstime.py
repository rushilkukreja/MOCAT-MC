# -----------------------------------------------------------------------------
#
#                           function lstime
#
#  this function finds the local sidereal time at a given location.
#
#  author        : david vallado                  719-573-2600   27 may 2002
#
#  revisions
#                -
#
#  inputs          description                    range / units
#    lon         - site longitude (west -)        -2pi to 2pi rad
#    jd          - julian date                    days from 4713 bc
#
#  outputs       :
#    lst         - local sidereal time            0.0 to 2pi rad
#    gst         - greenwich sidereal time        0.0 to 2pi rad
#
#  locals        :
#    none.
#
#  coupling      :
#    gstime        finds the greenwich sidereal time
#
#  references    :
#    vallado       2007, 194, alg 15, ex 3-5
#
# [lst,gst] = lstime ( lon, jd );
# -----------------------------------------------------------------------------

import numpy as np

def lstime(lon, jd):
    """
    Find the local sidereal time at a given location.
    
    Args:
        lon: site longitude (west -) (-2pi to 2pi rad)
        jd: julian date (days from 4713 bc)
        
    Returns:
        lst: local sidereal time (0.0 to 2pi rad)
        gst: greenwich sidereal time (0.0 to 2pi rad)
    """
    twopi = 2.0 * np.pi
    
    # ------------------------  implementation   ------------------
    # TODO: Implement gstime function
    # [gst] = gstime(jd)
    gst = None  # Placeholder for gstime function
    
    if gst is not None:
        lst = lon + gst
        
        # ----------------------- check quadrants ---------------------
        lst = np.remainder(lst, twopi)
        if lst < 0.0:
            lst = lst + twopi
    else:
        lst = None
    
    return lst, gst 