"""
Position/Velocity to Orbital Elements Conversion
Converts Cartesian position and velocity vectors to classical orbital elements
"""

import numpy as np

def rv2coe_vec(r, v, mu):
    """
    Convert position and velocity vectors to orbital elements
    
    Parameters:
    -----------
    r : array-like
        Position vectors [x, y, z] in km
    v : array-like
        Velocity vectors [vx, vy, vz] in km/s
    mu : float
        Gravitational parameter in km³/s²
        
    Returns:
    --------
    tuple : (p, a, e, i, omega, argp, nu, m, arglat, truelon, lonper)
        p : semi-parameter (km)
        a : semi-major axis (km)
        e : eccentricity
        i : inclination (rad)
        omega : right ascension of ascending node (rad)
        argp : argument of perigee (rad)
        nu : true anomaly (rad)
        m : mean anomaly (rad)
        arglat : argument of latitude (rad)
        truelon : true longitude (rad)
        lonper : longitude of perigee (rad)
    """
    
    r = np.array(r)
    v = np.array(v)
    
    # Handle single vector case
    if r.ndim == 1:
        r = r.reshape(1, -1)
        v = v.reshape(1, -1)
    
    n_objects = r.shape[0]
    
    # Initialize output arrays
    p = np.zeros(n_objects)
    a = np.zeros(n_objects)
    e = np.zeros(n_objects)
    i = np.zeros(n_objects)
    omega = np.zeros(n_objects)
    argp = np.zeros(n_objects)
    nu = np.zeros(n_objects)
    m = np.zeros(n_objects)
    arglat = np.zeros(n_objects)
    truelon = np.zeros(n_objects)
    lonper = np.zeros(n_objects)
    
    for k in range(n_objects):
        r_vec = r[k, :]
        v_vec = v[k, :]
        
        # Magnitudes
        r_mag = np.linalg.norm(r_vec)
        v_mag = np.linalg.norm(v_vec)
        
        # Angular momentum vector
        h_vec = np.cross(r_vec, v_vec)
        h_mag = np.linalg.norm(h_vec)
        
        # Eccentricity vector
        e_vec = np.cross(v_vec, h_vec) / mu - r_vec / r_mag
        e_mag = np.linalg.norm(e_vec)
        
        # Semi-parameter
        p[k] = h_mag**2 / mu
        
        # Semi-major axis
        energy = v_mag**2 / 2 - mu / r_mag
        if abs(energy) < 1e-10:  # Parabolic
            a[k] = np.inf
        else:
            a[k] = -mu / (2 * energy)
        
        # Eccentricity
        e[k] = e_mag
        
        # Inclination
        i[k] = np.arccos(np.clip(h_vec[2] / h_mag, -1, 1))
        
        # Node vector
        n_vec = np.cross([0, 0, 1], h_vec)
        n_mag = np.linalg.norm(n_vec)
        
        # Right ascension of ascending node
        if n_mag > 1e-10:
            omega[k] = np.arccos(np.clip(n_vec[0] / n_mag, -1, 1))
            if n_vec[1] < 0:
                omega[k] = 2 * np.pi - omega[k]
        else:
            omega[k] = 0
        
        # Argument of perigee
        if n_mag > 1e-10 and e_mag > 1e-10:
            argp[k] = np.arccos(np.clip(np.dot(n_vec, e_vec) / (n_mag * e_mag), -1, 1))
            if e_vec[2] < 0:
                argp[k] = 2 * np.pi - argp[k]
        else:
            argp[k] = 0
        
        # True anomaly
        if e_mag > 1e-10:
            nu[k] = np.arccos(np.clip(np.dot(e_vec, r_vec) / (e_mag * r_mag), -1, 1))
            if np.dot(r_vec, v_vec) < 0:
                nu[k] = 2 * np.pi - nu[k]
        else:
            # Circular orbit
            nu[k] = np.arccos(np.clip(r_vec[0] / r_mag, -1, 1))
            if r_vec[1] < 0:
                nu[k] = 2 * np.pi - nu[k]
        
        # Mean anomaly (Kepler's equation)
        if e_mag < 1e-10:  # Circular
            m[k] = nu[k]
        elif e_mag < 1:  # Elliptical
            E = 2 * np.arctan(np.sqrt((1 - e_mag) / (1 + e_mag)) * np.tan(nu[k] / 2))
            m[k] = E - e_mag * np.sin(E)
        else:  # Hyperbolic
            H = 2 * np.arctanh(np.sqrt((e_mag - 1) / (e_mag + 1)) * np.tan(nu[k] / 2))
            m[k] = e_mag * np.sinh(H) - H
        
        # Argument of latitude
        arglat[k] = argp[k] + nu[k]
        
        # True longitude
        truelon[k] = omega[k] + argp[k] + nu[k]
        
        # Longitude of perigee
        lonper[k] = omega[k] + argp[k]
    
    return p, a, e, i, omega, argp, nu, m, arglat, truelon, lonper 