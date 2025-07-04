#!/usr/bin/env python3
"""
GETIGRFCOEFS - Extract IGRF coefficients from .dat files.

This module extracts the IGRF coefficients from .dat files provided on the
IGRF ftp server. The coefficients are stored as a structure array with
various fields for year, g/h coefficients, and slope information.

Author: Converted from MATLAB
Date: 2024
"""

import os
import re
import numpy as np
import pickle
from pathlib import Path


def getigrfcoefs(datadirectory=None):
    """
    Extract IGRF coefficients from .dat files.
    
    Usage: 
        coefs, years = getigrfcoefs(datadirectory)
        or getigrfcoefs(datadirectory)  # saves to igrfcoefs.pkl
    
    Use this function to extract the IGRF coefficients from .dat files
    provided on the IGRF ftp here:
    
    ftp://hanna.ccmc.gsfc.nasa.gov/pub/modelweb/geomagnetic/igrf/fortran_code/
    
    The .dat files should be located in the directory DATADIRECTORY. If
    DATADIRECTORY is unspecified, this function will look for a directory
    called "datfiles" within the directory that this file is in or, if that
    does not exist, will just use the directory that this file is in.
    
    Parameters:
    -----------
    datadirectory : str, optional
        Directory where the .dat IGRF coefficients can be found.
        If None, looks for "datfiles" subdirectory or uses current directory.
        
    Returns:
    --------
    coefs : list of dicts
        List of dictionaries with the following fields:
        - year: Year for the coefficients
        - gh: g and h coefficients in a vector
        - g: g coefficients in a matrix with each n going down the rows
        - h: h coefficients in a matrix with each n going down the rows
        - slope: True if the coefficients are slopes, false otherwise
    years : ndarray
        Year of each element in coefs
    """
    # Get the directory with the datfiles
    if datadirectory is None or datadirectory == '':
        fpath = Path(__file__).parent
        datfiles_path = fpath / 'datfiles'
        if datfiles_path.exists():
            datadirectory = str(datfiles_path)
        else:
            datadirectory = str(fpath)
    
    # Get all the valid coefficient files
    datfiles = []
    for file in os.listdir(datadirectory):
        if file.endswith('.dat') and 'grf' in file:
            datfiles.append(file)
    
    if not datfiles:
        raise FileNotFoundError(f'No valid .dat files found in {datadirectory}')
    
    years = np.zeros(len(datfiles))
    coefs = []
    
    for index, filename in enumerate(datfiles):
        # Read the current file
        filepath = os.path.join(datadirectory, filename)
        try:
            with open(filepath, 'r') as fid:
                line1 = fid.readline().strip()
                line2 = fid.readline().strip()
                line2_parts = line2.split()
                thisnmax = int(line2_parts[0])
                thisr = float(line2_parts[1])
                thisyear = float(line2_parts[2])
                
                # Read all coefficients
                thiscoefs = []
                for line in fid:
                    thiscoefs.extend([float(x) for x in line.split()])
                thiscoefs = np.array(thiscoefs)
        except Exception as e:
            raise IOError(f'Cannot open {filename}: {e}')
        
        # Generate a vector that has all the m indices
        # It will go [0 1 0 1 2 0 1 2 3 ...]
        mmat = np.tril(np.tile(np.arange(1, thisnmax + 1), (thisnmax, 1))).T
        mmat[mmat == 0] = -1
        mmat = np.vstack([np.zeros((1, thisnmax)), mmat])
        m = mmat[mmat != -1]
        
        # Also generate a vector that has all the n indices
        # It will go [1 1 2 2 2 3 3 3 3 ...]
        nmat = np.vstack([np.arange(1, thisnmax + 1), 
                         np.triu(np.tile(np.arange(1, thisnmax + 1), (thisnmax, thisnmax)))])
        n = nmat[nmat != 0]
        
        # thiscoefs omits h when m = 0. However, it is easier to just set h = 0
        # in those places. Find where those places should be in a full vector:
        m0 = m.copy()
        m0[m0 == 0] = -1
        h0 = np.column_stack([m, m0]) == -1
        h0 = h0.flatten()
        
        # Extract the g and h coefficients from thiscoefs
        ncoefs = 2 * sum(range(1, thisnmax + 2))
        coefsvec = np.zeros(ncoefs)
        coefsvec[~h0] = thiscoefs
        gvec = coefsvec[::2]  # Every other element starting from 0
        hvec = coefsvec[1::2]  # Every other element starting from 1
        
        # Put the coefficients in a matrix with n going down the rows and m
        # down the columns
        thisg = np.zeros((thisnmax, thisnmax + 1))
        thish = np.zeros((thisnmax, thisnmax + 1))
        
        for i in range(len(n)):
            thisg[n[i] - 1, m[i]] = gvec[i]
            thish[n[i] - 1, m[i]] = hvec[i]
        
        # Save the data to coefs
        coef_dict = {
            'year': thisyear,
            'g': thisg,
            'h': thish,
            'gh': thiscoefs,
            'slope': bool(re.search(r'\wgrf\d\d\d\ds\.dat', filename, re.IGNORECASE))
        }
        coefs.append(coef_dict)
        
        # Save the year for sorting later
        years[index] = thisyear
    
    # Sort coefs based on the year
    sortind = np.argsort(years)
    coefs = [coefs[i] for i in sortind]
    years = years[sortind]
    
    return coefs, years


def main():
    """Example usage of getigrfcoefs function."""
    try:
        # Try to get coefficients
        coefs, years = getigrfcoefs()
        
        print(f"Found {len(coefs)} IGRF coefficient sets")
        print(f"Years: {years}")
        
        if coefs:
            print(f"\nFirst coefficient set (year {coefs[0]['year']}):")
            print(f"  g matrix shape: {coefs[0]['g'].shape}")
            print(f"  h matrix shape: {coefs[0]['h'].shape}")
            print(f"  gh vector length: {len(coefs[0]['gh'])}")
            print(f"  slope: {coefs[0]['slope']}")
        
        # Save to pickle file (equivalent to MATLAB's .mat file)
        fpath = Path(__file__).parent
        with open(fpath / 'igrfcoefs.pkl', 'wb') as f:
            pickle.dump({'years': years, 'coefs': coefs}, f)
        print(f"\nSaved coefficients to {fpath / 'igrfcoefs.pkl'}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure .dat files are available in the datfiles directory")


if __name__ == "__main__":
    main() 