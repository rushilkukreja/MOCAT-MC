import numpy as np

# ------------------------------------------------------------------------------
#
#                           function rv2coe
#
#  this function finds the classical orbital elements given the geocentric
#    equatorial position and velocity vectors.
#
#  author        : david vallado                  719-573-2600   21 jun 2002
#
#  revisions
#    vallado     - fix special cases                              5 sep 2002
#    vallado     - delete extra check in inclination code        16 oct 2002
#    vallado     - add constant file use                         29 jun 2003
#    vallado     - add mu                                         2 apr 2007
#
#  inputs          description                    range / units
#    r           - ijk position vector            km
#    v           - ijk velocity vector            km / s
#    mu          - gravitational parameter        km3 / s2
#
#  outputs       :
#    p           - semilatus rectum               km
#    a           - semimajor axis                 km
#    ecc         - eccentricity
#    incl        - inclination                    0.0  to pi rad
#    omega       - longitude of ascending node    0.0  to 2pi rad
#    argp        - argument of perigee            0.0  to 2pi rad
#    nu          - true anomaly                   0.0  to 2pi rad
#    m           - mean anomaly                   0.0  to 2pi rad
#    arglat      - argument of latitude      (ci) 0.0  to 2pi rad
#    truelon     - true longitude            (ce) 0.0  to 2pi rad
#    lonper      - longitude of periapsis    (ee) 0.0  to 2pi rad
#
#  locals        :
#    hbar        - angular momentum h vector      km2 / s
#    ebar        - eccentricity     e vector
#    nbar        - line of nodes    n vector
#    c1          - v**2 - u/r
#    rdotv       - r dot v
#    hk          - hk unit vector
#    sme         - specfic mechanical energy      km2 / s2
#    i           - index
#    e           - eccentric, parabolic,
#                  hyperbolic anomaly             rad
#    temp        - temporary variable
#    typeorbit   - type of orbit                  ee, ei, ce, ci
#
#  coupling      :
#    mag         - magnitude of a vector
#    angl        - find the angl between two vectors
#    newtonnu    - find the mean anomaly
#
#  references    :
#    vallado       2007, 121, alg 9, ex 2-5
#
# [p,a,ecc,incl,omega,argp,nu,m,arglat,truelon,lonper ] = rv2coe (r,v,mu);
# ------------------------------------------------------------------------------

def mag(vec):
    return np.linalg.norm(vec)

def angl(vec1, vec2):
    # Placeholder for angle between two vectors
    v1 = np.array(vec1)
    v2 = np.array(vec2)
    cos_ang = np.dot(v1, v2) / (mag(v1) * mag(v2))
    return np.arccos(np.clip(cos_ang, -1.0, 1.0))

def newtonnu(ecc, nu):
    # Placeholder for mean anomaly calculation
    # Returns (eccentric anomaly, mean anomaly)
    return 0.0, 0.0

def rv2coe(r, v, mu):
    small = 1e-10
    infinite = float('inf')
    undefined = None
    twopi = 2.0 * np.pi
    halfpi = 0.5 * np.pi

    r = np.array(r)
    v = np.array(v)
    magr = mag(r)
    magv = mag(v)
    hbar = np.cross(r, v)
    magh = mag(hbar)
    if magh > small:
        nbar = np.array([-hbar[1], hbar[0], 0.0])
        magn = mag(nbar)
        c1 = magv * magv - mu / magr
        rdotv = np.dot(r, v)
        ebar = (c1 * r - rdotv * v) / mu
        ecc = mag(ebar)
        sme = (magv * magv * 0.5) - (mu / magr)
        if abs(sme) > small:
            a = -mu / (2.0 * sme)
        else:
            a = infinite
        p = magh * magh / mu
        hk = hbar[2] / magh
        incl = np.arccos(hk)
        # Determine type of orbit
        typeorbit = 'ei'
        if ecc < small:
            if (incl < small) or (abs(incl - np.pi) < small):
                typeorbit = 'ce'
            else:
                typeorbit = 'ci'
        else:
            if (incl < small) or (abs(incl - np.pi) < small):
                typeorbit = 'ee'
        # Longitude of ascending node
        if magn > small:
            temp = nbar[0] / magn
            if abs(temp) > 1.0:
                temp = np.sign(temp)
            omega = np.arccos(temp)
            if nbar[1] < 0.0:
                omega = twopi - omega
        else:
            omega = undefined
        # Argument of perigee
        if typeorbit == 'ei':
            argp = angl(nbar, ebar)
            if ebar[2] < 0.0:
                argp = twopi - argp
        else:
            argp = undefined
        # True anomaly
        if typeorbit[0] == 'e':
            nu = angl(ebar, r)
            if rdotv < 0.0:
                nu = twopi - nu
        else:
            nu = undefined
        # Argument of latitude
        if typeorbit == 'ci':
            arglat = angl(nbar, r)
            if r[2] < 0.0:
                arglat = twopi - arglat
            m = arglat
        else:
            arglat = undefined
        # Longitude of periapsis
        if (ecc > small) and (typeorbit == 'ee'):
            temp = ebar[0] / ecc
            if abs(temp) > 1.0:
                temp = np.sign(temp)
            lonper = np.arccos(temp)
            if ebar[1] < 0.0:
                lonper = twopi - lonper
            if incl > halfpi:
                lonper = twopi - lonper
        else:
            lonper = undefined
        # True longitude
        if (magr > small) and (typeorbit == 'ce'):
            temp = r[0] / magr
            if abs(temp) > 1.0:
                temp = np.sign(temp)
            truelon = np.arccos(temp)
            if r[1] < 0.0:
                truelon = twopi - truelon
            if incl > halfpi:
                truelon = twopi - truelon
            m = truelon
        else:
            truelon = undefined
        # Mean anomaly
        if typeorbit[0] == 'e':
            _, m = newtonnu(ecc, nu)
        return p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper
    else:
        p = undefined
        a = undefined
        ecc = undefined
        incl = undefined
        omega = undefined
        argp = undefined
        nu = undefined
        m = undefined
        arglat = undefined
        truelon = undefined
        lonper = undefined
        return p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper 