"""
------------------------------------------------------------------------------

                           function moon

  this function calculates the geocentric equatorial (ijk) position vector
    for the moon given the julian date.

  author        : david vallado                  719-573-2600   27 may 2002

  revisions
                -

  inputs          description                    range / units
    jd          - julian date                    days from 4713 bc

  outputs       :
    rmoon       - ijk position vector of moon    er
    rtasc       - right ascension                rad
    decl        - declination                    rad

  references    :
    vallado       2007, 290, alg 31, ex 5-3

[rmoon, rtasc,decl] = moon ( jd )
------------------------------------------------------------------------------
"""
import numpy as np

def moon(jd):
    twopi = 2.0 * np.pi
    deg2rad = np.pi / 180.0
    # Implementation
    ttdb = (jd - 2451545.0) / 36525.0
    eclplong = (218.32 + 481267.8813 * ttdb
                + 6.29 * np.sin((134.9 + 477198.85 * ttdb) * deg2rad)
                - 1.27 * np.sin((259.2 - 413335.38 * ttdb) * deg2rad)
                + 0.66 * np.sin((235.7 + 890534.23 * ttdb) * deg2rad)
                + 0.21 * np.sin((269.9 + 954397.70 * ttdb) * deg2rad)
                - 0.19 * np.sin((357.5 + 35999.05 * ttdb) * deg2rad)
                - 0.11 * np.sin((186.6 + 966404.05 * ttdb) * deg2rad))
    eclplat = (5.13 * np.sin((93.3 + 483202.03 * ttdb) * deg2rad)
               + 0.28 * np.sin((228.2 + 960400.87 * ttdb) * deg2rad)
               - 0.28 * np.sin((318.3 + 6003.18 * ttdb) * deg2rad)
               - 0.17 * np.sin((217.6 - 407332.20 * ttdb) * deg2rad))
    hzparal = (0.9508 + 0.0518 * np.cos((134.9 + 477198.85 * ttdb) * deg2rad)
               + 0.0095 * np.cos((259.2 - 413335.38 * ttdb) * deg2rad)
               + 0.0078 * np.cos((235.7 + 890534.23 * ttdb) * deg2rad)
               + 0.0028 * np.cos((269.9 + 954397.70 * ttdb) * deg2rad))
    eclplong = np.remainder(eclplong * deg2rad, twopi)
    eclplat = np.remainder(eclplat * deg2rad, twopi)
    hzparal = np.remainder(hzparal * deg2rad, twopi)
    obliquity = 23.439291 - 0.0130042 * ttdb  # deg
    obliquity = obliquity * deg2rad
    # Geocentric direction cosines
    l = np.cos(eclplat) * np.cos(eclplong)
    m = np.cos(obliquity) * np.cos(eclplat) * np.sin(eclplong) - np.sin(obliquity) * np.sin(eclplat)
    n = np.sin(obliquity) * np.cos(eclplat) * np.sin(eclplong) + np.cos(obliquity) * np.sin(eclplat)
    # Moon position vector
    magr = 1.0 / np.sin(hzparal)
    rmoon = np.array([magr * l, magr * m, magr * n])
    # Right ascension and declination
    rtasc = np.arctan2(m, l)
    decl = np.arcsin(n)
    return rmoon, rtasc, decl 