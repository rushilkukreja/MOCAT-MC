# ------------------------------------------------------------------------------
#
#                           function pkepler
#
#  this function propagates a satellite's position and velocity vector over
#    a given time period accounting for perturbations caused by j2.
#
#  author        : david vallado                  719-573-2600    1 mar 2001
#
#  inputs          description                    range / units
#    ro          - original position vector       km
#    vo          - original velocity vector       km/sec
#    ndot        - time rate of change of n       rad/sec
#    nddot       - time accel of change of n      rad/sec2
#    dtsec       - change in time                 sec
#
#  outputs       :
#    r           - updated position vector        km
#    v           - updated velocity vector        km/sec
#
#  locals        :
#    p           - semi-paramter                  km
#    a           - semior axis                    km
#    ecc         - eccentricity
#    incl        - inclination                    rad
#    argp        - argument of periapsis          rad
#    argpdot     - change in argument of perigee  rad/sec
#    omega       - longitude of the asc node      rad
#    omegadot    - change in omega                rad
#    e0          - eccentric anomaly              rad
#    e1          - eccentric anomaly              rad
#    m           - mean anomaly                   rad/sec
#    mdot        - change in mean anomaly         rad/sec
#    arglat      - argument of latitude           rad
#    arglatdot   - change in argument of latitude rad/sec
#    truelon     - true longitude of vehicle      rad
#    truelondot  - change in the true longitude   rad/sec
#    lonper     - longitude of periapsis         rad
#    lonperodot  - longitude of periapsis change  rad/sec
#    n           - mean angular motion            rad/sec
#    nuo         - true anomaly                   rad
#    j2op2       - j2 over p sqyared
#    sinv,cosv   - sine and cosine of nu
#
#  coupling:
#    rv2coe      - orbit elements from position and velocity vectors
#    coe2rv      - position and velocity vectors from orbit elements
#    newtonm     - newton rhapson to find nu and eccentric anomaly
#
#  references    :
#    vallado       2007, 687, alg 64
#
# [r,v] = pkepler( ro,vo, dtsec, ndot,nddot );
# -----------------------------------------------------------------------------

import numpy as np

def pkepler(ro, vo, dtsec, ndot, nddot):
    """
    Propagate a satellite's position and velocity vector over a given time period 
    accounting for perturbations caused by j2.
    
    Args:
        ro: original position vector (km)
        vo: original velocity vector (km/sec)
        dtsec: change in time (sec)
        ndot: time rate of change of n (rad/sec)
        nddot: time accel of change of n (rad/sec2)
        
    Returns:
        r: updated position vector (km)
        v: updated velocity vector (km/sec)
    """
    # TODO: Import constastro constants
    # constastro
    j2 = 0.00108263
    mu = 398600.4418  # km^3/s^2 (placeholder)
    re = 6378.137  # km (placeholder)
    small = 0.000001  # placeholder
    twopi = 2.0 * np.pi  # placeholder
    
    # TODO: Implement rv2coe function
    # [p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper] = rv2coe(ro, vo)
    
    # Placeholder for rv2coe results
    p = 0.0
    a = 0.0
    ecc = 0.0
    incl = 0.0
    omega = 0.0
    argp = 0.0
    nu = 0.0
    m = 0.0
    arglat = 0.0
    truelon = 0.0
    lonper = 0.0
    
    n = np.sqrt(mu / (a * a * a))
    
    # ------------- find the value of j2 perturbations -------------
    j2op2 = (n * 1.5 * re**2 * j2) / (p * p)
    # nbar = n * (1.0 + j2op2 * np.sqrt(1.0 - ecc * ecc) * (1.0 - 1.5 * np.sin(incl) * np.sin(incl)))
    omegadot = -j2op2 * np.cos(incl)
    argpdot = j2op2 * (2.0 - 2.5 * np.sin(incl) * np.sin(incl))
    mdot = n
    
    a = a - 2.0 * ndot * dtsec * a / (3.0 * n)
    ecc = ecc - 2.0 * (1.0 - ecc) * ndot * dtsec / (3.0 * n)
    p = a * (1.0 - ecc * ecc)
    
    # ----- update the orbital elements for each orbit type --------
    if ecc < small:
        # -------------  circular equatorial  ----------------
        if (incl < small) or (abs(incl - np.pi) < small):
            truelondot = omegadot + argpdot + mdot
            truelon = truelon + truelondot * dtsec
            truelon = np.remainder(truelon, twopi)
        else:
            # -------------  circular inclined    --------------
            omega = omega + omegadot * dtsec
            omega = np.remainder(omega, twopi)
            arglatdot = argpdot + mdot
            arglat = arglat + arglatdot * dtsec
            arglat = np.remainder(arglat, twopi)
    else:
        # -- elliptical, parabolic, hyperbolic equatorial ---
        if (incl < small) or (abs(incl - np.pi) < small):
            lonperdot = omegadot + argpdot
            lonper = lonper + lonperdot * dtsec
            lonper = np.remainder(lonper, twopi)
            m = m + mdot * dtsec + ndot * dtsec * dtsec + nddot * dtsec * dtsec * dtsec
            m = np.remainder(m, twopi)
            # TODO: Implement newtonm function
            # [e0, nu] = newtonm(ecc, m)
            e0 = 0.0  # placeholder
            nu = 0.0  # placeholder
        else:
            # --- elliptical, parabolic, hyperbolic inclined --
            omega = omega + omegadot * dtsec
            omega = np.remainder(omega, twopi)
            argp = argp + argpdot * dtsec
            argp = np.remainder(argp, twopi)
            m = m + mdot * dtsec + ndot * dtsec * dtsec + nddot * dtsec * dtsec * dtsec
            m = np.mod(m, twopi)
            # TODO: Implement newtonm function
            # [e0, nu] = newtonm(ecc, m)
            e0 = 0.0  # placeholder
            nu = 0.0  # placeholder
    
    # ------------- use coe2rv to find new vectors ---------------
    # TODO: Implement coe2rv function
    # [r, v] = coe2rv(p, ecc, incl, omega, argp, nu, arglat, truelon, lonper)
    
    # Placeholder for coe2rv results
    r = np.zeros(3)  # placeholder
    v = np.zeros(3)  # placeholder
    
    r = r.T  # Transpose to match MATLAB behavior
    v = v.T  # Transpose to match MATLAB behavior
    
    return r, v 