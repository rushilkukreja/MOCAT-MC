"""
-----------------------------------------------------------------------------

    invjday.py

    This function finds the year, month, day, hour, minute and second
    given the julian date. tu can be ut1, tdt, tdb, etc.

    Author        : David Vallado (original MATLAB)
    Python port   : OpenAI Assistant, 2024

    Inputs:
        jd         - julian date                    days from 4713 bc

    Outputs:
        year       - year                           1900 .. 2100
        mon        - month                          1 .. 12
        day        - day                            1 .. 28,29,30,31
        hr         - hour                           0 .. 23
        min        - minute                         0 .. 59
        sec        - second                         0.0 .. 59.999

    References:
        Vallado 2007, 208, alg 22, ex 3-13
-----------------------------------------------------------------------------
"""
import numpy as np

def invjday(jd):
    # Find year and days of the year
    temp = jd - 2415019.5
    tu = temp / 365.25
    year = 1900 + np.floor(tu)
    leapyrs = np.floor((year - 1901) * 0.25)
    days = temp - ((year - 1900) * 365.0 + leapyrs)
    
    # Check for case of beginning of a year
    if days < 1.0:
        year = year - 1
        leapyrs = np.floor((year - 1901) * 0.25)
        days = temp - ((year - 1900) * 365.0 + leapyrs)
    
    # Find remaining data
    mon, day, hr, min_val, sec = days2mdh(year, days)
    
    return year, mon, day, hr, min_val, sec

# Placeholder for MATLAB dependencies
def days2mdh(year, days):
    # TODO: Implement days to month, day, hour conversion
    return 1, 1, 0, 0, 0.0 