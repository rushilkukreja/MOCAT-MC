"""
------------------------------------------------------------------------------

                           function jdayall

  this function finds the julian date given the year, month, day, and time.
    the julian date is defined by each elapsed day since noon, jan 1, 4713 bc.

  author        : david vallado                  719-573-2600   27 may 2002

  references    :
    vallado       2001, 187

jd = jdayall(year, mon, day, hr, min, sec, whichtype)
------------------------------------------------------------------------------
"""
def jdayall(year, mon, day, hr, minute, sec, whichtype):
    if mon <= 2:
        year -= 1
        mon += 12
    if whichtype == 'j':
        b = 0.0
    else:
        b = 2 - int(year * 0.01) + int(int(year * 0.01) * 0.25)
    jd = int(365.25 * (year + 4716)) \
         + int(30.6001 * (mon + 1)) \
         + day + b - 1524.5 \
         + (((sec / 60.0 + minute) / 60.0 + hr) / 24.0)
    return jd 