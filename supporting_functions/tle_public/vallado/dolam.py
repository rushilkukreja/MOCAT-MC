import numpy as np

def dolam(fid, nrev, kepmov, rtgto, vtgto, rinto, vinto, direc, mu):
    """
    dolam - code insertion for testlam program
    """
    def mag(vec):
        return np.linalg.norm(vec)
    
    def dot(vec1, vec2):
        return np.dot(vec1, vec2)
    
    def kepler(rtgto, vtgto, dt, flag):
        # Placeholder for kepler function
        return rtgto, vtgto, 'ok'
    
    def lambertu(rinto, rtgt1, direc, nrev, dt, fid):
        # Placeholder for lambertu function
        return None, None, 'ok'
    
    def rv2coe(r, v):
        # Placeholder for rv2coe function
        return None, None, None, None, None, None, None, None, None, None, None
    
    # Do the short way multiple revolution cases
    print('xx')
    print('xx 501    psinew         dt       x      a          e')
    
    for i in range(nrev * 100, 501):
        dt = i * 60.0  # sec
        # Make target moving...
        if kepmov == 'y':
            rtgt1, vtgt1, errork = kepler(rtgto, vtgto, dt, 0)
        else:
            errork = '      ok'
            rtgt1 = rtgto
            vtgt1 = vtgto
        
        if i == nrev * 100:
            # Check min energy condition and min time for that
            cosdeltanu = dot(rinto, rtgt1) / (mag(rinto) * mag(rtgt1))
            chord = np.sqrt(mag(rinto)**2 + mag(rtgt1)**2 - 2.0 * mag(rinto) * mag(rtgt1) * cosdeltanu)
            s = (mag(rinto) + mag(rtgt1) + chord) * 0.5
            amin = s / 2.0
            betam = 2.0 * np.arcsin(np.sqrt((s - chord) / s))  # Note that 2*amin is s here
            alpham = np.pi
            
            if direc == 's':
                # This one works - gets min for min a on each case
                ttran = np.sqrt(amin**3 / mu) * (2.0 * nrev * np.pi + alpham - np.sin(alpham) - betam + np.sin(betam))
                tpar = (s**1.5 - (s - chord)**1.5) * np.sqrt(2) / (3.0 * np.sqrt(mu))
            else:
                ttran = np.sqrt(amin**3 / mu) * (2.0 * nrev * np.pi + alpham - np.sin(alpham) + betam - np.sin(betam))
                tpar = (s**1.5 + (s - chord)**1.5) * np.sqrt(2) / (3.0 * np.sqrt(mu))
            
            beta = 2.0 * np.arcsin(np.sqrt((s - chord) / s))  # Should be 2*a here!!!!
            tmin = np.sqrt(amin**3 / mu) * ((2.0 * nrev + 1.0) * np.pi - beta + np.sin(beta))
            print(f'dnu {np.arccos(cosdeltanu)*180/np.pi:11.7f} mins c {chord:11.7f} s {s:11.7f} a {amin:11.7f} be {betam:11.7f} tranmin {ttran:11.7f} tmin {tmin:11.7f} tpar {tpar:11.7f}')
        
        vtrans1, vtrans2, errorl = lambertu(rinto, rtgt1, direc, nrev, dt, fid)
        
        if errorl == '      ok' and errork == '      ok':
            p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = rv2coe(rinto, vtrans1)  # Of trans orbit
            dv1 = mag(vinto - vtrans1)
            dv2 = mag(vtrans2 - vtgt1)
            print(f' {a:11.5f} {ecc:11.5f} {dv1:11.5f} {dv2:11.5f} {dv1+dv2:11.5f}')
        else:
            print(f'  0  0 {errorl}') 