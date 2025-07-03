# -----------------------------------------------------------------------------
#
#                           function inittime
#
#  this function initializes some of the time variables.
#
#  revisions
#                -
#
#  inputs          description                    range / units
#
#
#  outputs       :
#
#
#  locals        :
#    i           - index
#
#  coupling      :
#    none
#
# -----------------------------------------------------------------------------

def inittime():
    """
    Initialize some of the time variables.
    
    Returns:
        lmonth: array of days in each month
        monthtitle: array of month abbreviations
        daytitle: array of day abbreviations
    """
    # ------------------------  implementation   ------------------
    
    # inittime.m
    lmonth = [0] * 12
    
    for i in range(12):
        if i + 1 in [1, 3, 5, 7, 8, 10, 12]:
            lmonth[i] = 31
        elif i + 1 in [4, 6, 9, 11]:
            lmonth[i] = 30
        elif i + 1 == 2:
            lmonth[i] = 28
    
    monthtitle = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                  'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    
    daytitle = ['sun', 'mon', 'tue', 'wed', 'thr', 'fri', 'sat']
    
    return lmonth, monthtitle, daytitle 