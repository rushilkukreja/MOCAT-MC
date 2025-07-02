"""
Configuration constants for MOCAT-MC
Python version of cfgMC_constants.m
"""

import numpy as np
from scipy import constants

def get_cfgMC_constants():
    """Get MOCAT-MC configuration constants"""
    
    # Set conversion units
    cfgMC = {}
    cfgMC['DAY2MIN'] = 60 * 24
    cfgMC['DAY2SEC'] = cfgMC['DAY2MIN'] * 60
    cfgMC['YEAR2DAY'] = 365.2425  # days per year
    cfgMC['YEAR2MIN'] = cfgMC['YEAR2DAY'] * cfgMC['DAY2MIN']
    cfgMC['rad'] = np.pi / 180
    
    # GLOBAL VARIABLES - using WGS84 constants
    # These correspond to whichconst = 84 in MATLAB
    cfgMC['tumin'] = 13.4468396969593  # minutes in one time unit
    cfgMC['mu_const'] = 398600.4418  # km^3/s^2 (Earth's gravitational parameter)
    cfgMC['radiusearthkm'] = 6378.137  # km (Earth's equatorial radius)
    cfgMC['xke'] = 0.0743669161331734  # sqrt of Earth's gravitational parameter in earth radii^3/min^2
    cfgMC['j2'] = 0.001082616  # J2 harmonic coefficient
    cfgMC['j3'] = -0.00000253881  # J3 harmonic coefficient
    cfgMC['j4'] = -0.00000165597  # J4 harmonic coefficient
    cfgMC['j3oj2'] = cfgMC['j3'] / cfgMC['j2']
    cfgMC['omega_earth'] = 2 * np.pi / cfgMC['DAY2SEC']  # Earth's rotation rate (rad/s)
    
    return cfgMC

# Create global constants for backward compatibility
cfgMC = get_cfgMC_constants()

# Make constants available as module-level variables
DAY2MIN = cfgMC['DAY2MIN']
DAY2SEC = cfgMC['DAY2SEC']
YEAR2DAY = cfgMC['YEAR2DAY']
YEAR2MIN = cfgMC['YEAR2MIN']
rad = cfgMC['rad']
tumin = cfgMC['tumin']
mu_const = cfgMC['mu_const']
radiusearthkm = cfgMC['radiusearthkm']
j2 = cfgMC['j2']
omega_earth = cfgMC['omega_earth'] 