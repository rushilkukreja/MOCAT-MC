#!/usr/bin/env python3
"""
GEOD2ECEF - Convert geodetic coordinates to ECEF coordinates.

This module converts geodetic coordinates to Earth-centered, Earth fixed
(ECEF) coordinates using the World Geodetic System 1984 (WGS84) ellipsoid.

Author: Converted from MATLAB
Date: 2024
"""

import numpy as np


def geod2ecef(latitude, longitude=None, altitude=None):
    """
    Convert geodetic coordinates to ECEF coordinates.
    
    Usage: 
        x, y, z = geod2ecef(latitude, longitude, altitude)
        or xyz = geod2ecef(lla)
    
    Converts geodetic coordinates LATITUDE, LONGITUDE, and ALTITUDE to
    Earth-centered, Earth fixed (ECEF) coordinates X, Y, and Z. The inputs
    can either be three separate arguments or 1 matrix. For a matrix input,
    the first dimension with length 3 is assumed to have the three separate
    LATITUDE, LONGITUDE, and ALTITUDE inputs across it. The World Geodetic
    System 1984 (WGS84) ellipsoid model of the Earth is assumed.
    
    Parameters:
    -----------
    latitude : array-like
        Geodetic latitude in degrees, or matrix with lla data
    longitude : array-like, optional
        Geodetic longitude in degrees
    altitude : array-like, optional
        Height above the Earth in meters
        
    Returns:
    --------
    x : ndarray
        x coordinates of the point in meters
    y : ndarray
        y coordinates of the point in meters
    z : ndarray
        z coordinates of the point in meters
    """
    # Input checking/conversion
    if longitude is None and altitude is None:
        # Single matrix input
        latitude = np.asarray(latitude)
        sizelatitude = latitude.shape
        first3 = np.where(np.array(sizelatitude) == 3)[0]
        
        if len(first3) == 0:
            raise ValueError("Input matrix must have a dimension of length 3")
        
        first3 = first3[0]
        
        # Reshape to 3xN matrix
        perm = list(range(len(sizelatitude)))
        perm.insert(0, perm.pop(first3))
        latitude_reshaped = np.transpose(latitude, perm)
        latitude_reshaped = latitude_reshaped.reshape(3, -1)
        
        latitude = latitude_reshaped[0, :].reshape(sizelatitude[:first3] + (1,) + sizelatitude[first3+1:])
        longitude = latitude_reshaped[1, :].reshape(sizelatitude[:first3] + (1,) + sizelatitude[first3+1:])
        altitude = latitude_reshaped[2, :].reshape(sizelatitude[:first3] + (1,) + sizelatitude[first3+1:])
    else:
        # Separate latitude, longitude, altitude inputs
        latitude = np.asarray(latitude)
        longitude = np.asarray(longitude)
        altitude = np.asarray(altitude)
    
    # Convert to radians
    latitude = latitude * np.pi / 180
    longitude = longitude * np.pi / 180
    
    # WGS84 parameters
    a = 6378137  # Semi-major axis in meters
    f = 1/298.257223563  # Flattening
    b = a * (1 - f)  # Semi-minor axis
    e2 = 1 - (b/a)**2  # Eccentricity squared
    
    # Conversion from:
    # en.wikipedia.org/wiki/Geodetic_system#Conversion_calculations
    Nphi = a / np.sqrt(1 - e2 * np.sin(latitude)**2)
    x = (Nphi + altitude) * np.cos(latitude) * np.cos(longitude)
    y = (Nphi + altitude) * np.cos(latitude) * np.sin(longitude)
    z = (Nphi * (1 - e2) + altitude) * np.sin(latitude)
    
    return x, y, z


def main():
    """Example usage of geod2ecef function."""
    # Example coordinates (somewhere on Earth)
    lat = 40.7128  # degrees (New York City)
    lon = -74.0060  # degrees
    alt = 10  # meters above sea level
    
    # Convert to ECEF coordinates
    x, y, z = geod2ecef(lat, lon, alt)
    
    print(f"Geodetic coordinates: ({lat}°, {lon}°, {alt} m)")
    print(f"ECEF coordinates: ({x:.1f}, {y:.1f}, {z:.1f}) meters")
    
    # Test with matrix input
    lla = np.array([lat, lon, alt])
    x2, y2, z2 = geod2ecef(lla)
    
    print(f"\nMatrix input test:")
    print(f"ECEF coordinates: ({x2:.1f}, {y2:.1f}, {z2:.1f}) meters")
    
    # Test round-trip conversion
    lat_back, lon_back, alt_back = ecef2geod(x, y, z)
    
    print(f"\nRound-trip test:")
    print(f"Original: ({lat:.6f}°, {lon:.6f}°, {alt:.1f} m)")
    print(f"Converted back: ({lat_back:.6f}°, {lon_back:.6f}°, {alt_back:.1f} m)")


if __name__ == "__main__":
    # Import for round-trip test
    from ecef2geod import ecef2geod
    main() 