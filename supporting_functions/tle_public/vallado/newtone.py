# ------------------------------------------------------------------------------
#
#                           function newtone
#
#  this function solves keplers equation when the eccentric, paraboic, or
#    hyperbolic anomalies are known. the mean anomaly and true anomaly are
#    calculated.
#
#  author        : david vallado                  719-573-2600    9 jun 2002
#
#  revisions
#                -
#
#  inputs          description                    range / units
#    ecc         - eccentricity                   0.0  to
#    e0          - eccentric anomaly              -2pi to 2pi rad
#
#  outputs       :
#    m           - mean anomaly                   0.0  to 2pi rad
#    nu          - true anomaly                   0.0  to 2pi rad
#
#  locals        :
#    sinv        - sine of nu
#    cosv        - cosine of nu
#
#  coupling      :
#    sinh        - hyperbolic sine
#    cosh        - hyperbolic cosine
#
#  references    :
#    vallado       2001, 85, alg 6
#
# [m,nu] = newtone ( ecc,e0 );
# ------------------------------------------------------------------------------

import numpy as np

def newtone(ecc, e0):
    """
    Solve Kepler's equation when the eccentric, parabolic, or hyperbolic 
    anomalies are known. The mean anomaly and true anomaly are calculated.
    
    Args:
        ecc: eccentricity (0.0 to ...)
        e0: eccentric anomaly (-2pi to 2pi rad)
        
    Returns:
        m: mean anomaly (0.0 to 2pi rad)
        nu: true anomaly (0.0 to 2pi rad)
    """
    # -------------------------  implementation   -----------------
    small = 0.00000001
    
    # ------------------------- circular --------------------------
    if abs(ecc) < small:
        m = e0
        nu = e0
    else:
        # ----------------------- elliptical ----------------------
        if ecc < 0.999:
            m = e0 - ecc * np.sin(e0)
            sinv = (np.sqrt(1.0 - ecc * ecc) * np.sin(e0)) / (1.0 - ecc * np.cos(e0))
            cosv = (np.cos(e0) - ecc) / (1.0 - ecc * np.cos(e0))
            nu = np.arctan2(sinv, cosv)
        else:
            # ---------------------- hyperbolic  ------------------
            if ecc > 1.0001:
                m = ecc * np.sinh(e0) - e0
                sinv = (np.sqrt(ecc * ecc - 1.0) * np.sinh(e0)) / (1.0 - ecc * np.cosh(e0))
                cosv = (np.cosh(e0) - ecc) / (1.0 - ecc * np.cosh(e0))
                nu = np.arctan2(sinv, cosv)
            else:
                # -------------------- parabolic ------------------
                m = e0 + (1.0 / 3.0) * e0 * e0 * e0
                nu = 2.0 * np.arctan(e0)  # datan is arctan
    
    return m, nu 