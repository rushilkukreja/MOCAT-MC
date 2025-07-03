import numpy as np

def ell2rv(rr, ecllon, ecllat, drr, decllon, decllat):
    """
    Ecliptic latitude longitude to position and velocity
    dav 28 mar 04
    """
    def rot1(vec, angle):
        # Placeholder for rot1 function
        return vec
    
    # Implementation
    obliquity = 0.40909280  # 23.439291 /rad
    
    r = np.zeros(3)
    r[0] = rr * np.cos(ecllat) * np.cos(ecllon)
    r[1] = rr * np.cos(ecllat) * np.sin(ecllon)
    r[2] = rr * np.sin(ecllat)
    
    v = np.zeros(3)
    v[0] = (drr * np.cos(ecllat) * np.cos(ecllon) 
            - rr * np.sin(ecllat) * np.cos(ecllon) * decllat 
            - rr * np.cos(ecllat) * np.sin(ecllon) * decllon)
    v[1] = (drr * np.cos(ecllat) * np.sin(ecllon) 
            - rr * np.sin(ecllat) * np.sin(ecllon) * decllat 
            + rr * np.cos(ecllat) * np.cos(ecllon) * decllon)
    v[2] = drr * np.sin(ecllat) + rr * np.cos(ecllat) * decllat
    
    rijk = rot1(r, -obliquity)
    vijk = rot1(v, -obliquity)
    
    return rijk, vijk 