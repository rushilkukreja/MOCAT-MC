#!/usr/bin/env python3
"""
ECEF2GEOD - Convert ECEF coordinates to geodetic coordinates.

This module converts Earth-centered, Earth fixed (ECEF) coordinates to
geodetic coordinates using the World Geodetic System 1984 (WGS84) ellipsoid.

Author: Converted from MATLAB
Date: 2024
"""

import numpy as np


def ecef2geod(x, y=None, z=None, tol=None):
    """
    Convert ECEF coordinates to geodetic coordinates.
    
    Usage: 
        latitude, longitude, altitude = ecef2geod(x, y, z, tol)
        or lla = ecef2geod(xyz, tol)
    
    Converts Earth-centered, Earth fixed (ECEF) coordinates X, Y, and Z to
    geodetic coordinates LATITUDE, LONGITUDE, and ALTITUDE. For a matrix
    input, the first dimension with length 3 is assumed to have the three
    separate X, Y, and Z inputs across it. The World Geodetic System 1984
    (WGS84) ellipsoid model of the Earth is assumed.
    
    Parameters:
    -----------
    x : array-like
        x coordinates of the point in meters, or matrix with xyz data
    y : array-like, optional
        y coordinates of the point in meters
    z : array-like, optional
        z coordinates of the point in meters
    tol : float, optional
        Maximum error tolerance in the latitude in radians (default: 1e-12)
        
    Returns:
    --------
    latitude : ndarray
        Geodetic latitude in degrees
    longitude : ndarray
        Geodetic longitude in degrees
    altitude : ndarray
        Height above the Earth in meters
    """
    # Input checking and processing
    if y is None and z is None:
        # Single matrix input
        if tol is None:
            tol = 1e-12
        else:
            tol, x = x, tol  # Swap arguments
        
        x = np.asarray(x)
        sizex = x.shape
        first3 = np.where(np.array(sizex) == 3)[0]
        
        if len(first3) == 0:
            raise ValueError("Input matrix must have a dimension of length 3")
        
        first3 = first3[0]
        
        # Reshape to 3xN matrix
        perm = list(range(len(sizex)))
        perm.insert(0, perm.pop(first3))
        x_reshaped = np.transpose(x, perm)
        x_reshaped = x_reshaped.reshape(3, -1)
        
        x = x_reshaped[0, :].reshape(sizex[:first3] + (1,) + sizex[first3+1:])
        y = x_reshaped[1, :].reshape(sizex[:first3] + (1,) + sizex[first3+1:])
        z = x_reshaped[2, :].reshape(sizex[:first3] + (1,) + sizex[first3+1:])
    else:
        # Separate x, y, z inputs
        if tol is None:
            tol = 1e-12
        x = np.asarray(x)
        y = np.asarray(y)
        z = np.asarray(z)
    
    # WGS84 parameters
    a = 6378137  # Semi-major axis in meters
    f = 1/298.257223563  # Flattening
    b = a * (1 - f)  # Semi-minor axis
    e2 = 1 - (b/a)**2  # Eccentricity squared
    
    # Longitude is easy
    longitude = np.arctan2(y, x) * 180 / np.pi
    
    # Compute latitude recursively
    rd = np.hypot(x, y)
    latitude, Nphi = _recur(np.arcsin(z / np.hypot(x, np.hypot(y, z))), 
                           z, a, e2, rd, tol, 1)
    
    sinlat = np.sin(latitude)
    coslat = np.cos(latitude)
    latitude = latitude * 180 / np.pi
    
    # Get altitude from latitude
    altitude = rd * coslat + (z + e2 * Nphi * sinlat) * sinlat - Nphi
    
    return latitude, longitude, altitude


def _recur(lat_in, z, a, e2, rd, tol, iter_count):
    """
    Recursive function to compute latitude and Nphi.
    
    Parameters:
    -----------
    lat_in : ndarray
        Input latitude in radians
    z : ndarray
        Z coordinate in meters
    a : float
        Semi-major axis in meters
    e2 : float
        Eccentricity squared
    rd : ndarray
        Radial distance in xy plane
    tol : float
        Tolerance for convergence
    iter_count : int
        Current iteration count
        
    Returns:
    --------
    latitude : ndarray
        Computed latitude in radians
    Nphi : ndarray
        Computed Nphi values
    """
    thisNphi = a / np.sqrt(1 - e2 * np.sin(lat_in)**2)
    nextlat = np.arctan((z + thisNphi * e2 * np.sin(lat_in)) / rd)
    
    if np.all(np.abs(lat_in - nextlat) < tol) or iter_count > 100:
        latitude = nextlat
        Nphi = thisNphi
    else:
        latitude, Nphi = _recur(nextlat, z, a, e2, rd, tol, iter_count + 1)
    
    return latitude, Nphi


def main():
    """Example usage of ecef2geod function."""
    # Example coordinates (somewhere on Earth)
    x = 4000000  # meters
    y = 1000000  # meters
    z = 5000000  # meters
    
    # Convert to geodetic coordinates
    lat, lon, alt = ecef2geod(x, y, z)
    
    print(f"ECEF coordinates: ({x}, {y}, {z}) meters")
    print(f"Geodetic coordinates: ({lat:.6f}°, {lon:.6f}°, {alt:.1f} m)")
    
    # Test with matrix input
    xyz = np.array([x, y, z])
    lat2, lon2, alt2 = ecef2geod(xyz)
    
    print(f"\nMatrix input test:")
    print(f"Geodetic coordinates: ({lat2:.6f}°, {lon2:.6f}°, {alt2:.1f} m)")


if __name__ == "__main__":
    main() 