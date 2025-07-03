# ------------------------------------------------------------------------------
#
#                           function quartbln
#
#  this function performs quartic blending of an input zero crossing
#  function in order to find event times.
#
#  author        : david vallado                  719-573-2600   18 dec 2002
#
#  revisions
#                - misc fixes                                      2 feb 2004
#
#  inputs          description                    range / units
#    p1,p2,p3,p4,p5,p6
#                - function values used for blending
#
#  outputs       :
#    minfound    - test of success 
#    rootf       - root for the function
#    funrate     - function rate
#
#  locals        :
#
#  coupling      :
#    quintic     - find roots of a quintic
#
#  references    :
#    vallado       2001, 899-901
#
# [minfound,rootf,funrate] = quartbln ( p1,p2,p3,p4,p5,p6 );
# ------------------------------------------------------------------------------

import numpy as np

def quartbln(p1, p2, p3, p4, p5, p6):
    """
    Perform quartic blending of an input zero crossing function in order to find event times.
    
    Args:
        p1, p2, p3, p4, p5, p6: function values used for blending
        
    Returns:
        minfound: test of success
        rootf: root for the function
        funrate: function rate
    """
    rootf = 0.0
    funrate = 0.0
    minfound = 'n'
    
    # ------ set up function from C-45 --------
    #  aqit5*x**5 + aqit4*x**4 + etc
    temp = 1.0 / 24.0
    aqi0 = p3
    aqi1 = (2 * p1 - 16 * p2 + 16 * p4 - 2 * p5) * temp
    aqi2 = (-1 * p1 + 16 * p2 - 30 * p3 + 16 * p4 - p5) * temp
    aqi3 = (-9 * p1 + 39 * p2 - 70 * p3 + 66 * p4 - 33 * p5 + 7 * p6) * temp
    aqi4 = (13 * p1 - 64 * p2 + 126 * p3 - 124 * p4 + 61 * p5 - 12 * p6) * temp
    aqi5 = (-5 * p1 + 25 * p2 - 50 * p3 + 50 * p4 - 25 * p5 + 5 * p6) * temp
    
    # --------------- solve roots of this function -------------
    opt = 'U'
    # TODO: Implement quintic function
    # [r1r,r1i,r2r,r2i,r3r,r3i,r4r,r4i,r5r,r5i] = quintic(aqi5,aqi4,aqi3,aqi2,aqi1,aqi0,opt)
    
    # Use numpy roots instead
    coeffs = [aqi5, aqi4, aqi3, aqi2, aqi1, aqi0]
    rt = np.roots(coeffs)
    
    # ---------- search through roots to locate answers --------
    for indx2 in range(5):  # 1:5 in MATLAB
        root = 99999.9
        if (indx2 == 0) and np.isreal(rt[indx2]):
            root = rt[indx2]
        if (indx2 == 1) and np.isreal(rt[indx2]):
            root = rt[indx2]
        if (indx2 == 2) and np.isreal(rt[indx2]):
            root = rt[indx2]
        if (indx2 == 3) and np.isreal(rt[indx2]):
            root = rt[indx2]
        if (indx2 == 4) and np.isreal(rt[indx2]):
            root = rt[indx2]
        
        if (root >= 0.0) and (root <= 1.0):  # use 1 since roots gets all the roots
            minfound = 'y'
            rootf = root
            # [time] = recovqt(t1,t2,t3,t4,t5,t6, root)
            # [ans] = recovqt(p1,p2,p3,p4,p5,p6, root)  # should be 0.0!!!!!!
            
            # ----- recover the function value derivative
            funrate = (5.0 * aqi5 * root**4 + 4.0 * aqi4 * root**3 + 
                       3.0 * aqi3 * root**2 + 2.0 * aqi2 * root + aqi1)
    
    return minfound, rootf, funrate 