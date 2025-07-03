"""
------------------------------------------------------------------------------

                           function days2mdh

  this function converts the day of the year and year into month, day, hour,
    minute, and second.

  author        : david vallado                  719-573-2600   27 may 2002

  references    :
    vallado       2001, 183

[mon,day,hr,minute,sec] = days2mdh(year, days)
------------------------------------------------------------------------------
"""
def days2mdh(year, days):
    lmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Leap year check
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        lmonth[1] = 29
    dayofyr = int(np.floor(days))
    temp = 0
    mon = 1
    while dayofyr > lmonth[mon-1] and mon < 12:
        dayofyr -= lmonth[mon-1]
        mon += 1
    day = dayofyr
    temp = (days - np.floor(days)) * 24.0
    hr = int(np.floor(temp))
    temp = (temp - hr) * 60.0
    minute = int(np.floor(temp))
    sec = (temp - minute) * 60.0
    return mon, day, hr, minute, sec 