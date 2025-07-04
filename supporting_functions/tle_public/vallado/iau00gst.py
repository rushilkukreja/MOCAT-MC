"""
----------------------------------------------------------------------------

    iau00gst.py

    This function finds the iau2000 greenwich sidereal time.

    Author        : David Vallado (original MATLAB)
    Python port   : OpenAI Assistant, 2024

    Inputs:
        jdut1     - julian date of ut1             days from 4713 bc
        ttt       - julian centuries of tt
        deltapsi  - change in longitude            rad
        l         - delaunay element               rad
        ll        - delaunay element               rad
        f         - delaunay element               rad
        d         - delaunay element               rad
        omega     - delaunay element               rad
        many others for planetary values           rad

    Outputs:
        gst       - greenwich sidereal time        0 to twopi rad
        st        - transformation matrix

    References:
        Vallado 2004, 216
----------------------------------------------------------------------------
"""
import numpy as np

def iau00gst(jdut1, ttt, deltapsi, l, l1, f, d, omega, 
             lonmer, lonven, lonear, lonmar, lonjup, lonsat, lonurn, lonnep, precrate):
    twopi = 2.0 * np.pi
    deg2rad = np.pi / 180.0
    # " to rad
    convrt = np.pi / (180.0 * 3600.0)
    
    # Initialize data arrays
    axs0, a0xi, ays0, a0yi, ass0, a0si, apn, apni, appl, appli, agst, agsti = iau00in()
    
    ttt2 = ttt * ttt
    ttt3 = ttt2 * ttt
    ttt4 = ttt2 * ttt2
    ttt5 = ttt3 * ttt2
    
    # Mean obliquity of the ecliptic
    epsa = 84381.448 - 46.84024 * ttt - 0.00059 * ttt2 + 0.001813 * ttt3  # "
    epsa = (epsa / 3600.0) % 360.0  # deg
    epsa = epsa * deg2rad  # rad
    
    # Evaluate the ee complementary terms
    gstsum0 = 0.0
    for i in range(32, -1, -1):  # 33: -1 : 1 in MATLAB
        tempval = (agsti[i, 0] * l + agsti[i, 1] * l1 + agsti[i, 2] * f + 
                   agsti[i, 3] * d + agsti[i, 4] * omega + agsti[i, 5] * lonmer + 
                   agsti[i, 6] * lonven + agsti[i, 7] * lonear + agsti[i, 8] * lonmar + 
                   agsti[i, 9] * lonjup + agsti[i, 10] * lonsat + agsti[i, 11] * lonurn + 
                   agsti[i, 12] * lonnep + agsti[i, 13] * precrate)
        gstsum0 = gstsum0 + agst[i, 0] * np.sin(tempval) + agst[i, 1] * np.cos(tempval)  # rad
    
    gstsum1 = 0.0
    for j in range(0, -1, -1):  # 1: -1 : 1 in MATLAB
        i = 33 + j
        tempval = (agsti[i, 0] * l + agsti[i, 1] * l1 + agsti[i, 2] * f + 
                   agsti[i, 3] * d + agsti[i, 4] * omega + agsti[i, 5] * lonmer + 
                   agsti[i, 6] * lonven + agsti[i, 7] * lonear + agsti[i, 8] * lonmar + 
                   agsti[i, 9] * lonjup + agsti[i, 10] * lonsat + agsti[i, 11] * lonurn + 
                   agsti[i, 12] * lonnep + agsti[i, 13] * precrate)
        gstsum1 = gstsum1 + agst[i, 0] * ttt * np.sin(tempval) + agst[i, 1] * ttt * np.cos(tempval)
    
    eect2000 = gstsum0 + gstsum1 * ttt  # rad
    
    # Equation of the equinoxes
    ee2000 = deltapsi * np.cos(epsa) + eect2000  # rad
    
    # Earth rotation angle
    tut1d = jdut1 - 2451545.0
    era = twopi * (0.7790572732640 + 1.00273781191135448 * tut1d)
    era = era % twopi  # rad
    
    # Greenwich mean sidereal time, iau 2000
    gmst2000 = era + (0.014506 + 4612.15739966 * ttt + 1.39667721 * ttt2 - 
                      0.00009344 * ttt3 + 0.00001882 * ttt4) * convrt  # " to rad
    
    gst = gmst2000 + ee2000  # rad
    
    # Transformation matrix
    st = np.array([
        [np.cos(gst), -np.sin(gst), 0.0],
        [np.sin(gst), np.cos(gst), 0.0],
        [0.0, 0.0, 1.0]
    ])
    
    return gst, st

# Placeholder for MATLAB dependencies
def iau00in():
    # TODO: Initialize the data arrays
    return (np.zeros((100, 2)), np.zeros((100, 14)), np.zeros((100, 2)), 
            np.zeros((100, 14)), np.zeros((100, 2)), np.zeros((100, 14)),
            np.zeros((100, 8)), np.zeros((100, 5)), np.zeros((100, 4)), 
            np.zeros((100, 14)), np.zeros((100, 2)), np.zeros((100, 14))) 