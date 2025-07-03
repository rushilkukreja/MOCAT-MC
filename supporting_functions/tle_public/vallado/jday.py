# -----------------------------------------------------------------------------
#
#                           function jday
#
#  this function finds the julian date given the year, month, day, and time.
#
#  author        : david vallado                  719-573-2600   27 may 2002
#
#  revisions
#                -
#
#  inputs          description                    range / units
#    year        - year                           1900 .. 2100
#    mon         - month                          1 .. 12
#    day         - day                            1 .. 28,29,30,31
#    hr          - universal time hour            0 .. 23
#    min         - universal time min             0 .. 59
#    sec         - universal time sec             0.0 .. 59.999
#    whichtype   - julian .or. gregorian calender   'j' .or. 'g'
#
#  outputs       :
#    jd          - julian date                    days from 4713 bc
#
#  locals        :
#    none.
#
#  coupling      :
#    none.
#
#  references    :
#    vallado       2007, 189, alg 14, ex 3-14
#
# jd = jday(yr, mon, day, hr, min, sec)
# -----------------------------------------------------------------------------

import numpy as np

def jday(yr, mon, day, hr, min, sec):
    """
    Find the julian date given the year, month, day, and time.
    
    Args:
        yr: year (1900 .. 2100)
        mon: month (1 .. 12)
        day: day (1 .. 28,29,30,31)
        hr: universal time hour (0 .. 23)
        min: universal time min (0 .. 59)
        sec: universal time sec (0.0 .. 59.999)
        
    Returns:
        jd: julian date (days from 4713 bc)
    """
    # ------------------------  implementation   ------------------
    jd = (367.0 * yr 
          - np.floor((7 * (yr + np.floor((mon + 9) / 12.0))) * 0.25)
          + np.floor(275 * mon / 9.0)
          + day + 1721013.5
          + ((sec / 60.0 + min) / 60.0 + hr) / 24.0)
    #  - 0.5 * sign(100.0 * yr + mon - 190002.5) + 0.5;
    
    return jd 