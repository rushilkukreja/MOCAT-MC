"""
------------------------------------------------------------------------------

                           function finddays

  this function finds the fractional days through a year given the year,
    month, day, hour, minute and second.

  author        : david vallado                  719-573-2600   22 jun 2002

  revisions
                -

  inputs          description                    range / units
    year        - year                           1900 .. 2100
    mon         - month                          1 .. 12
    day         - day                            1 .. 28,29,30,31
    hr          - hour                           0 .. 23
    min         - minute                         0 .. 59
    sec         - second                         0.0 .. 59.999

  outputs       :
    days        - day of year plus fraction of a
                    day                          days

  locals        :
    lmonth      - length of months of year
    i           - index

  coupling      :
    none.

  references    :
    vallado       2007, 207, ex 3-12

[days] = finddays ( year,month,day,hr,min,sec)
------------------------------------------------------------------------------
"""
def finddays(year, month, day, hr, minute, sec):
    lmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Leap year adjustment
    if year % 4 == 0:
        lmonth[1] = 29
        if year % 100 == 0 and year % 400 != 0:
            lmonth[1] = 28
    days = 0.0
    for i in range(0, month - 1):
        days += lmonth[i]
    days += day + hr / 24.0 + minute / 1440.0 + sec / 86400.0
    return days 
------------------------------------------------------------------------------

                           function finddays

  this function finds the fractional days through a year given the year,
    month, day, hour, minute and second.

  author        : david vallado                  719-573-2600   22 jun 2002

  revisions
                -

  inputs          description                    range / units
    year        - year                           1900 .. 2100
    mon         - month                          1 .. 12
    day         - day                            1 .. 28,29,30,31
    hr          - hour                           0 .. 23
    min         - minute                         0 .. 59
    sec         - second                         0.0 .. 59.999

  outputs       :
    days        - day of year plus fraction of a
                    day                          days

  locals        :
    lmonth      - length of months of year
    i           - index

  coupling      :
    none.

  references    :
    vallado       2007, 207, ex 3-12

[days] = finddays ( year,month,day,hr,min,sec)
------------------------------------------------------------------------------
"""
def finddays(year, month, day, hr, minute, sec):
    lmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Leap year adjustment
    if year % 4 == 0:
        lmonth[1] = 29
        if year % 100 == 0 and year % 400 != 0:
            lmonth[1] = 28
    days = 0.0
    for i in range(0, month - 1):
        days += lmonth[i]
    days += day + hr / 24.0 + minute / 1440.0 + sec / 86400.0
    return days 