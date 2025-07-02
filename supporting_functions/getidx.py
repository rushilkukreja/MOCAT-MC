"""
Index definitions for mat_sats matrix
Python version of getidx.m
Note: Python uses 0-based indexing, so all indices are shifted by -1 from MATLAB
"""

# Orbital elements and physical parameters (0-based indexing)
idx_a = 0          # semi-major axis
idx_ecco = 1       # eccentricity
idx_inclo = 2      # inclination
idx_nodeo = 3      # right ascension of ascending node
idx_argpo = 4      # argument of perigee
idx_mo = 5         # mean anomaly
idx_bstar = 6      # B* drag term
idx_mass = 7       # mass
idx_radius = 8     # radius
idx_error = 9      # error flag
idx_controlled = 10 # controlled flag
idx_a_desired = 11 # desired semi-major axis
idx_missionlife = 12 # mission lifetime
idx_constel = 13   # constellation flag
idx_date_created = 14 # date created
idx_launch_date = 15 # launch date

# Position and velocity vectors (0-based indexing)
idx_r = [16, 17, 18]  # position vector [x, y, z]
idx_v = [19, 20, 21]  # velocity vector [vx, vy, vz]

# Object classification
idx_objectclass = 22  # object class
idx_ID = 23          # object ID 