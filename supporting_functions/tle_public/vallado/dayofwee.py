"""
------------------------------------------------------------------------------

                           function dayofwee

  this function finds the day of the week for a given julian date.

  author        : david vallado                  719-573-2600   27 may 2002

  references    :
    vallado       2001, 187

[dayofweek] = dayofwee(jd)
------------------------------------------------------------------------------
"""
def dayofwee(jd):
    # 0 = Sunday, 1 = Monday, ..., 6 = Saturday
    dayofweek = int(np.floor(jd + 1.5)) % 7
    return dayofweek 