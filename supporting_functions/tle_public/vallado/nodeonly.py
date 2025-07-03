# ------------------------------------------------------------------------------
#
#                           procedure nodeonly
#
#  this procedure calculates the delta v's for a change in longitude of
#    ascending node only.
#
#  author        : david vallado                  719-573-2600    1 mar 2001
#
#  inputs          description                    range / units
#    deltaomega  - change in node                 rad
#    ecc         - ecc of first orbit
#    vinit       - initial velocity vector        er/tu
#    fpa         - flight path angle              rad
#    incl        - inclination                    rad
#
#
#  outputs       :
#    ifinal      - final inclination              rad
#    deltav      - change in velocity             er/tu
#
#  locals        :
#    vfinal      - final velocity vector          er/tu
#    arglat      - argument of latitude           rad
#    arglat1     - final argument of latitude     rad
#    nuinit      - initial true anomaly           rad
#    theta       -
#
#  coupling      :
#    asin      - arc sine function
#    acos      - arc cosine function
#
#  references    :
#    vallado       2007, 349, alg 40, ex 6-5
# function [ifinal,deltav ] = nodeonly(iinit,ecc,deltaomega,vinit,fpa,incl);
# -----------------------------------------------------------------------------

import numpy as np

def nodeonly(iinit, ecc, deltaomega, vinit, fpa, incl):
    """
    Calculate the delta v's for a change in longitude of ascending node only.
    
    Args:
        deltaomega: change in node (rad)
        ecc: eccentricity of first orbit
        vinit: initial velocity vector (er/tu)
        fpa: flight path angle (rad)
        incl: inclination (rad)
        
    Returns:
        ifinal: final inclination (rad)
        deltav: change in velocity (er/tu)
    """
    rad = 57.29577951308230
    
    if abs(ecc) > 0.00000001:
        # ------------------------- elliptical ---------------------
        theta = np.arctan(np.sin(iinit) * np.tan(deltaomega))
        ifinal = np.arcsin(np.sin(theta) / np.sin(deltaomega))
        deltav = 2.0 * vinit * np.cos(fpa) * np.sin(0.5 * theta)
        
        arglat = np.pi * 0.5  # set at 90 deg
        arglat1 = np.arccos(np.cos(incl) * np.sin(incl) * (1.0 - np.cos(deltaomega)) / np.sin(theta))
    else:
        # -------------------------- circular ----------------------
        ifinal = 0.0
        theta = np.arccos(np.cos(iinit) * np.cos(iinit) + np.sin(iinit) * np.sin(iinit) * np.cos(deltaomega))
        deltav = 2.0 * vinit * np.sin(0.5 * theta)
        
        arglat = np.arccos(np.tan(iinit) * (np.cos(deltaomega) - np.cos(theta)) / np.sin(theta))
        arglat1 = np.arccos(np.cos(incl) * np.sin(incl) * (1.0 - np.cos(deltaomega)) / np.sin(theta))
    
    return ifinal, deltav 