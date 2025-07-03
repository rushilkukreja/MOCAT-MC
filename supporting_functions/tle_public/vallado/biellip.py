# ------------------------------------------------------------------------------
#
#                           procedure biellip 
#
#  this procedure calculates the delta v's for a bi-elliptic transfer for either
#    circle to circle, or ellipse to ellipse.
#
#  author        : david vallado                  719-573-2600    1 mar 2001
#
#  inputs          description                    range / units
#    rinit       - initial position magnitude     er
#    r2          - interim orbit magnitude        er
#    rfinal      - final position magnitude       er
#    einit       - eccentricity of first orbit
#    efinal      - eccentricity of final orbit
#    nuinit      - true anomaly of first orbit    0 or pi rad
#    nufinal     - true anomaly of final orbit    0 or pi rad, opp of nuinit
#
#  outputs       :
#    deltava     - change in velocity at point a  er / tu
#    deltavb     - change in velocity at point b  er / tu
#    dttu        - time of flight for the trans   tu
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
#
#  coupling      :
#    none.
#
#  references    :
#    vallado       2007, 327, alg 37, ex 6-2
#function [deltava,deltavb,deltavc,dttu ] = biellip(rinit,rb,rfinal,einit,efinal,nuinit,nufinal);
# -----------------------------------------------------------------------------

import numpy as np

def biellip(rinit, rb, rfinal, einit, efinal, nuinit, nufinal):
    """
    Calculate the delta v's for a bi-elliptic transfer for either
    circle to circle, or ellipse to ellipse.
    
    Args:
        rinit: initial position magnitude (er)
        rb: interim orbit magnitude (er)
        rfinal: final position magnitude (er)
        einit: eccentricity of first orbit
        efinal: eccentricity of final orbit
        nuinit: true anomaly of first orbit (0 or pi rad)
        nufinal: true anomaly of final orbit (0 or pi rad, opp of nuinit)
        
    Returns:
        deltava: change in velocity at point a (er/tu)
        deltavb: change in velocity at point b (er/tu)
        deltavc: change in velocity at point c (er/tu)
        dttu: time of flight for the transfer (tu)
    """
    # --------------------  initialize values   -------------------
    mu = 1.0  # canonical units
    
    ainit = (rinit * (1.0 + einit * np.cos(nuinit))) / (1.0 - einit * einit)
    atran1 = (rinit + rb) * 0.5
    atran2 = (rb + rfinal) * 0.5
    afinal = (rfinal * (1.0 + efinal * np.cos(nufinal))) / (1.0 - efinal * efinal)
    
    deltava = 0.0
    deltavb = 0.0
    deltavc = 0.0
    dttu = 0.0
    
    if (einit < 1.0) and (efinal < 1.0):
        # -----------------  find delta v at point a  -----------------
        vinit = np.sqrt((2.0 * mu) / rinit - (mu / ainit))
        vtran1a = np.sqrt((2.0 * mu) / rinit - (mu / atran1))
        deltava = abs(vtran1a - vinit)
        
        # -----------------  find delta v at point b  -----------------
        vtran1b = np.sqrt((2.0 * mu) / rb - (mu / atran1))
        vtran2b = np.sqrt((2.0 * mu) / rb - (mu / atran2))
        deltavb = abs(vtran1b - vtran2b)
        
        # -----------------  find delta v at point c  -----------------
        vtran2c = np.sqrt((2.0 * mu) / rfinal - (mu / atran2))
        vfinal = np.sqrt((2.0 * mu) / rfinal - (mu / afinal))
        deltavc = abs(vfinal - vtran2c)
        
        # ----------------  find transfer time of flight  -------------
        dttu = (np.pi * np.sqrt((atran1 * atran1 * atran1) / mu) + 
                np.pi * np.sqrt((atran2 * atran2 * atran2) / mu))
    
    return deltava, deltavb, deltavc, dttu 