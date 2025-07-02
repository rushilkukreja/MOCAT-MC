"""
Create TLE objects from fragment data
Converts fragment information to satellite matrix format
"""

import numpy as np
from rv2coe_vec import rv2coe_vec
from filter_objclass_fragments_int import filter_objclass_fragments_int

def func_create_tlesv2_vec(ep, r_parent, v_parent, class_parent, fragments, max_frag, mu, req, maxID):
    """
    Create new satellite objects from fragmentation information
    
    Parameters:
    -----------
    ep : float
        Epoch
    r_parent : array-like
        Parent position vector [x, y, z]
    v_parent : array-like
        Parent velocity vector [vx, vy, vz]
    class_parent : int
        Parent object class
    fragments : array-like
        Nx8 fragment data: [diam, Area, AMR, m, total_dv, dv_X, dv_Y, dv_Z]
    max_frag : int
        Maximum number of fragments
    mu : float
        Gravitational parameter
    req : float
        Earth radius
    maxID : int
        Maximum object ID
        
    Returns:
    --------
    mat_frag : array-like
        Fragment matrix in satellite format
    """
    
    r0 = np.array(r_parent)
    v0 = np.array(v_parent)
    
    if len(fragments) > max_frag:
        print(f'Warning: number of fragments {len(fragments)} exceeds max_frag {max_frag}')
    
    n_frag = min(len(fragments), max_frag)
    
    if n_frag == 0:
        return np.array([])
    
    # Sort by mass to minimize mass conservation issues
    mass_idx = np.argsort(fragments[:, 3])[::-1]  # Sort by mass (descending)
    fragments = fragments[mass_idx[:n_frag]]
    
    # Add velocity changes to parent velocity
    v = fragments[:, 5:8] + v0  # Add dV components
    r = np.tile(r0, (n_frag, 1))  # Repeat parent position
    
    # Convert to orbital elements
    try:
        _, a, ecc, incl, omega, argp, _, m, _, _, _ = rv2coe_vec(r, v, mu)
    except:
        # If conversion fails, return empty array
        return np.array([])
    
    # Filter for elliptical orbits (a > 0)
    idx_a = np.where(a > 0)[0]
    num_a = len(idx_a)
    
    if num_a == 0:
        return np.array([])
    
    # Extract valid orbital elements
    a = a[idx_a] / req  # Convert to Earth radii
    ecco = ecc[idx_a]
    inclo = incl[idx_a]
    nodeo = omega[idx_a]
    argpo = argp[idx_a]
    mo = m[idx_a]
    
    # Calculate Bstar parameter
    rho_0 = 0.157  # kg/(m²*Re)
    A_M = fragments[idx_a, 2]  # Area-to-mass ratio
    bstar = (0.5 * 2.2 * rho_0) * A_M  # Bstar in 1/re
    
    # Physical properties
    mass = fragments[idx_a, 3]
    radius = fragments[idx_a, 0] / 2  # Diameter to radius
    
    # Initialize other parameters
    errors = np.zeros(num_a)
    controlled = np.zeros(num_a)
    a_desired = np.full(num_a, np.nan)
    missionlife = np.full(num_a, np.nan)
    constel = np.zeros(num_a)
    date_created = np.full(num_a, ep)
    launch_date = np.full(num_a, np.nan)
    
    # Assign fragment object class
    frag_objectclass = np.full(num_a, filter_objclass_fragments_int(class_parent))
    
    # Generate fragment IDs
    ID_frag = np.arange(maxID + 1, maxID + num_a + 1)
    
    # Create fragment matrix
    mat_frag = np.column_stack([
        a, ecco, inclo, nodeo, argpo, mo, bstar, mass, radius,
        errors, controlled, a_desired, missionlife, constel,
        date_created, launch_date, r[idx_a], v[idx_a], frag_objectclass, ID_frag
    ])
    
    return mat_frag 