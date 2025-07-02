import numpy as np

def hill2eci(rtgteci, vtgteci, rinthill, vinthill):
    """
    Finds the interceptor's ECI pos/vel vectors given the ECI target and hill (relative) interceptor vectors.
    All vectors are column vectors.
    """
    magrtgt = np.linalg.norm(rtgteci)
    magrint = magrtgt + rinthill[0]
    # rv2rsw is assumed to be another function in this module
    from .rv2rsw import rv2rsw
    rtgtrsw, vtgtrsw, rotECI2RSW = rv2rsw(rtgteci, vtgteci)
    lambdadottgt = np.linalg.norm(vtgteci) / magrtgt
    lambdaint = rinthill[1] / magrtgt
    phiint = rinthill[2] / magrtgt
    sinphiint = np.sin(phiint)
    cosphiint = np.cos(phiint)
    sinlambdaint = np.sin(lambdaint)
    coslambdaint = np.cos(lambdaint)
    rotrswtoSEZ = np.array([
        [sinphiint * coslambdaint, sinphiint * sinlambdaint, -cosphiint],
        [-sinlambdaint,            coslambdaint,             0.0],
        [cosphiint * coslambdaint, cosphiint * sinlambdaint, sinphiint]
    ])
    rdotint = vinthill[0]
    lambdadotint = vinthill[1] / magrtgt + lambdadottgt
    phidotint = vinthill[2] / magrtgt
    vintSEZ = np.array([
        -magrint * phidotint,
        magrint * lambdadotint * cosphiint,
        rdotint
    ])
    vintrsw = rotrswtoSEZ.T @ vintSEZ
    vinteci = rotECI2RSW.T @ vintrsw
    rintrsw = np.array([
        cosphiint * magrint * coslambdaint,
        cosphiint * magrint * sinlambdaint,
        sinphiint * magrint
    ])
    rinteci = rotECI2RSW.T @ rintrsw
    return rinteci, vinteci 