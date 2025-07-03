import numpy as np

def doubler(cc1, cc2, magrsite1, magrsite2, magr1in, magr2in, los1, los2, los3, rsite1, rsite2, rsite3, t1, t3, direct):
    """
    This routine accomplishes the iteration work for the double-r angles only routine
    
    dav 12-23-03
    """
    def mag(vec):
        return np.linalg.norm(vec)
    
    def dot(vec1, vec2):
        return np.dot(vec1, vec2)
    
    def cross(vec1, vec2):
        return np.cross(vec1, vec2)
    
    re = 6378.137
    mu = 3.986004418e5
    
    rho1 = (-cc1 + np.sqrt(cc1**2 - 4 * (magrsite1**2 - magr1in**2))) / 2.0
    rho2 = (-cc2 + np.sqrt(cc2**2 - 4 * (magrsite2**2 - magr2in**2))) / 2.0
    
    r1 = rho1 * los1 + rsite1
    r2 = rho2 * los2 + rsite2
    
    print(f'start of loop  {magr1in:11.7f}  {magr2in:11.7f}')
    magr1 = mag(r1)
    magr2 = mag(r2)
    print(f'r1  {r1[0]:11.7f}   {r1[1]:11.7f}  {r1[2]:11.7f}', end='')
    print(f'r2  {r2[0]:11.7f}   {r2[1]:11.7f}  {r2[2]:11.7f}')
    
    if direct == 'y':
        w = cross(r1, r2) / (magr1 * magr2)
    else:
        w = -cross(r1, r2) / (magr1 * magr2)
    
    # Change to negative sign
    rho3 = -dot(rsite3, w) / dot(los3, w)
    r3 = rho3 * los3 + rsite3
    print(f'r3  {r3[0]:11.7f}   {r3[1]:11.7f}  {r3[2]:11.7f}')
    magr3 = mag(r3)
    print(f'after 1st mag  {magr1:11.7f}  {magr2:11.7f}  {magr3:11.7f}')
    
    cosdv21 = dot(r2, r1) / (magr2 * magr1)
    sindv21 = mag(cross(r2, r1)) / (magr2 * magr1)
    dv21 = np.arctan2(sindv21, cosdv21)
    
    cosdv31 = dot(r3, r1) / (magr3 * magr1)
    sindv31 = np.sqrt(1.0 - cosdv31**2)
    dv31 = np.arctan2(sindv31, cosdv31)
    
    cosdv32 = dot(r3, r2) / (magr3 * magr2)
    sindv32 = mag(cross(r3, r2)) / (magr3 * magr2)
    
    dv32 = np.arctan2(sindv32, cosdv32)
    
    if dv31 > np.pi:
        c1 = (magr2 * sindv32) / (magr1 * sindv31)
        c3 = (magr2 * sindv21) / (magr3 * sindv31)
        p = (c1 * magr1 + c3 * magr3 - magr2) / (c1 + c3 - 1)
    else:
        c1 = (magr1 * sindv31) / (magr2 * sindv32)
        c3 = (magr1 * sindv21) / (magr3 * sindv32)
        p = (c3 * magr3 - c1 * magr2 + magr1) / (-c1 + c3 + 1)
    
    ecosv1 = p / magr1 - 1
    ecosv2 = p / magr2 - 1
    ecosv3 = p / magr3 - 1
    
    if dv21 != np.pi:
        esinv2 = (-cosdv21 * ecosv2 + ecosv1) / sindv21
    else:
        esinv2 = (cosdv32 * ecosv2 - ecosv3) / sindv31
    
    e = np.sqrt(ecosv2**2 + esinv2**2)
    a = p / (1 - e**2)
    
    if e * e < 0.99:
        n = np.sqrt(mu / a**3)
        
        s = magr2 / p * np.sqrt(1 - e**2) * esinv2
        c = magr2 / p * (e**2 + ecosv2)
        
        sinde32 = magr3 / np.sqrt(a * p) * sindv32 - magr3 / p * (1 - cosdv32) * s
        cosde32 = 1 - magr2 * magr3 / (a * p) * (1 - cosdv32)
        deltae32 = np.arctan2(sinde32, cosde32)
        
        sinde21 = magr1 / np.sqrt(a * p) * sindv21 + magr1 / p * (1 - cosdv21) * s
        cosde21 = 1 - magr2 * magr1 / (a * p) * (1 - cosdv21)
        deltae21 = np.arctan2(sinde21, cosde21)
        
        deltam32 = deltae32 + 2 * s * (np.sin(deltae32 / 2))**2 - c * np.sin(deltae32)
        deltam12 = -deltae21 + 2 * s * (np.sin(deltae21 / 2))**2 + c * np.sin(deltae21)
    else:
        print(f'hyperbolic, e1 is greater than 0.99 {e:11.7f}')
        n = np.sqrt(mu / -a**3)
        
        s = magr2 / p * np.sqrt(e**2 - 1) * esinv2
        c = magr2 / p * (e**2 + ecosv2)
        
        sindh32 = magr3 / np.sqrt(-a * p) * sindv32 - magr3 / p * (1 - cosdv32) * s
        sindh21 = magr1 / np.sqrt(-a * p) * sindv21 + magr1 / p * (1 - cosdv21) * s
        
        deltah32 = np.log(sindh32 + np.sqrt(sindh32**2 + 1))
        deltah21 = np.log(sindh21 + np.sqrt(sindh21**2 + 1))
        
        deltam32 = -deltah32 + 2 * s * (np.sinh(deltah32 / 2))**2 + c * np.sinh(deltah32)
        deltam12 = deltah21 + 2 * s * (np.sinh(deltah21 / 2))**2 - c * np.sinh(deltah21)
        # What if ends on hyperbolic solution.
        # How to pass back deltae32?
        deltae32 = deltah32  # Fix
    
    print(f'dm32 {deltam32:11.7f}  dm12 {deltam12:11.7f} {c1:11.7f} {c3:11.7f} {p:11.7f} {a:11.7f} {e:11.7f} {s:11.7f} {c:11.7f}')
    print(f'{dv21:11.7f} {dv31:11.7f} {dv32:11.7f}')
    
    f1 = t1 - deltam12 / n
    f2 = t3 - deltam32 / n
    
    q1 = np.sqrt(f1**2 + f2**2)
    
    return r2, r3, f1, f2, q1, magr1, magr2, a, deltae32 