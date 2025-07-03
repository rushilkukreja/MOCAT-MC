# ------------------------------------------------------------------------------
#
#                           function newtonm
#
#  this function performs the newton rhapson iteration to find the
#    eccentric anomaly given the mean anomaly.  the true anomaly is also
#    calculated.
#
#  author        : david vallado                  719-573-2600    9 jun 2002
#
#  revisions
#                -
#
#  inputs          description                    range / units
#    ecc         - eccentricity                   0.0  to
#    m           - mean anomaly                   -2pi to 2pi rad
#
#  outputs       :
#    e0          - eccentric anomaly              0.0  to 2pi rad
#    nu          - true anomaly                   0.0  to 2pi rad
#
#  locals        :
#    e1          - eccentric anomaly, next value  rad
#    sinv        - sine of nu
#    cosv        - cosine of nu
#    ktr         - index
#    r1r         - cubic roots - 1 to 3
#    r1i         - imaginary component
#    r2r         -
#    r2i         -
#    r3r         -
#    r3i         -
#    s           - variables for parabolic solution
#    w           - variables for parabolic solution
#
#  coupling      :
#    cubic       - solves a cubic polynomial
#
#  references    :
#    vallado       2001, 72-75, alg 2, ex 2-1
#
# [e0,nu] = newtonm ( ecc,m );
# ------------------------------------------------------------------------------

import numpy as np

def newtonm(ecc, m):
    """
    Perform the Newton-Raphson iteration to find the eccentric anomaly 
    given the mean anomaly. The true anomaly is also calculated.
    
    Args:
        ecc: eccentricity (0.0 to ...)
        m: mean anomaly (-2pi to 2pi rad)
        
    Returns:
        e0: eccentric anomaly (0.0 to 2pi rad)
        nu: true anomaly (0.0 to 2pi rad)
    """
    # -------------------------  implementation   -----------------
    numiter = 50
    small = 0.00000001
    halfpi = np.pi * 0.5
    
    # -------------------------- hyperbolic  ----------------------
    if (ecc - 1.0) > small:
        # -------------------  initial guess -----------------------
        if ecc < 1.6:
            if ((m < 0.0) and (m > -np.pi)) or (m > np.pi):
                e0 = m - ecc
            else:
                e0 = m + ecc
        else:
            if (ecc < 3.6) and (abs(m) > np.pi):
                e0 = m - np.sign(m) * ecc
            else:
                e0 = m / (ecc - 1.0)
        
        ktr = 1
        e1 = e0 + ((m - ecc * np.sinh(e0) + e0) / (ecc * np.cosh(e0) - 1.0))
        while (abs(e1 - e0) > small) and (ktr <= numiter):
            e0 = e1
            e1 = e0 + ((m - ecc * np.sinh(e0) + e0) / (ecc * np.cosh(e0) - 1.0))
            ktr = ktr + 1
        
        # ----------------  find true anomaly  --------------------
        sinv = -(np.sqrt(ecc * ecc - 1.0) * np.sinh(e1)) / (1.0 - ecc * np.cosh(e1))
        cosv = (np.cosh(e1) - ecc) / (1.0 - ecc * np.cosh(e1))
        nu = np.arctan2(sinv, cosv)
    else:
        # --------------------- parabolic -------------------------
        if abs(ecc - 1.0) < small:
            # TODO: Implement cubic function
            # c = [1.0/3.0; 0.0; 1.0; -m]
            # [r1r] = roots(c)
            # e0 = r1r
            
            s = 0.5 * (halfpi - np.arctan(1.5 * m))
            w = np.arctan(np.tan(s)**(1.0 / 3.0))
            e0 = 2.0 * (1.0 / np.tan(2.0 * w))  # cot function
            ktr = 1
            nu = 2.0 * np.arctan(e0)
        else:
            # -------------------- elliptical ----------------------
            if ecc > small:
                # -----------  initial guess -------------
                if ((m < 0.0) and (m > -np.pi)) or (m > np.pi):
                    e0 = m - ecc
                else:
                    e0 = m + ecc
                
                ktr = 1
                e1 = e0 + (m - e0 + ecc * np.sin(e0)) / (1.0 - ecc * np.cos(e0))
                while (abs(e1 - e0) > small) and (ktr <= numiter):
                    ktr = ktr + 1
                    e0 = e1
                    e1 = e0 + (m - e0 + ecc * np.sin(e0)) / (1.0 - ecc * np.cos(e0))
                
                # -------------  find true anomaly  ---------------
                sinv = (np.sqrt(1.0 - ecc * ecc) * np.sin(e1)) / (1.0 - ecc * np.cos(e1))
                cosv = (np.cos(e1) - ecc) / (1.0 - ecc * np.cos(e1))
                nu = np.arctan2(sinv, cosv)
            else:
                # -------------------- circular -------------------
                ktr = 0
                nu = m
                e0 = m
    
    return e0, nu 