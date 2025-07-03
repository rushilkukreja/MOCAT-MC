"""
    -----------------------------------------------------------------
    
                              Ex2_5.py
    
  this file demonstrates example 2-5. it also includes some stressing
  cases for the coe and rv conversions for all orbit types. 
    
                          companion code for
             fundamentals of astrodynamics and applications
                                 2007
                            by david vallado
    
     (h)               email dvallado@msn.com
     (w) 719-573-2600, email dvallado@agi.com
    
     *****************************************************************
    
  current :
            30 mar 07  david vallado
                         original
  changes :
            13 feb 07  david vallado
                         original baseline
    
     *****************************************************************
"""

import numpy as np
from constastro import *
from rv2coe import rv2coe
from coe2rv import coe2rv

def ex2_5():
    rad = 180.0 / np.pi
    
    print('coe test ----------------------------')
    r = np.array([6524.834, 6862.875, 6448.296])
    v = np.array([4.901327, 5.533756, -1.976341])
    
    print(f'start {r[0]:15.9f} {r[1]:15.9f} {r[2]:15.9f}', end='')
    print(f' v {v[0]:15.10f} {v[1]:15.10f} {v[2]:15.10f}')
    # --------  coe2rv       - classical elements to position and velocity
    # --------  rv2coe       - position and velocity vectors to classical elements
    p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = rv2coe(r, v)
    print('          p km       a km      ecc      incl deg     raan deg     argp deg      nu deg      m deg      arglat   truelon    lonper')
    print(f'coes {p:11.4f} {a:11.4f} {ecc:13.9f} {incl*rad:13.7f} {omega*rad:11.5f} {argp*rad:11.5f} {nu*rad:11.5f} {m*rad:11.5f} {arglat*rad:11.5f} {truelon*rad:11.5f} {lonper*rad:11.5f}')
    
    # test various combinations of coe and rv
    print('coe tests ----------------------------')
    for i in range(1, 21):
        if i == 1:
            r = r
            v = v
        if i == 2:
            print('coe test ----------------------------')
            r = np.array([6524.834, 6862.875, 6448.296])
            v = np.array([4.901327, 5.533756, -1.976341])
        
        # ------- elliptical orbit tests -------------------
        if i == 3:
            print('coe test elliptical ----------------------------')
            r = np.array([1.1372844, -1.0534274, -0.8550194]) * 6378.137
            v = np.array([0.6510489, 0.4521008, 0.0381088]) * 7.905366149846
        if i == 4:
            print('coe test elliptical ----------------------------')
            r = np.array([1.0561942, -0.8950922, -0.0823703]) * 6378.137
            v = np.array([-0.5981066, -0.6293575, 0.1468194]) * 7.905366149846
        
        # ------- circular inclined orbit tests -------------------
        if i == 5:
            print('coe test near circular inclined ----------------------------')
            r = np.array([-0.4222777, 1.0078857, 0.7041832]) * 6378.137
            v = np.array([-0.5002738, -0.5415267, 0.4750788]) * 7.905366149846
        if i == 6:
            print('coe test near circular inclined ----------------------------')
            r = np.array([-0.7309361, -0.6794646, -0.8331183]) * 6378.137
            v = np.array([-0.6724131, 0.0341802, 0.5620652]) * 7.905366149846
        
        if i == 7:  # -- CI u = 45 deg
            print('coe test circular inclined ----------------------------')
            r = np.array([-2693.34555010128, 6428.43425355863, 4491.37782050409])
            v = np.array([-3.95484712246016, -4.28096585381370, 3.75567104538731])
        if i == 8:  # -- CI u = 315 deg
            print('coe test circular inclined ----------------------------')
            r = np.array([-7079.68834483379, 3167.87718823353, -2931.53867301568])
            v = np.array([1.77608080328182, 6.23770933190509, 2.45134017949138])
        
        # ------- elliptical equatorial orbit tests -------------------
        if i == 9:
            print('coe test elliptical near equatorial ----------------------------')
            r = np.array([21648.6109280739, -14058.7723188698, -0.0003598029])
            v = np.array([2.16378060719980, 3.32694348486311, 0.00000004164788])
        if i == 10:
            print('coe test elliptical near equatorial ----------------------------')
            r = np.array([7546.9914487222, 24685.1032834356, -0.0003598029])
            v = np.array([3.79607016047138, -1.15773520476223, 0.00000004164788])
        
        if i == 11:  # -- EE w = 20 deg
            print('coe test elliptical equatorial ----------------------------')
            r = np.array([-22739.1086596208, -22739.1086596208, 0.0])
            v = np.array([2.48514004188565, -2.02004112073465, 0.0])
        if i == 12:  # -- EE w = 240 deg
            print('coe test elliptical equatorial ----------------------------')
            r = np.array([28242.3662822040, 2470.8868808397, 0.0])
            v = np.array([0.66575215057746, -3.62533022188304, 0.0])
        
        # ------- circular equatorial orbit tests -------------------
        if i == 13:
            print('coe test circular near equatorial ----------------------------')
            r = np.array([-2547.3697454933, 14446.8517254604, 0.000])
            v = np.array([-5.13345156333487, -0.90516601477599, 0.00000090977789])
        if i == 14:
            print('coe test circular near equatorial ----------------------------')
            r = np.array([7334.858850000, -12704.3481945462, 0.000])
            v = np.array([-4.51428154312046, -2.60632166411836, 0.00000090977789])
        
        if i == 15:  # -- CE l = 65 deg
            print('coe test circular equatorial ----------------------------')
            r = np.array([6199.6905946008, 13295.2793851394, 0.0])
            v = np.array([-4.72425923942564, 2.20295826245369, 0.0])
        if i == 16:  # -- CE l = 65 deg i = 180 deg
            print('coe test circular equatorial ----------------------------')
            r = np.array([6199.6905946008, -13295.2793851394, 0.0])
            v = np.array([-4.72425923942564, -2.20295826245369, 0.0])
        
        # ------- parabolic orbit tests -------------------
        if i == 17:
            print('coe test parabolic ----------------------------')
            r = np.array([0.5916109, -1.2889359, -0.3738343]) * 6378.137
            v = np.array([1.1486347, -0.0808249, -0.1942733]) * 7.905366149846
        
        if i == 18:
            print('coe test parabolic ----------------------------')
            r = np.array([-1.0343646, -0.4814891, 0.1735524]) * 6378.137
            v = np.array([0.1322278, 0.7785322, 1.0532856]) * 7.905366149846
        
        if i == 19:
            print('coe test hyperbolic ---------------------------')
            r = np.array([0.9163903, 0.7005747, -1.3909623]) * 6378.137
            v = np.array([0.1712704, 1.1036199, -0.3810377]) * 7.905366149846
        
        if i == 20:
            print('coe test hyperbolic ---------------------------')
            r = np.array([12.3160223, -7.0604653, -3.7883759]) * 6378.137
            v = np.array([-0.5902725, 0.2165037, 0.1628339]) * 7.905366149846
        
        print(f'start {r[0]:15.9f} {r[1]:15.9f} {r[2]:15.9f}', end='')
        print(f' v  {v[0]:15.10f} {v[1]:15.10f} {v[2]:15.10f}')
        # --------  coe2rv       - classical elements to position and velocity
        # --------  rv2coe       - position and velocity vectors to classical elements
        p, a, ecc, incl, omega, argp, nu, m, arglat, truelon, lonper = rv2coe(r, v)
        print('          p km       a km      ecc      incl deg     raan deg     argp deg      nu deg      m deg      arglat   truelon    lonper')
        print(f'coes {p:11.4f} {a:11.4f} {ecc:13.9f} {incl*rad:13.7f} {omega*rad:11.5f} {argp*rad:11.5f} {nu*rad:11.5f} {m*rad:11.5f} {arglat*rad:11.5f} {truelon*rad:11.5f} {lonper*rad:11.5f}')
        r_new, v_new = coe2rv(p, ecc, incl, omega, argp, nu, arglat, truelon, lonper)
        print(f'r     {r_new[0]:15.9f} {r_new[1]:15.9f} {r_new[2]:15.9f}', end='')
        print(f' v  {v_new[0]:15.10f} {v_new[1]:15.10f} {v_new[2]:15.10f}')

if __name__ == "__main__":
    ex2_5() 