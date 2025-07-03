# ------------------------------------------------------------------------------
#
#                           procedure mincomb
#
#  this procedure calculates the delta v's and the change in inclination
#    necessary for the minimum change in velocity when traveling between two
#    non-coplanar orbits.
#
#  author        : david vallado                  719-573-2600    1 mar 2001
#
#  inputs          description                    range / units
#    rinit       - initial position magnitude     er
#    rfinal      - final position magnitude       er
#    einit       - ecc of first orbit
#    e2          - ecc of trans orbit
#    efinal      - ecc of final orbit
#    nuinit      - true anomaly of first orbit    0 or pi rad
#    nufinal     - true anomaly of final orbit    0 or pi rad
#    iinit       - incl of the first orbit        rad
#    ifinal      - incl of the second orbit       rad
#
#  outputs       :
#    deltai1     - amount of incl chg req at a    rad
#    deltava     - change in velocity at point a  er / tu
#    deltavb     - change in velocity at point b  er / tu
#    dttu        - time of flight for the trans   tu
#    numiter     - number of iterations
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
#    e2          - eccentricity of second orbit
#
#  coupling      :
#    power       - raise a base to a power
#    asin      - arc sine routine
#
#  references    :
#    vallado       2007, 355, alg 42, table 6-3
#function [deltai,deltai1,deltava,deltavb,dttu ] = mincomb(rinit,rfinal,einit,efinal,nuinit,nufinal,iinit,ifinal);
# -----------------------------------------------------------------------------

import numpy as np

def mincomb(rinit, rfinal, einit, efinal, nuinit, nufinal, iinit, ifinal, show='n'):
    """
    Calculate the delta v's and the change in inclination necessary for 
    the minimum change in velocity when traveling between two non-coplanar orbits.
    
    Args:
        rinit: initial position magnitude (er)
        rfinal: final position magnitude (er)
        einit: eccentricity of first orbit
        efinal: eccentricity of final orbit
        nuinit: true anomaly of first orbit (0 or pi rad)
        nufinal: true anomaly of final orbit (0 or pi rad)
        iinit: inclination of the first orbit (rad)
        ifinal: inclination of the second orbit (rad)
        show: show output flag ('y', 'n')
        
    Returns:
        deltai: total inclination change (rad)
        deltai1: amount of incl chg req at a (rad)
        deltava: change in velocity at point a (er/tu)
        deltavb: change in velocity at point b (er/tu)
        dttu: time of flight for the transfer (tu)
    """
    rad = 57.29577951308230
    
    # --------------------  initialize values   --------------------
    a1 = (rinit * (1.0 + einit * np.cos(nuinit))) / (1.0 - einit * einit)
    a2 = 0.5 * (rinit + rfinal)
    a3 = (rfinal * (1.0 + efinal * np.cos(nufinal))) / (1.0 - efinal * efinal)
    sme1 = -1.0 / (2.0 * a1)
    sme2 = -1.0 / (2.0 * a2)
    sme3 = -1.0 / (2.0 * a3)
    
    # ----------- find velocities --------
    vinit = np.sqrt(2.0 * ((1.0 / rinit) + sme1))
    v1t = np.sqrt(2.0 * ((1.0 / rinit) + sme2))
    
    vfinal = np.sqrt(2.0 * ((1.0 / rfinal) + sme3))
    v3t = np.sqrt(2.0 * ((1.0 / rfinal) + sme2))
    
    # ----------- find the optimum change of inclination -----------
    tdi = ifinal - iinit
    
    temp = (1.0 / tdi) * np.arctan((np.power(rfinal / rinit, 1.5) - np.cos(tdi)) / np.sin(tdi))
    temp = (1.0 / tdi) * np.arctan(np.sin(tdi) / (np.power(rfinal / rinit, 1.5) + np.cos(tdi)))
    
    deltava = np.sqrt(v1t * v1t + vinit * vinit - 2.0 * v1t * vinit * np.cos(temp * tdi))
    deltavb = np.sqrt(v3t * v3t + vfinal * vfinal - 2.0 * v3t * vfinal * np.cos(tdi * (1.0 - temp)))
    
    deltai = temp * tdi
    deltai1 = tdi * (1.0 - temp)
    
    # ----------------  find transfer time of flight  --------------
    dttu = np.pi * np.sqrt(a2 * a2 * a2)
    
    if show == 'y':
        dvold = abs(v1t - vinit) + np.sqrt(v3t * v3t + vfinal * vfinal - 2.0 * v3t * vfinal * np.cos(tdi))
        print(f"temp = {temp:11.7f} this uses di in rad")
        print(f"rinit {rinit:14.7f} {rinit*6378.137:14.7f} rfinal {rfinal:14.7f} {rfinal*6378.137:14.7f}")
        print(f"deltai1 {deltai*rad:13.7f} {deltai1*rad:13.7f}")
        print(f"deltava {deltava:13.7f} deltavb {deltavb:13.7f} er/tu")
        print(f"deltava {deltava*7.905365998:13.7f} deltavb {deltavb*7.905365998:13.7f} km/s")
        print(f"{1000*(deltava+deltavb)*7.905365998:13.7f} m/s")
        print(f"dv old way {1000*dvold*7.905365998:13.7f} m/s")
        print(f"dttu {dttu*13.446851158:13.7f} min")
    
    # ----- iterate to find the optimum change of inclination -----
    deltainew = deltai  # 1st guess, 0.01 to 0.025 seems good
    deltai1 = 100.0  # if going to smaller orbit, should be 1.0 - 0.025!
    numiter = 0  # 1.0 - 0.025!
    
    while abs(deltainew - deltai1) > 0.000001:
        deltai1 = deltainew
        deltava = np.sqrt(v1t * v1t + vinit * vinit - 2.0 * v1t * vinit * np.cos(deltai1))
        
        deltavb = np.sqrt(v3t * v3t + vfinal * vfinal - 2.0 * v3t * vfinal * np.cos(tdi - deltai1))
        
        deltainew = np.arcsin((deltava * vfinal * v3t * np.sin(tdi - deltai1)) / (vinit * v1t * deltavb))
        numiter += 1
    
    if show == 'y':
        print(f"iter di {deltai1*rad:14.6f}° {numiter:3d} {(deltava+deltavb)*7905.365998:13.7f}")
    
    return deltai, deltai1, deltava, deltavb, dttu 