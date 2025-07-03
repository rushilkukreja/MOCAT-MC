# ------------------------------------------------------------------------------
#
#                           function checkhitearth
#
#  this function checks to see if the trajectory hits the earth during the
#    transfer.  the first check determines if the satellite is initially
#    heading towards perigee, and finally heading away from perigee.  if (
#    this is the case, the radius of perigee is calculated.
#
#  author        : david vallado                  719-573-2600   27 may 2002
#
#  revisions
#                -
#
#  inputs          description                    range / units
#    rint        - initial position vector of int er
#    v1t         - initial velocity vector of trnser/tu
#    rtgt        - initial position vector of tgt er
#    v2t         - final velocity vector of trns  er/tu
#
#  outputs       :
#    hitearth    - is earth was impacted          'y' 'n'
#
#  locals        :
#    sme         - specific mechanical energy
#    rp          - radius of perigee              er
#    transa      - semi-or axis of transfer       er
#    transe      - eccentricity of transfer
#    transp      - semi-paramater of transfer     er
#    hbar        - angular momentum vector of
#                  transfer orbit
#
#  coupling      :
#    dot         - dot product of vectors
#    mag         - magnitude of a vector
#    cross       - cross product of vectors
#
#  references    :
#    vallado       2001, 472-474, alg 57
#
# [hitearth] = checkhitearth ( rint,v1t,rtgt,v2t );
# ------------------------------------------------------------------------------

import numpy as np

def checkhitearth(rint, v1t, rtgt, v2t):
    """
    Check to see if the trajectory hits the earth during the transfer.
    The first check determines if the satellite is initially heading towards 
    perigee, and finally heading away from perigee. If this is the case, 
    the radius of perigee is calculated.
    
    Args:
        rint: initial position vector of int (er)
        v1t: initial velocity vector of transfer (er/tu)
        rtgt: initial position vector of target (er)
        v2t: final velocity vector of transfer (er/tu)
        
    Returns:
        hitearth: is earth was impacted ('y', 'n')
    """
    # -------------------------  implementation   -----------------
    hitearth = 'n'
    
    # ---------- find if trajectory intersects earth --------------
    if ((np.dot(rint, v1t) < 0.0) and (np.dot(rtgt, v2t) > 0.0)):
        # ---------------  find h n and e vectors   ---------------
        # TODO: Implement cross function
        # cross(rint, v1t, hbar)
        hbar = np.cross(rint, v1t)
        
        # TODO: Implement mag function
        # magh = mag(hbar)
        magh = np.linalg.norm(hbar)
        
        if magh > 0.00001:
            # ---------  find a e and semi-latus rectum   ---------
            # TODO: Fix indexing - MATLAB uses 1-based indexing
            sme = v1t[0] * v1t[0] * 0.5 - (1.0 / rint[0])
            transp = magh * magh
            transe = 1.0
            if abs(sme) > 0.00001:
                transa = -1.0 / (2.0 * sme)
                transe = np.sqrt((transa - transp) / transa)
                rp = transa * (1.0 - transe)
            else:
                rp = transp * 0.5  # parabola
            
            if abs(rp) < 1.0:
                hitearth = 'y'
        else:
            print('the orbit does not exist')
    
    return hitearth 