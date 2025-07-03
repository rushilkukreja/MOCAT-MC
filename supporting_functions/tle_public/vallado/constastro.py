"""
------------------------------------------------------------------------------

                           file: constastro.m

  this file contains commonly used astronomical constants.

  author        : david vallado                  719-573-2600   27 may 2002

  references    :
    vallado       2001, 1-6
------------------------------------------------------------------------------
"""
import numpy as np

# Astronomical constants
re = 6378.137          # Earth equatorial radius (km)
mu = 398600.4418       # Earth gravitational parameter (km^3/s^2)
au = 149597870.0       # Astronomical unit (km)
omegaearth = 7.292115e-5  # Earth rotation rate (rad/s)
flat = 1.0 / 298.257223563  # Earth flattening
j2 = 1.08262668e-3     # J2 harmonic (nondim)
j3 = -2.53215306e-6    # J3 harmonic (nondim)
j4 = -1.61098761e-6    # J4 harmonic (nondim)

# Add more constants as needed from the original file 