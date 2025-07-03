"""
------------------------------------------------------------------------------

                           function moonill

  this function calculates the illumination due to the moon.

  author        : david vallado                  719-573-2600    9 jun 2002

  references    :
    vallado       2001, 295-297, eq 5-9

[moonillum] = moonill ( f,moonel )
------------------------------------------------------------------------------
"""
def moonill(f, moonel):
    x = moonel / 90.0
    g = 1.0
    if moonel >= 20:
        l0 = -1.95
        l1 = 4.06
        l2 = -4.24
        l3 = 1.56
    elif 5.0 <= moonel < 20.0:
        l0 = -2.58
        l1 = 12.58
        l2 = -42.58
        l3 = 59.06
    elif -0.8 < moonel < 5.0:
        l0 = -2.79
        l1 = 24.27
        l2 = -252.95
        l3 = 1321.29
    else:
        l0 = 0.0
        l1 = 0.0
        l2 = 0.0
        l3 = 0.0
        f = 0.0
        g = 0.0
    l1 = l0 + l1 * x + l2 * x * x + l3 * x * x * x
    l2 = (-0.00868 * f - 2.2e-9 * f ** 4)
    moonillum = 10.0 ** (l1 + l2)
    if moonillum < -1e+36 or moonillum > 0.999:
        moonillum = 0.0
    return moonillum 