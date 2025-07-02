"""
Categorize objects into satellite, derelict, debris, and rocket body
Python version of categorizeObj.m
"""

import numpy as np

def categorizeObj(objint_st, cont_st):
    """
    Separate satellites into satellite, derelict, nonusable/debris, rocket body
    
    Parameters:
    -----------
    objint_st : array-like
        List of object indices
    cont_st : array-like
        List of control indices
        
    Returns:
    --------
    nS : int
        Satellite numbers
    nD : int
        Derelict numbers  
    nN : int
        Debris numbers
    nB : int
        Rocket body numbers
        
    Notes:
    ------
    Object classes:
    - P(payload), PMRO(debris), Pfrag(debris), Pdeb(debris), RB(rocket body),
    - RBMRO(debris), RBfrag(debris), RBdeb(debris), Deb(debris), OtherDeb(debris),
    - Unkwn(debris), untracked(debris)
    
    Categories:
    - S: satellite, object index 1 and control index 1
    - D: derelict, object index 1 and control index 0  
    - N: nonusable/debris, object index 3,4,6,7,8,9...
    - B: rocket body, object index 5
    """
    
    objint_st = np.asarray(objint_st)
    cont_st = np.asarray(cont_st)
    
    nS = np.sum((objint_st == 1) & (cont_st == 1))
    nD = np.sum((objint_st == 1) & (cont_st == 0))
    nN = np.sum((objint_st == 3) | (objint_st == 4) | (objint_st >= 6))
    nB = np.sum(objint_st == 5)
    
    return int(nS), int(nD), int(nN), int(nB) 