def sec2hms(utsec):
    """
    Converts seconds from the beginning of the day into hours, minutes, and seconds.
    """
    temp = utsec / 3600.0
    hr = int(temp)
    min_ = int((temp - hr) * 60.0)
    sec = (temp - hr - min_ / 60.0) * 3600.0
    return hr, min_, sec 