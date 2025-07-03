import numpy as np

def anglesg(decl1, decl2, decl3, rtasc1, rtasc2, rtasc3, jd1, jd2, jd3, rs1, rs2, rs3):
    """
    This function solves the problem of orbit determination using three
    optical sightings. The solution function uses the gaussian technique.
    There are lots of debug statements in here to test various options.
    
    Author: David Vallado 719-573-2600 1 mar 2001
    23 dec 2003
    8 oct 2007
    
    Inputs:
        rtasc1 - right ascension #1 (rad)
        rtasc2 - right ascension #2 (rad)
        rtasc3 - right ascension #3 (rad)
        decl1 - declination #1 (rad)
        decl2 - declination #2 (rad)
        decl3 - declination #3 (rad)
        jd1 - julian date of 1st sighting (days from 4713 bc)
        jd2 - julian date of 2nd sighting (days from 4713 bc)
        jd3 - julian date of 3rd sighting (days from 4713 bc)
        rs1, rs2, rs3 - ijk site position vectors (km)
    
    Outputs:
        r2 - ijk position vector at t2 (km)
        v2 - ijk velocity vector at t2 (km/s)
    
    References:
        Vallado 2007, 429-439
    """
    def mag(vec):
        return np.linalg.norm(vec)
    
    def dot(vec1, vec2):
        return np.dot(vec1, vec2)
    
    def det(mat):
        return np.linalg.det(mat)
    
    def roots(poly):
        # Placeholder for roots function
        return np.roots(poly)
    
    def gibbs(r1, r2, r3):
        # Placeholder for gibbs function
        return None, None, None, None, 'ok'
    
    def hgibbs(r1, r2, r3, jd1, jd2, jd3):
        # Placeholder for hgibbs function
        return None, None, None, None, 'ok'
    
    def rv2coe(r, v):
        # Placeholder for rv2coe function
        return None, None, None, None, None, None, None, None, None, None, None
    
    def angl(vec1, vec2):
        # Placeholder for angl function
        return np.arccos(dot(vec1, vec2) / (mag(vec1) * mag(vec2)))
    
    # Constants
    mu = 3.986004418e5
    rad = 57.29577951308230
    
    ddpsi = 0.0
    ddeps = 0.0
    magr1in = 2.0 * 6378.137
    magr2in = 2.01 * 6378.137
    direct = 'y'
    
    # Set middle to 0, find decls to others
    tau1 = (jd1 - jd2) * 86400.0
    tau3 = (jd3 - jd2) * 86400.0
    print(f'jd123 {jd1:14.6f} {jd2:14.6f} {jd3:14.6f} tau {tau1:11.7f}  {tau3:11.7f}')
    
    # Find line of sight vectors
    l1 = np.array([np.cos(decl1) * np.cos(rtasc1), np.cos(decl1) * np.sin(rtasc1), np.sin(decl1)])
    l2 = np.array([np.cos(decl2) * np.cos(rtasc2), np.cos(decl2) * np.sin(rtasc2), np.sin(decl2)])
    l3 = np.array([np.cos(decl3) * np.cos(rtasc3), np.cos(decl3) * np.sin(rtasc3), np.sin(decl3)])
    
    # Leave these as they come since the topoc radec are already eci
    l1eci = l1
    l2eci = l2
    l3eci = l3
    
    # Called lmati since it is only used for determ
    lmatii = np.zeros((3, 3))
    rsmat = np.zeros((3, 3))
    
    for i in range(3):
        lmatii[i, 0] = l1eci[i]
        lmatii[i, 1] = l2eci[i]
        lmatii[i, 2] = l3eci[i]
        rsmat[i, 0] = rs1[i]
        rsmat[i, 1] = rs2[i]
        rsmat[i, 2] = rs3[i]
    
    print(f'rsmat eci {rsmat[0,0]:11.7f}  {rsmat[1,0]:11.7f}  {rsmat[2,0]:11.7f}')
    print(f'rsmat eci {rsmat[0,0]/6378.137:11.7f}  {rsmat[1,0]/6378.137:11.7f}  {rsmat[2,0]/6378.137:11.7f}')
    
    print('this should be the inverse of what the code finds later')
    li = np.linalg.inv(lmatii)
    d = det(lmatii)
    
    # Now assign the inverse
    lmati = np.zeros((3, 3))
    lmati[0, 0] = (l2eci[1] * l3eci[2] - l2eci[2] * l3eci[1]) / d
    lmati[1, 0] = (-l1eci[1] * l3eci[2] + l1eci[2] * l3eci[1]) / d
    lmati[2, 0] = (l1eci[1] * l2eci[2] - l1eci[2] * l2eci[1]) / d
    lmati[0, 1] = (-l2eci[0] * l3eci[2] + l2eci[2] * l3eci[0]) / d
    lmati[1, 1] = (l1eci[0] * l3eci[2] - l1eci[2] * l3eci[0]) / d
    lmati[2, 1] = (-l1eci[0] * l2eci[2] + l1eci[2] * l2eci[0]) / d
    lmati[0, 2] = (l2eci[0] * l3eci[1] - l2eci[1] * l3eci[0]) / d
    lmati[1, 2] = (-l1eci[0] * l3eci[1] + l1eci[1] * l3eci[0]) / d
    lmati[2, 2] = (l1eci[0] * l2eci[1] - l1eci[1] * l2eci[0]) / d
    
    lir = lmati @ rsmat
    
    # Find f and g series at 1st and 3rd obs
    # Speed by assuming circ sat vel for udot here ??
    # Some similarities in 1/6t3t1 ...
    # Keep separated this time
    a1 = tau3 / (tau3 - tau1)
    a1u = (tau3 * ((tau3 - tau1)**2 - tau3 * tau3)) / (6.0 * (tau3 - tau1))
    a3 = -tau1 / (tau3 - tau1)
    a3u = -(tau1 * ((tau3 - tau1)**2 - tau1 * tau1)) / (6.0 * (tau3 - tau1))
    
    print(f'a1/a3 {a1:11.7f}  {a1u:11.7f}  {a3:11.7f}  {a3u:11.7f}')
    
    # Form initial guess of r2
    decl1 = lir[1, 0] * a1 - lir[1, 1] + lir[1, 2] * a3
    decl2 = lir[1, 0] * a1u + lir[1, 2] * a3u
    
    # Solve eighth order poly not same as laplace
    magrs2 = mag(rs2)
    l2dotrs = dot(l2, rs2)
    print(f'magrs2 {magrs2:11.7f}  {l2dotrs:11.7f}')
    
    poly = np.zeros(9)
    poly[0] = 1.0  # r2^8th variable
    poly[1] = 0.0
    poly[2] = -(decl1 * decl1 + 2.0 * decl1 * l2dotrs + magrs2**2)
    poly[3] = 0.0
    poly[4] = 0.0
    poly[5] = -2.0 * mu * (l2dotrs * decl2 + decl1 * decl2)
    poly[6] = 0.0
    poly[7] = 0.0
    poly[8] = -mu * mu * decl2 * decl2
    
    print(f'{poly[0]:11.7f}')
    rootarr = roots(poly)
    
    # Select the correct root
    bigr2 = -99999990.0
    # Change from 1
    for j in range(8):
        if (rootarr[j] > bigr2) and (np.isreal(rootarr[j])):
            bigr2 = rootarr[j]
    
    # Solve matrix with u2 better known
    u = mu / (bigr2 * bigr2 * bigr2)
    
    c1 = a1 + a1u * u
    c2 = -1.0
    c3 = a3 + a3u * u
    
    print(f'u {u:17.14f} c1 {c1:11.7f} c3 {c3:11.7f} {c2:11.7f}')
    
    cmat = np.zeros((3, 1))
    cmat[0, 0] = -c1
    cmat[1, 0] = -c2
    cmat[2, 0] = -c3
    rhomat = lir @ cmat
    
    rhoold1 = rhomat[0, 0] / c1
    rhoold2 = rhomat[1, 0] / c2
    rhoold3 = rhomat[2, 0] / c3
    print(f'rhoold {rhoold1:11.7f} {rhoold2:11.7f} {rhoold3:11.7f}')
    
    r1 = np.zeros(3)
    r2 = np.zeros(3)
    r3 = np.zeros(3)
    
    for i in range(3):
        r1[i] = rhomat[0, 0] * l1eci[i] / c1 + rs1[i]
        r2[i] = rhomat[1, 0] * l2eci[i] / c2 + rs2[i]
        r3[i] = rhomat[2, 0] * l3eci[i] / c3 + rs3[i]
    
    print(f'r1 {r1[0]:11.7f} {r1[1]:11.7f} {r1[2]:11.7f}')
    print(f'r2 {r2[0]:11.7f} {r2[1]:11.7f} {r2[2]:11.7f}')
    print(f'r3 {r3[0]:11.7f} {r3[1]:11.7f} {r3[2]:11.7f}')
    
    # Loop through the refining process
    print('now refine the answer')
    rho2 = 999999.9
    ll = 0
    
    while (abs(rhoold2 - rho2) > 1.0e-12) and (ll <= 0):  # ll <= 15
        ll = ll + 1
        print(f' iteration #{ll:3d}')
        rho2 = rhoold2  # Reset now that inside while loop
        
        # Now form the three position vectors
        for i in range(3):
            r1[i] = rhomat[0, 0] * l1eci[i] / c1 + rs1[i]
            r2[i] = -rhomat[1, 0] * l2eci[i] + rs2[i]
            r3[i] = rhomat[2, 0] * l3eci[i] / c3 + rs3[i]
        
        magr1 = mag(r1)
        magr2 = mag(r2)
        magr3 = mag(r3)
        
        v2, theta, theta1, copa, error = gibbs(r1, r2, r3)
        
        print(f'r1 {r1[0]:11.7f} {r1[1]:11.7f} {r1[2]:11.7f} {theta*rad:11.7f} {theta1*rad:11.7f}')
        print(f'r2 {r2[0]:11.7f} {r2[1]:11.7f} {r2[2]:11.7f}')
        print(f'r3 {r3[0]:11.7f} {r3[1]:11.7f} {r3[2]:11.7f}')
        print(f'w gibbs km/s       v2 {v2[0]:11.7f} {v2[1]:11.7f} {v2[2]:11.7f}')
        
        if (error != '          ok') and (copa < 1.0 / rad):
            p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = rv2coe(r2, v2)
            print(f'coes init ans {p:11.4f}{a:11.4f}{ecc:13.9f}{incl*rad:13.7f}{omega*rad:11.5f}{argp*rad:11.5f}{nu*rad:11.5f}{m*rad:11.5f}')
            # Hgibbs to get middle vector
            v2, theta, theta1, copa, error = hgibbs(r1, r2, r3, jd1, jd2, jd3)
            print('using hgibbs: ')
        
        p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = rv2coe(r2, v2)
        print(f'coes init ans {p:11.4f}{a:11.4f}{ecc:13.9f}{incl*rad:13.7f}{omega*rad:11.5f}{argp*rad:11.5f}{nu*rad:11.5f}{m*rad:11.5f}')
        
        if ll <= 8:  # 4
            # Now get an improved estimate of the f and g series
            u = mu / (magr2 * magr2 * magr2)
            rdot = dot(r2, v2) / magr2
            udot = (-3.0 * mu * rdot) / (magr2**4)
            
            print(f'u {u:17.15f} rdot  {rdot:11.7f} udot {udot:11.7f}')
            tausqr = tau1 * tau1
            f1 = 1.0 - 0.5 * u * tausqr - (1.0 / 6.0) * udot * tausqr * tau1
            g1 = tau1 - (1.0 / 6.0) * u * tau1 * tausqr - (1.0 / 12.0) * udot * tausqr * tausqr
            tausqr = tau3 * tau3
            f3 = 1.0 - 0.5 * u * tausqr - (1.0 / 6.0) * udot * tausqr * tau3
            g3 = tau3 - (1.0 / 6.0) * u * tau3 * tausqr - (1.0 / 12.0) * udot * tausqr * tausqr
            print(f'f1 {f1:11.7f} g1 {g1:11.7f} f3 {f3:11.7f} g3 {g3:11.7f}')
        else:
            # Use exact method to find f and g
            theta = angl(r1, r2)
            theta1 = angl(r2, r3)
            
            f1 = 1.0 - ((magr1 * (1.0 - np.cos(theta)) / p))
            g1 = (magr1 * magr2 * np.sin(-theta)) / np.sqrt(p)  # - angl because backwards
            f3 = 1.0 - ((magr3 * (1.0 - np.cos(theta1)) / p))
            g3 = (magr3 * magr2 * np.sin(theta1)) / np.sqrt(p)
        
        c1 = g3 / (f1 * g3 - f3 * g1)
        c3 = -g1 / (f1 * g3 - f3 * g1)
        
        print(f' c1 {c1:11.7f} c3 {c3:11.7f} {c2:11.7f}')
        
        # Solve for all three ranges via matrix equation
        cmat[0, 0] = -c1
        cmat[1, 0] = -c2
        cmat[2, 0] = -c3
        rhomat = lir @ cmat
        
        print(f'rhomat {rhomat[0,0]:11.7f} {rhomat[1,0]:11.7f} {rhomat[2,0]:11.7f}')
        
        rhoold1 = rhomat[0, 0] / c1
        rhoold2 = rhomat[1, 0] / c2
        rhoold3 = rhomat[2, 0] / c3
        print(f'rhoold {rhoold1:11.7f} {rhoold2:11.7f} {rhoold3:11.7f}')
        
        for i in range(3):
            r1[i] = rhomat[0, 0] * l1eci[i] / c1 + rs1[i]
            r2[i] = rhomat[1, 0] * l2eci[i] / c2 + rs2[i]
            r3[i] = rhomat[2, 0] * l3eci[i] / c3 + rs3[i]
        
        print(f'r1 {r1[0]:11.7f} {r1[1]:11.7f} {r1[2]:11.7f}')
        print(f'r2 {r2[0]:11.7f} {r2[1]:11.7f} {r2[2]:11.7f}')
        print(f'r3 {r3[0]:11.7f} {r3[1]:11.7f} {r3[2]:11.7f}')
        print('====================next loop')
        print(f'rhoold while  {rhoold2:16.14f} {rho2:16.14f}')
    
    # Find all three vectors ri
    for i in range(3):
        r1[i] = rhomat[0, 0] * l1eci[i] / c1 + rs1[i]
        r2[i] = -rhomat[1, 0] * l2eci[i] + rs2[i]
        r3[i] = rhomat[2, 0] * l3eci[i] / c3 + rs3[i]
    
    return r2, v2 