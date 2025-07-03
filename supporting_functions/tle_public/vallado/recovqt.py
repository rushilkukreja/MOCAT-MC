def recovqt(p1, p2, p3, p4, p5, p6, root):
    # This function recovers the time and function values in quartic blending routines.
    temp = 1.0 / 24.0
    aqit0 = p3
    aqit1 = (2 * p1 - 16 * p2 + 16 * p4 - 2 * p5) * temp
    aqit2 = (-1 * p1 + 16 * p2 - 30 * p3 + 16 * p4 - p5) * temp
    aqit3 = (-9 * p1 + 39 * p2 - 70 * p3 + 66 * p4 - 33 * p5 + 7 * p6) * temp
    aqit4 = (13 * p1 - 64 * p2 + 126 * p3 - 124 * p4 + 61 * p5 - 12 * p6) * temp
    aqit5 = (-5 * p1 + 25 * p2 - 50 * p3 + 50 * p4 - 25 * p5 + 5 * p6) * temp
    funvalue = aqit5 * root ** 5 + aqit4 * root ** 4 + aqit3 * root ** 3 + aqit2 * root ** 2 + aqit1 * root + aqit0
    return funvalue 