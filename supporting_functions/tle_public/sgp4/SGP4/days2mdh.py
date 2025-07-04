import numpy as np

def days2mdh(year, days):
    """
    Convert day of year to month, day, hour, minute, second.
    
    Parameters:
    -----------
    year : int
        Year
    days : float
        Day of year (1.0 to 366.0)
    
    Returns:
    --------
    mon : int
        Month (1-12)
    day : int
        Day of month (1-31)
    hr : int
        Hour (0-23)
    minute : int
        Minute (0-59)
    sec : float
        Second (0-59.999...)
    """
    # Days in each month (non-leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check if leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    
    # Find month and day
    day_of_year = int(days)
    remaining_days = days - day_of_year
    
    mon = 1
    day = day_of_year
    
    for i, days_in_mon in enumerate(days_in_month):
        if day <= days_in_mon:
            mon = i + 1
            break
        day -= days_in_mon
    
    # Convert remaining fraction to time
    total_seconds = remaining_days * 24 * 3600
    hr = int(total_seconds // 3600)
    minute = int((total_seconds % 3600) // 60)
    sec = total_seconds % 60
    
    return mon, day, hr, minute, sec 