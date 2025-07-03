def recovqd(p1, p2, p3, root):
    # This function recovers the time and function values in parabolic blending routines.
    aqd0 = p1
    aqd1 = (-3.0 * p1 + 4.0 * p2 - p3) * 0.5
    aqd2 = (p1 - 2.0 * p2 + p3) * 0.5
    funvalue = aqd2 * root ** 2 + aqd1 * root + aqd0
    return funvalue 