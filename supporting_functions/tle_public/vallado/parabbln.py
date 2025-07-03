# ------------------------------------------------------------------------------
#
#                           function parabbln
#
#  this function performs parabolic blending of an input zero crossing
#  function in order to find event times.
#
#  author        : david vallado                  719-573-2600    18 dec 2002
#
#  revisions
#                - fix eqt ref                                     3 jan 2003
#                - misc fixes                                      2 feb 2004
#
#  inputs          description                    range / units
#    p1,p2,p3    - function values used for blending
#
#  outputs       :
#    minfound    - test of success 
#    rootf       - root for the function
#    funrate     - function rate
#
#  locals        :
#
#  coupling      :
#    quadric     - find roots of a quadric
#
#  references    :
#    vallado       2007, 979
#
# [minfound,rootf,funrate] = parabbln( p1,p2,p3 );
# ------------------------------------------------------------------------------

import numpy as np

def parabbln(p1, p2, p3):
    """
    Perform parabolic blending of an input zero crossing function in order to find event times.
    
    Args:
        p1, p2, p3: function values used for blending
        
    Returns:
        minfound: test of success
        rootf: root for the function
        funrate: function rate
    """
    rootf = 0.0
    funrate = 0.0
    minfound = 'n'
    
    # ------ set up function from C-37 --------
    aqd0 = p1
    aqd1 = (-3.0 * p1 + 4.0 * p2 - p3) * 0.5
    aqd2 = (p1 - 2.0 * p2 + p3) * 0.5
    
    # --------------- solve roots of this function -------------
    opt = 'U'
    # TODO: Implement quadric function
    # [r1r, r1i, r2r, r2i] = quadric(aqd2, aqd1, aqd0, opt)
    
    # Placeholder for quadric results
    r1r = 0.0
    r1i = 0.0
    r2r = 0.0
    r2i = 0.0
    
    # ---------- search through roots to locate answers --------
    for indx2 in range(1, 3):  # 1:2 in MATLAB
        if indx2 == 1:
            root = r1r
        if indx2 == 2:
            root = r2r
        
        if (root >= 0.0) and (root <= 2.0):
            # [time] = recovqd(t1, t2, t3, root)  # should be 0.0!!!!!!
            # [ans] = recovqd(p1, p2, p3, root)  # should be 0.0!!!!!!
            
            # ----- recover the function value derivative
            funrate = 2.0 * aqd2 * root + aqd1
    
    return minfound, rootf, funrate 