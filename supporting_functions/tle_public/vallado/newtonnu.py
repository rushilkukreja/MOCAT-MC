# ------------------------------------------------------------------------------
#
#                           function newtonnu
#
#  this function solves keplers equation when the true anomaly is known.
#    the mean and eccentric, parabolic, or hyperbolic anomaly is also found.
#    the parabolic limit at 168 is arbitrary. the hyperbolic anomaly is also
#    limited. the hyperbolic sine is used because it's not double valued.
#
#  author        : david vallado                  719-573-2600   27 may 2002
#
#  revisions
#    vallado     - fix small                                     24 sep 2002
#
#  inputs          description                    range / units
#    ecc         - eccentricity                   0.0  to
#    nu          - true anomaly                   -2pi to 2pi rad
#
#  outputs       :
#    e0          - eccentric anomaly              0.0  to 2pi rad       153.02 deg
#    m           - mean anomaly                   0.0  to 2pi rad       151.7425 deg
#
#  locals        :
#    e1          - eccentric anomaly, next value  rad
#    sine        - sine of e
#    cose        - cosine of e
#    ktr         - index
#
#  coupling      :
#    arcsinh     - arc hyperbolic sine
#    sinh        - hyperbolic sine
#
#  references    :
#    vallado       2007, 85, alg 5
#
# [e0,m] = newtonnu ( ecc,nu );
# ------------------------------------------------------------------------------

import numpy as np

def newtonnu(ecc, nu):
    """
    Solve Kepler's equation when the true anomaly is known.
    The mean and eccentric, parabolic, or hyperbolic anomaly is also found.
    The parabolic limit at 168 is arbitrary. The hyperbolic anomaly is also
    limited. The hyperbolic sine is used because it's not double valued.
    
    Args:
        ecc: eccentricity (0.0 to ...)
        nu: true anomaly (-2pi to 2pi rad)
        
    Returns:
        e0: eccentric anomaly (0.0 to 2pi rad)
        m: mean anomaly (0.0 to 2pi rad)
    """
    # ---------------------  implementation   ---------------------
    e0 = 999999.9
    m = 999999.9
    small = 0.00000001
    
    # --------------------------- circular ------------------------
    if abs(ecc) < small:
        m = nu
        e0 = nu
    else:
        # ---------------------- elliptical -----------------------
        if ecc < 1.0 - small:
            sine = (np.sqrt(1.0 - ecc * ecc) * np.sin(nu)) / (1.0 + ecc * np.cos(nu))
            cose = (ecc + np.cos(nu)) / (1.0 + ecc * np.cos(nu))
            e0 = np.arctan2(sine, cose)
            m = e0 - ecc * np.sin(e0)
        else:
            # -------------------- hyperbolic  --------------------
            if ecc > 1.0 + small:
                if (ecc > 1.0) and (abs(nu) + 0.00001 < np.pi - np.arccos(1.0 / ecc)):
                    sine = (np.sqrt(ecc * ecc - 1.0) * np.sin(nu)) / (1.0 + ecc * np.cos(nu))
                    e0 = np.arcsinh(sine)
                    m = ecc * np.sinh(e0) - e0
            else:
                # ----------------- parabolic ---------------------
                if abs(nu) < 168.0 * np.pi / 180.0:
                    e0 = np.tan(nu * 0.5)
                    m = e0 + (e0 * e0 * e0) / 3.0
    
    if ecc < 1.0:
        m = np.remainder(m, 2.0 * np.pi)
        if m < 0.0:
            m = m + 2.0 * np.pi
        e0 = np.remainder(e0, 2.0 * np.pi)
    
    return e0, m 