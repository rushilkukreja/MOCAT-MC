# ------------------------------------------------------------------------------
#
#                           procedure onetang
#
#  this procedure calculates the delta v's for a one tangent transfer for either
#    circle to circle, or ellipse to ellipse.
#
#  author        : david vallado                  719-573-2600    1 mar 2001
#
#  inputs          description                    range / units
#    rinit       - initial position magnitude     er
#    rfinal      - final position magnitude       er
#    einit       - eccentricity of first orbit
#    efinal      - eccentricity of final orbit
#    nuinit      - true anomaly of first orbit    0 or pi rad
#    nu2         - true anomaly of second orbit   same quad as nuinit, rad
#    nufinal     - true anomaly of final orbit    0 or pi rad
#
#  outputs       :
#    deltava     - change in velocity at point a  er / tu
#    deltavb     - change in velocity at point b  er / tu
#    dttu        - time of flight for the transf  tu
#
#  locals        :
#    sme1        - mech energy of first orbit     er2 / tu
#    sme2        - mech energy of transfer orbit  er2 / tu
#    sme3        - mech energy of final orbit     er2 / tu
#    vinit       - velocity of first orbit at a   er / tu
#    vtransa     - velocity of trans orbit at a   er / tu
#    vtransb     - velocity of trans orbit at b   er / tu
#    vfinal      - velocity of final orbit at b   er / tu
#    ainit       - semimajor axis of first orbit  er
#    atrans      - semimajor axis of trans orbit  er
#    afinal      - semimajor axis of final orbit  er
#    e           - ecc anomaly of trans at b      rad
#    ratio       - ratio of initial to final
#                    orbit radii
#
#  coupling      :
#    atan2       - arc tangent rountine that solves quadrant ambiguities
#
#  references    :
#    vallado       2007, 335, alg 38, ex 6-3
#function [deltava,deltavb,dttu ] = onetang(rinit,rfinal,einit,efinal,nuinit,nutran);
# -----------------------------------------------------------------------------

import numpy as np

def onetang(rinit, rfinal, einit, efinal, nuinit, nutran):
    """
    Calculate the delta v's for a one tangent transfer for either circle to circle, 
    or ellipse to ellipse.
    
    Args:
        rinit: initial position magnitude (er)
        rfinal: final position magnitude (er)
        einit: eccentricity of first orbit
        efinal: eccentricity of final orbit
        nuinit: true anomaly of first orbit (0 or pi rad)
        nutran: true anomaly of second orbit (same quad as nuinit, rad)
        
    Returns:
        deltava: change in velocity at point a (er / tu)
        deltavb: change in velocity at point b (er / tu)
        dttu: time of flight for the transfer (tu)
    """
    # --------------------  initialize values   -------------------
    mu = 1.0  # cannonical units
    
    deltava = 0.0
    deltavb = 0.0
    dttu = 0.0
    ratio = rinit / rfinal
    
    if abs(nuinit) < 0.01:  # check 0 or 180
        etran = (ratio - 1.0) / (np.cos(nutran) - ratio)  # init at perigee
        eainit = 0.0
    else:
        etran = (ratio - 1.0) / (np.cos(nutran) + ratio)  # init at apogee
        eainit = np.pi
    
    if etran >= 0.0:
        ainit = (rinit * (1.0 + einit * np.cos(nuinit))) / (1.0 - einit * einit)
        afinal = (rfinal * (1.0 + efinal * np.cos(nutran))) / (1.0 - efinal * efinal)
        # nutran is used since it = nufinal!!
        ainit = rinit
        afinal = rfinal
        
        if abs(etran - 1.0) > 0.000001:
            if abs(nuinit) < 0.01:  # check 0 or 180
                atran = (rinit * (1.0 + etran * np.cos(nuinit))) / (1.0 - etran * etran)  # per
            else:
                # atran = (rinit * (1.0 + etran * np.cos(nuinit))) / (1.0 + etran * etran)  # apo
                atran = rinit / (1.0 + etran)
        else:
            atran = 999999.9  # infinite for parabolic orbit
        
        # -----------------  find delta v at point a  -----------------
        vinit = np.sqrt((2.0 * mu) / rinit - (mu / ainit))
        vtrana = np.sqrt((2.0 * mu) / rinit - (mu / atran))
        deltava = abs(vtrana - vinit)
        
        # -----------------  find delta v at point b  -----------------
        vfinal = np.sqrt((2.0 * mu) / rfinal - (mu / afinal))
        vtranb = np.sqrt((2.0 * mu) / rfinal - (mu / atran))
        fpatranb = np.arctan((etran * np.sin(nutran)) / (1.0 + etran * np.cos(nutran)))
        fpafinal = np.arctan((efinal * np.sin(nutran)) / (1.0 + efinal * np.cos(nutran)))
        deltavb = np.sqrt(vtranb * vtranb + vfinal * vfinal - 
                         2.0 * vtranb * vfinal * np.cos(fpatranb - fpafinal))
        
        # ----------------  find transfer time of flight  -------------
        if etran < 0.99999:
            sinv = (np.sqrt(1.0 - etran * etran) * np.sin(nutran)) / (1.0 + etran * np.cos(nutran))
            cosv = (etran + np.cos(nutran)) / (1.0 + etran * np.cos(nutran))
            e = np.arctan2(sinv, cosv)
            dttu = np.sqrt((atran * atran * atran) / mu) * (e - etran * np.sin(e) - (eainit - etran * np.sin(eainit)))
        else:
            if abs(etran - 1.0) < 0.000001:
                # parabolic dttu
                pass
            else:
                # hyperbolic dttu
                pass
    else:
        print('the one tangent burn is not possible for this case')
    
    return deltava, deltavb, dttu 