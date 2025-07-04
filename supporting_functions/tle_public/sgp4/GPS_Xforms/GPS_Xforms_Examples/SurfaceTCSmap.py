#!/usr/bin/env python3
"""
SurfaceTCSmap - Generate uniformly spaced topocentric x-y maps

This function generates uniformly spaced topocentric x-y maps of surface height,
range, and bearing. The WGS84 ellipsoid defines surface height.

Author: Converted from MATLAB
Date: 2024
"""

import numpy as np
from scipy.interpolate import griddata
import sys
import os

# Add parent directories to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..'))

# Import required functions (these would need to be implemented)
# from GPS_CoordinateXforms import llh2tcsT

def llh2tcsT(llh, origin):
    """
    Convert LLH coordinates to TCS coordinates.
    
    This is a placeholder - the actual implementation would need to be
    converted from the MATLAB version.
    """
    # Placeholder implementation
    # This should convert from lat/lon/height to TCS coordinates
    return np.zeros_like(llh)

def SurfaceTCSmap(latitude, longitude, RADAR):
    """
    Generate uniformly spaced topocentric x-y maps of surface height, range, and bearing.
    The WGS84 ellipsoid defines surface height.
    
    Parameters:
    -----------
    latitude : array-like
        Uniformly spaced grid of latitudes (rad +North)
    longitude : array-like
        Uniformly spaced grid of longitudes (rad +East)
    RADAR : dict
        Structure containing Rlat, Rlon, Rheight (rad, rad, m)
        
    Returns:
    --------
    R : ndarray
        Radar range to surface at (x,y) (m)
    PHI : ndarray
        Radar azimuth to surface at (x,y) (rad)
    x : ndarray
        X coordinates of the grid (m)
    y : ndarray
        Y coordinates of the grid (m)
    Surf : ndarray
        Surface height from topocentric tangent plane at radar origin (m)
    """
    dtr = np.pi / 180
    Rlat = RADAR['Rlat']
    Rlon = RADAR['Rlon']
    Rheight = RADAR['Rheight']
    
    # TCL reference on ellipsoid at radar location
    origin = np.array([Rlat, Rlon, 0])
    
    # Create meshgrid
    LAT, LON = np.meshgrid(latitude, longitude)
    nptsx = len(longitude)
    nptsy = len(latitude)
    
    # Generate llh 3-by-nptsx*nptsy vector of surface (zero height) points
    llh = np.vstack([LAT.flatten(), LON.flatten(), 
                     np.zeros(nptsx * nptsy)])
    
    # Convert llh to tcs
    tcs = llh2tcsT(llh, origin)
    
    # Reshape to grid
    x = tcs[0, :].reshape(nptsx, nptsy)
    y = tcs[1, :].reshape(nptsx, nptsy)
    z = tcs[2, :].reshape(nptsx, nptsy)
    
    # Compute range & azimuth(bearing) to each grid point
    R = np.sqrt(x**2 + y**2 + (z - Rheight)**2)
    PHI = np.arctan2(y, x)
    
    # Resample to uniform grid (Trim grid a bit to avoid NaN's in output)
    xs = np.linspace(np.ceil(np.min(x.flatten() / 1000)), 
                     np.floor(np.max(x.flatten() / 1000) - 1), nptsx) * 1000
    ys = np.linspace(np.ceil(np.min(y.flatten() / 1000)), 
                     np.floor(np.max(y.flatten() / 1000) - 1), nptsy) * 1000
    
    xm, ym = np.meshgrid(xs, ys)
    
    # Interpolate to uniform grid
    points = np.column_stack([x.flatten(), y.flatten()])
    
    Surf = griddata(points, z.flatten(), (xm, ym), method='linear')
    R = griddata(points, R.flatten(), (xm, ym), method='linear')
    PHI = griddata(points, PHI.flatten(), (xm, ym), method='linear')
    
    return R, PHI, xs, ys, Surf

def main():
    """Example usage of SurfaceTCSmap function."""
    # Example parameters
    latitude = np.linspace(0.5, 0.6, 50)  # rad
    longitude = np.linspace(-1.3, -1.2, 50)  # rad
    
    RADAR = {
        'Rlat': 0.55,  # rad
        'Rlon': -1.25,  # rad
        'Rheight': 1000  # m
    }
    
    # Generate maps
    R, PHI, x, y, Surf = SurfaceTCSmap(latitude, longitude, RADAR)
    
    print(f"Generated maps with shape: {R.shape}")
    print(f"X range: {x[0]:.1f} to {x[-1]:.1f} m")
    print(f"Y range: {y[0]:.1f} to {y[-1]:.1f} m")
    print(f"Range min/max: {np.nanmin(R):.1f} to {np.nanmax(R):.1f} m")
    print(f"Azimuth min/max: {np.nanmin(PHI):.3f} to {np.nanmax(PHI):.3f} rad")

if __name__ == "__main__":
    main() 