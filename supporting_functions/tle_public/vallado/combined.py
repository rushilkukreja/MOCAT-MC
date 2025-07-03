# ------------------------------------------------------------------------------
#
#                           procedure combined
#
#  this procedure calculates the delta v's for a combined maneuver.
#
#  author        : david vallado                  719-573-2600    1 mar 2001
#
#  inputs          description                    range / units
#    rinit       - initial position magnitude     er
#    rfinal      - final position magnitude       er
#    einit       - eccentricity of first orbit
#    efinal      - eccentricity of final orbit
#    deltai      - inclination change             rad
#
#  outputs       :
#    deltai1     - amount of incl chg req at a    rad
#    deltava     - change in velocity at point a  er / tu
#    deltavb     - change in velocity at point b  er / tu
#    gam1        - angle 1                        rad
#    gam2        - angle 2                        rad
#
#  locals        :
#    mu          - gravitational parameter
#    a1          - semimajor axis of first orbit  er
#    a2          - semimajor axis of transfer     er
#    e2          - eccentricity squared
#    sme1        - mech energy of first orbit     er2 / tu
#    sme2        - mech energy of transfer orbit  er2 / tu
#    vinit       - velocity of first orbit at a   er / tu
#    vfinal      - velocity of final orbit at b   er / tu
#    vtransa     - velocity of trans orbit at a   er / tu
#    vtransb     - velocity of trans orbit at b   er / tu
#    s           - optimization parameter
#    deltai1     - inclination change at point a  rad
#    deltai2     - inclination change at point b  rad
#
#  coupling      :
#    none.
#
#  references    :
#    vallado       2007, 352-359, ex 6-7
#function [deltai1,deltava,deltavb,gam1,gam2] = combined( rinit,rfinal,einit,efinal,deltai );
# -----------------------------------------------------------------------------

import numpy as np

def combined(rinit, rfinal, einit, efinal, deltai):
    """
    Calculate the delta v's for a combined maneuver.
    
    Args:
        rinit: initial position magnitude (er)
        rfinal: final position magnitude (er)
        einit: eccentricity of first orbit
        efinal: eccentricity of final orbit
        deltai: inclination change (rad)
        
    Returns:
        deltai1: amount of incl chg req at a (rad)
        deltava: change in velocity at point a (er/tu)
        deltavb: change in velocity at point b (er/tu)
        gam1: angle 1 (rad)
        gam2: angle 2 (rad)
    """
    # --------------------  initialize values   -------------------
    mu = 1.0  # canonical
    print(f"rinit {rinit:11.7f} {rinit:11.7f}  rfinal {rfinal:11.7f}  {rfinal:11.7f}")
    
    a1 = rinit  # assume circular orbit
    e2 = einit * einit
    if abs(e2 - 1.0) > 0.000001:
        a2 = (rinit + rfinal) / 2.0
        sme2 = -1.0 / (2.0 * a2)
    else:
        a2 = 999999.9  # undefined for parabolic orbit
        sme2 = 0.0
    
    print(f"a1 {a1:11.7f} {a1:11.7f}  e2 {e2:11.7f}")
    print(f"a2 {a2:11.7f} {a2:11.7f}")
    
    sme1 = -1.0 / (2.0 * a1)
    
    # -----------------  find delta v at point a  -----------------
    vinit = np.sqrt(2.0 * ((mu / rinit) + sme1))
    vtransa = np.sqrt(2.0 * ((mu / rinit) + sme2))
    
    # -----------------  find delta v at point b  -----------------
    vfinal = np.sqrt(mu / rfinal)
    vkmps = 7.905365719014
    print(f"vinit {vinit:11.7f} {vinit*vkmps:11.7f}  vfinal {vfinal:11.7f}  {vfinal*vkmps:11.7f}")
    
    vtransb = np.sqrt(2.0 * ((mu / rfinal) + sme2))
    
    print(f"vtransa {vtransa:11.7f} {vtransa*vkmps:11.7f}  vtransb {vtransb:11.7f}  {vtransb*vkmps:11.7f}")
    
    ratio = rfinal / rinit
    s = 1.0 / deltai * np.arctan(np.sin(deltai) / (ratio**1.5 + np.cos(deltai)))
    deltai1 = s * deltai
    deltai2 = (1.0 - s) * deltai
    
    deltava = np.sqrt(vinit**2 + vtransa**2 - 2.0 * vinit * vtransa * np.cos(deltai1))
    deltavb = np.sqrt(vfinal**2 + vtransb**2 - 2.0 * vfinal * vtransb * np.cos(deltai2))
    
    gam1 = np.arccos(-(vinit**2 + deltava**2 - vtransa**2) / (2.0 * vinit * deltava))
    gam2 = np.arccos(-(vtransb**2 + deltavb**2 - vfinal**2) / (2.0 * vtransb * deltavb))
    
    return deltai1, deltava, deltavb, gam1, gam2 