"""
Atmospheric model setup
Python version of fillin_atmosphere.m
"""

import numpy as np
import scipy.io as sio
from datetime import datetime
from astropy.time import Time
import sys
from pathlib import Path

def fillin_atmosphere(cfgMC):
    """
    Fill in atmospheric model configuration
    
    Parameters:
    -----------
    cfgMC : dict
        Configuration dictionary to be modified
        
    Returns:
    --------
    cfgMC : dict
        Updated configuration dictionary
    """
    
    # ATMOSPHERIC MODEL (pre-computed JB2008)
    # valid from March 2008 - Feb 2224 for density file 'dens_jb2008_032020_022224.mat'
    density_profile = 'JB2008'  # The options are 'static' or 'JB2008'
    cfgMC['density_profile'] = density_profile
    
    if cfgMC['density_profile'].lower() == 'jb2008':
        cfgMC = initJB2008(cfgMC)
        
    return cfgMC

def initJB2008(cfgMC):
    """
    Initialize JB2008 atmospheric model
    
    Parameters:
    -----------
    cfgMC : dict
        Configuration dictionary
        
    Returns:
    --------
    cfgMCout : dict
        Updated configuration dictionary with JB2008 parameters
    """
    
    # Find density file
    fn = Path(__file__).parent.parent / 'supporting_data' / 'dens_jb2008_032020_022224.mat'
    
    if not fn.exists():
        # Try alternative locations
        alt_paths = [
            Path(__file__).parent.parent.parent / 'supporting_data' / 'dens_jb2008_032020_022224.mat',
            Path.cwd() / 'supporting_data' / 'dens_jb2008_032020_022224.mat'
        ]
        
        for alt_path in alt_paths:
            if alt_path.exists():
                fn = alt_path
                break
        else:
            print(f"Warning: Density file not found at {fn}")
            print("Using default atmospheric parameters")
            # Set default parameters
            cfgMC['param'] = {
                'dens_times': np.array([]),
                'alt': np.array([]),
                'dens_value': np.array([])
            }
            return cfgMC
    
    # Load density data
    try:
        mat_data = sio.loadmat(str(fn))
        dens_highvar = mat_data['dens_highvar'][0, 0]  # Extract structure
        
        # Extract data from structure
        month = dens_highvar['month'].flatten()
        year = dens_highvar['year'].flatten()
        alt = dens_highvar['alt'].flatten()
        dens = dens_highvar['dens']
        
        # Calculate Julian dates
        dens_times = np.zeros(len(month))
        for k in range(len(month)):
            # Create datetime and convert to Julian date
            dt = datetime(int(year[k]), int(month[k]), 1)
            jd = Time(dt).jd
            dens_times[k] = jd
        
        # Create meshgrid
        dens_times2, alt2 = np.meshgrid(dens_times, alt)
        
        cfgMCout = cfgMC.copy()
        cfgMCout['param'] = {
            'dens_times': dens_times2,
            'alt': alt2,
            'dens_value': dens
        }
        
    except Exception as e:
        print(f"Error loading density file: {e}")
        print("Using default atmospheric parameters")
        # Set default parameters
        cfgMCout = cfgMC.copy()
        cfgMCout['param'] = {
            'dens_times': np.array([]),
            'alt': np.array([]),
            'dens_value': np.array([])
        }
    
    return cfgMCout 