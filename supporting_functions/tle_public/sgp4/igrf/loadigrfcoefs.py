#!/usr/bin/env python3
"""
LOADIGRFCOEFS - Load coefficients used in IGRF model.

This module loads the coefficients used in the IGRF model at a given time
and performs the necessary interpolation between epochs.

Author: Converted from MATLAB
Date: 2024
"""

import numpy as np
import pickle
from datetime import datetime
from pathlib import Path


def loadigrfcoefs(time):
    """
    Load coefficients used in IGRF model.
    
    Usage: 
        g, h = loadigrfcoefs(time)
        or gh = loadigrfcoefs(time)
    
    Loads the coefficients used in the IGRF model at time TIME and performs
    the necessary interpolation. If two output arguments are requested, this
    returns the properly interpolated matrices G and H from igrfcoefs.pkl.
    If just one output is requested, the proper coefficient vector GH is
    returned.
    
    If this function cannot find a file called igrfcoefs.pkl in the path,
    it will try to create it by calling getigrfcoefs.
    
    Parameters:
    -----------
    time : float or str
        Time to load coefficients either as a decimal year or a string
        that can be converted to a datetime object.
        
    Returns:
    --------
    g : ndarray
        g coefficients matrix (with n going down the rows, m along the columns)
        interpolated as necessary for the input time.
    h : ndarray
        h coefficients matrix (with n going down the rows, m along the columns)
        interpolated as necessary for the input time.
    gh : ndarray
        g and h coefficient vector formatted as:
        [g(n=1,m=0) g(n=1,m=1) h(n=1,m=1) g(n=2,m=0) g(n=2,m=1) h(n=2,m=1) ...]
    """
    # Load coefs and years variables
    fpath = Path(__file__).parent
    coefs_file = fpath / 'igrfcoefs.pkl'
    
    if not coefs_file.exists():
        # Try to create the file by calling getigrfcoefs
        from getigrfcoefs import getigrfcoefs
        getigrfcoefs()
    
    with open(coefs_file, 'rb') as f:
        data = pickle.load(f)
        coefs = data['coefs']
        years = data['years']
    
    # Convert time to a decimal year if it is a string
    if isinstance(time, str):
        try:
            dt = datetime.fromisoformat(time.replace('Z', '+00:00'))
            time = dt.year + (dt.timetuple().tm_yday - 1) / 365.25
        except ValueError:
            # Try other common formats
            for fmt in ['%Y-%m-%d', '%Y/%m/%d', '%m/%d/%Y']:
                try:
                    dt = datetime.strptime(time, fmt)
                    time = dt.year + (dt.timetuple().tm_yday - 1) / 365.25
                    break
                except ValueError:
                    continue
            else:
                raise ValueError(f"Could not parse time string: {time}")
    
    # Make sure time has only one element
    if np.size(time) > 1:
        raise ValueError('The input TIME can only have one element')
    
    # Check validity on time
    if time < years[0] or time > years[-1]:
        raise ValueError(f'This IGRF is only valid between {years[0]} and {years[-1]}')
    
    # Get the nearest epoch that the current time is between
    lastepoch = np.where(time - (time % 5) == years)[0]
    if len(lastepoch) == 0:
        # Find the closest epoch
        lastepoch = np.argmin(np.abs(years - (time - (time % 5))))
    else:
        lastepoch = lastepoch[0]
    
    if lastepoch == len(years) - 1:
        lastepoch = lastepoch - 1
    
    nextepoch = lastepoch + 1
    
    # Output either g and h matrices or gh vector depending on the number of
    # outputs requested (in Python, we'll return both and let the user decide)
    
    # Get the coefficients based on the epoch
    lastg = coefs[lastepoch]['g']
    lasth = coefs[lastepoch]['h']
    nextg = coefs[nextepoch]['g']
    nexth = coefs[nextepoch]['h']
    
    # If one of the coefficient matrices is smaller than the other, enlarge
    # the smaller one with 0's
    if lastg.shape[0] > nextg.shape[0]:
        smalln = nextg.shape[0]
        nextg_new = np.zeros_like(lastg)
        nextg_new[:smalln, :smalln+1] = coefs[nextepoch]['g']
        nextg = nextg_new
        
        nexth_new = np.zeros_like(lasth)
        nexth_new[:smalln, :smalln+1] = coefs[nextepoch]['h']
        nexth = nexth_new
    elif lastg.shape[0] < nextg.shape[0]:
        smalln = lastg.shape[0]
        lastg_new = np.zeros_like(nextg)
        lastg_new[:smalln, :smalln+1] = coefs[lastepoch]['g']
        lastg = lastg_new
        
        lasth_new = np.zeros_like(nexth)
        lasth_new[:smalln, :smalln+1] = coefs[lastepoch]['h']
        lasth = lasth_new
    
    # Calculate g and h using a linear interpolation between the last and next
    # epoch
    if coefs[nextepoch]['slope']:
        gslope = nextg
        hslope = nexth
    else:
        gslope = (nextg - lastg) / 5
        hslope = (nexth - lasth) / 5
    
    g = lastg + gslope * (time - years[lastepoch])
    h = lasth + hslope * (time - years[lastepoch])
    
    # Also calculate the gh vector for single output case
    lastgh = coefs[lastepoch]['gh']
    nextgh = coefs[nextepoch]['gh']
    
    # If one of the coefficient vectors is smaller than the other, enlarge
    # the smaller one with 0's
    if len(lastgh) > len(nextgh):
        smalln = len(nextgh)
        nextgh_new = np.zeros_like(lastgh)
        nextgh_new[:smalln] = coefs[nextepoch]['gh']
        nextgh = nextgh_new
    elif len(lastgh) < len(nextgh):
        smalln = len(lastgh)
        lastgh_new = np.zeros_like(nextgh)
        lastgh_new[:smalln] = coefs[lastepoch]['gh']
        lastgh = lastgh_new
    
    # Calculate gh using a linear interpolation between the last and next
    # epoch
    if coefs[nextepoch]['slope']:
        ghslope = nextgh
    else:
        ghslope = (nextgh - lastgh) / 5
    
    gh = lastgh + ghslope * (time - years[lastepoch])
    
    return g, h, gh


def main():
    """Example usage of loadigrfcoefs function."""
    try:
        # Test with different time formats
        test_times = [2020.5, "2020-06-15", "2020/06/15"]
        
        for time in test_times:
            print(f"\nTesting with time: {time}")
            try:
                g, h, gh = loadigrfcoefs(time)
                print(f"  g matrix shape: {g.shape}")
                print(f"  h matrix shape: {h.shape}")
                print(f"  gh vector length: {len(gh)}")
                print(f"  First few g coefficients: {g[0, :5]}")
                print(f"  First few h coefficients: {h[0, :5]}")
            except Exception as e:
                print(f"  Error: {e}")
    
    except Exception as e:
        print(f"Error: {e}")
        print("Please ensure igrfcoefs.pkl file exists or can be created")


if __name__ == "__main__":
    main() 