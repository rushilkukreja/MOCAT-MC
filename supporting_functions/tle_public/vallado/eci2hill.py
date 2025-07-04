"""
-----------------------------------------------------------------------------

    eci2hill.py

    This function finds the relative pos/vel vectors given the ECI target and 
    interceptor vectors.

    Routine not dependent on km or m for distance unit
    all vectors are column vectors

    Author        : Sal Alfano (original MATLAB)
    Python port   : OpenAI Assistant, 2024

    Inputs:
        rtgteci  - target position vector in ECI    km
        vtgteci  - target velocity vector in ECI    km/s
        rinteci  - interceptor position vector in ECI km
        vinteci  - interceptor velocity vector in ECI km/s

    Outputs:
        rhill    - relative position vector in Hill frame
        vhill    - relative velocity vector in Hill frame

-----------------------------------------------------------------------------
"""
import numpy as np

def eci2hill(rtgteci, vtgteci, rinteci, vinteci):
    # Find rotation matrix from ECI to rsw frame
    # Convert target and interceptor, compute vector magnitudes
    magrtgt = np.linalg.norm(rtgteci)
    magrint = np.linalg.norm(rinteci)
    
    rtgtrsw, vtgtrsw, rotECI2RSW = rv2rsw(rtgteci, vtgteci)
    rintrsw = matvecmult(rotECI2RSW, rinteci, 3)
    vintrsw = matvecmult(rotECI2RSW, vinteci, 3)
    
    # Find rotation angles (radians) to go from target to interceptor
    sinphiint = rintrsw[2] / magrint
    phiint = np.arcsin(sinphiint)
    cosphiint = np.cos(phiint)
    lambdaint = np.arctan2(rintrsw[1], rintrsw[0])
    sinlambdaint = np.sin(lambdaint)
    coslambdaint = np.cos(lambdaint)
    lambdadottgt = np.linalg.norm(vtgteci) / magrtgt  # if circular ==>> norm(vtgteci)/magrtgt; % if not ++>> vtgtrsw(2) / magrtgt
    
    # Find position component positions
    rhill = np.zeros(3)
    rhill[0] = magrint - magrtgt
    rhill[1] = lambdaint * magrtgt
    rhill[2] = phiint * magrtgt
    
    # Find rotation matrix to go from rsw to SEZ of interceptor
    rotrswtoSEZ = np.zeros((3, 3))
    rotrswtoSEZ[0, 0] = sinphiint * coslambdaint
    rotrswtoSEZ[0, 1] = sinphiint * sinlambdaint
    rotrswtoSEZ[0, 2] = -cosphiint
    rotrswtoSEZ[1, 0] = -sinlambdaint
    rotrswtoSEZ[1, 1] = coslambdaint
    rotrswtoSEZ[1, 2] = 0.0
    rotrswtoSEZ[2, 0] = cosphiint * coslambdaint
    rotrswtoSEZ[2, 1] = cosphiint * sinlambdaint
    rotrswtoSEZ[2, 2] = sinphiint
    
    # Find velocity component positions by using angular rates in SEZ frame 
    vintSEZ = matvecmult(rotrswtoSEZ, vintrsw, 3)
    phidotint = -vintSEZ[0] / magrint
    lambdadotint = vintSEZ[1] / (magrint * cosphiint)
    
    vhill = np.zeros(3)
    vhill[0] = vintSEZ[2]  # if circular ==>> vintSEZ(3); % if not ++>> vintSEZ(3) - vtgtrsw(1)
    vhill[1] = magrtgt * (lambdadotint - lambdadottgt)
    vhill[2] = magrtgt * phidotint
    
    return rhill, vhill

# Placeholder for MATLAB dependencies
def rv2rsw(reci, veci):
    # TODO: Implement rv2rsw transformation
    return np.zeros(3), np.zeros(3), np.eye(3)

def matvecmult(mat, vec, n):
    # TODO: Implement matrix-vector multiplication
    return mat @ vec 