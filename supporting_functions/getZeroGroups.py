"""
Get zero groups for mass and radius analysis
Python version of getZeroGroups.m
"""

import numpy as np
from scipy import stats

def getZeroGroups(inmatsat):
    """
    Group objects by their mass and radius characteristics
    
    Parameters:
    -----------
    inmatsat : array-like
        Input mat_sats matrix
        
    Returns:
    --------
    g1 : dict
        Group 1: payloads with logical indices
    g2 : dict  
        Group 2: rocket bodies with logical indices
    g3 : dict
        Group 3: all debris with logical indices
        
    Notes:
    ------
    Each group contains:
    - allclass: all objects of that class
    - zr: zero radius objects
    - zm: zero mass objects  
    - nz: non-zero radius and mass objects
    - nzno: non-zero, non-outlier objects
    """
    
    # Convert to numpy array if needed
    inmatsat = np.asarray(inmatsat)
    
    # Index definitions (0-based for Python)
    idx_mass = 7
    idx_radius = 8  
    idx_objectclass = 22
    
    # Initialize groups
    g1 = {'allclass': np.array([], dtype=int)}  # group 1: payloads
    g2 = {'allclass': np.array([], dtype=int)}  # group 2: RBs  
    g3 = {'allclass': np.array([], dtype=int)}  # group 3: all debris
    
    for ii in range(1, 13):  # object classes 1-12
        # Filter out NaN values and get objects with this class
        msinds = (inmatsat[:, idx_objectclass] == ii) & np.isfinite(inmatsat[:, idx_objectclass])
        
        if ii == 1:  # payloads
            g1['allclass'] = np.where(msinds)[0]  # all payload entries
            if len(g1['allclass']) > 0:
                g1['zr'] = g1['allclass'][inmatsat[g1['allclass'], idx_radius] == 0]  # index of zero radius
                g1['zm'] = g1['allclass'][inmatsat[g1['allclass'], idx_mass] == 0]    # index of zero mass
                g1['nz'] = np.setdiff1d(g1['allclass'], np.union1d(g1['zr'], g1['zm']))  # index of non-zero radius and mass
                
                # non-zero, non-outlier (using z-score method)
                if len(g1['nz']) > 0:
                    radius_outliers = np.abs(stats.zscore(inmatsat[g1['nz'], idx_radius])) > 3
                    mass_outliers = np.abs(stats.zscore(inmatsat[g1['nz'], idx_mass])) > 3
                    g1['nzno'] = g1['nz'][~(radius_outliers | mass_outliers)]
                else:
                    g1['nzno'] = np.array([])
            else:
                g1['zr'] = np.array([])
                g1['zm'] = np.array([])
                g1['nz'] = np.array([])
                g1['nzno'] = np.array([])
                
        elif ii == 5:  # rocket bodies
            g2['allclass'] = np.where(msinds)[0]  # all RB entries
            if len(g2['allclass']) > 0:
                g2['zr'] = g2['allclass'][inmatsat[g2['allclass'], idx_radius] == 0]
                g2['zm'] = g2['allclass'][inmatsat[g2['allclass'], idx_mass] == 0]
                g2['nz'] = np.setdiff1d(g2['allclass'], np.union1d(g2['zr'], g2['zm']))
                
                if len(g2['nz']) > 0:
                    radius_outliers = np.abs(stats.zscore(inmatsat[g2['nz'], idx_radius])) > 3
                    mass_outliers = np.abs(stats.zscore(inmatsat[g2['nz'], idx_mass])) > 3
                    g2['nzno'] = g2['nz'][~(radius_outliers | mass_outliers)]
                else:
                    g2['nzno'] = np.array([])
            else:
                g2['zr'] = np.array([])
                g2['zm'] = np.array([])
                g2['nz'] = np.array([])
                g2['nzno'] = np.array([])
                
        else:  # debris
            debris_inds = np.where(msinds)[0]
            g3['allclass'] = np.union1d(g3['allclass'], debris_inds).astype(int)  # all debris entries
    
    # Process debris group
    if len(g3['allclass']) > 0:
        g3['zr'] = g3['allclass'][inmatsat[g3['allclass'], idx_radius] == 0]
        g3['zm'] = g3['allclass'][inmatsat[g3['allclass'], idx_mass] == 0]
        g3['nz'] = np.setdiff1d(g3['allclass'], np.union1d(g3['zr'], g3['zm']))
        
        if len(g3['nz']) > 0:
            radius_outliers = np.abs(stats.zscore(inmatsat[g3['nz'], idx_radius])) > 3
            mass_outliers = np.abs(stats.zscore(inmatsat[g3['nz'], idx_mass])) > 3
            g3['nzno'] = g3['nz'][~(radius_outliers | mass_outliers)]
        else:
            g3['nzno'] = np.array([])
    else:
        g3['zr'] = np.array([])
        g3['zm'] = np.array([])
        g3['nz'] = np.array([])
        g3['nzno'] = np.array([])
    
    return g1, g2, g3 