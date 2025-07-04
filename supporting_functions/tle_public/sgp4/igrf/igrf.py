#!/usr/bin/env python3
"""
IGRF - International Geomagnetic Reference Field calculation.

This module provides functions to calculate the International Geomagnetic
Reference Field (IGRF) at given locations and times.

Author: Converted from MATLAB
Date: 2024
"""

import numpy as np
from loadigrfcoefs import loadigrfcoefs


def igrf(time, latitude, longitude, altitude, field_type='total'):
    """
    Calculate the International Geomagnetic Reference Field.
    
    Parameters:
    -----------
    time : float or str
        Time for the calculation (decimal year or date string)
    latitude : array-like
        Geodetic latitude in degrees
    longitude : array-like
        Geodetic longitude in degrees
    altitude : array-like
        Altitude in kilometers above Earth's surface
    field_type : str, optional
        Type of field to calculate: 'total', 'north', 'east', 'down', 'horizontal'
        (default: 'total')
        
    Returns:
    --------
    field : ndarray
        Magnetic field values in nanotesla (nT)
    """
    # Load IGRF coefficients
    g, h, gh = loadigrfcoefs(time)
    
    # Convert inputs to arrays
    latitude = np.asarray(latitude)
    longitude = np.asarray(longitude)
    altitude = np.asarray(altitude)
    
    # Ensure all inputs have the same shape
    if latitude.shape != longitude.shape or latitude.shape != altitude.shape:
        # Broadcast arrays to common shape
        latitude, longitude, altitude = np.broadcast_arrays(latitude, longitude, altitude)
    
    # Calculate magnetic field
    field = _calculate_igrf_field(latitude, longitude, altitude, g, h, field_type)
    
    return field


def _calculate_igrf_field(latitude, longitude, altitude, g, h, field_type):
    """
    Calculate IGRF magnetic field components.
    
    This is a simplified implementation. The full IGRF calculation involves
    spherical harmonic synthesis with the loaded coefficients.
    """
    # Convert to radians
    lat_rad = np.radians(latitude)
    lon_rad = np.radians(longitude)
    
    # Earth radius in km
    Re = 6371.2
    
    # Calculate radius ratio
    r = Re + altitude
    a_over_r = Re / r
    
    # Initialize field components
    B_north = np.zeros_like(latitude)
    B_east = np.zeros_like(latitude)
    B_down = np.zeros_like(latitude)
    
    # Simplified spherical harmonic calculation
    # This is a placeholder - the full implementation would use all coefficients
    for n in range(1, min(g.shape[0] + 1, 14)):  # Limit to n=13 for IGRF
        for m in range(n + 1):
            if m <= g.shape[1] - 1 and n <= g.shape[0]:
                # Get coefficients
                g_nm = g[n-1, m]
                h_nm = h[n-1, m] if m > 0 else 0
                
                # Calculate spherical harmonic functions
                P_nm = _legendre_function(n, m, np.sin(lat_rad))
                
                if m == 0:
                    # Zonal harmonics
                    B_north += g_nm * _dP_nm_dtheta(n, m, lat_rad) * (a_over_r)**(n+2)
                    B_down += g_nm * (n+1) * P_nm * (a_over_r)**(n+2)
                else:
                    # Tesseral harmonics
                    cos_m_phi = np.cos(m * lon_rad)
                    sin_m_phi = np.sin(m * lon_rad)
                    
                    B_north += (g_nm * cos_m_phi + h_nm * sin_m_phi) * _dP_nm_dtheta(n, m, lat_rad) * (a_over_r)**(n+2)
                    B_east += m * (g_nm * sin_m_phi - h_nm * cos_m_phi) * P_nm / np.cos(lat_rad) * (a_over_r)**(n+2)
                    B_down += (n+1) * (g_nm * cos_m_phi + h_nm * sin_m_phi) * P_nm * (a_over_r)**(n+2)
    
    # Return requested field component
    if field_type == 'north':
        return B_north
    elif field_type == 'east':
        return B_east
    elif field_type == 'down':
        return B_down
    elif field_type == 'horizontal':
        return np.sqrt(B_north**2 + B_east**2)
    elif field_type == 'total':
        return np.sqrt(B_north**2 + B_east**2 + B_down**2)
    else:
        raise ValueError(f"Unknown field_type: {field_type}")


def _legendre_function(n, m, x):
    """
    Calculate associated Legendre function P_n^m(x).
    
    This is a simplified implementation for demonstration.
    """
    # Simple implementation for low degrees
    if n == 1 and m == 0:
        return x
    elif n == 1 and m == 1:
        return np.sqrt(1 - x**2)
    elif n == 2 and m == 0:
        return 0.5 * (3 * x**2 - 1)
    elif n == 2 and m == 1:
        return 3 * x * np.sqrt(1 - x**2)
    elif n == 2 and m == 2:
        return 3 * (1 - x**2)
    else:
        # Placeholder for higher degrees
        return np.zeros_like(x)


def _dP_nm_dtheta(n, m, lat_rad):
    """
    Calculate derivative of Legendre function with respect to theta.
    
    This is a simplified implementation for demonstration.
    """
    x = np.sin(lat_rad)
    if n == 1 and m == 0:
        return np.cos(lat_rad)
    elif n == 1 and m == 1:
        return -x / np.sqrt(1 - x**2) * np.cos(lat_rad)
    elif n == 2 and m == 0:
        return 3 * x * np.cos(lat_rad)
    elif n == 2 and m == 1:
        return 3 * (np.sqrt(1 - x**2) - x**2 / np.sqrt(1 - x**2)) * np.cos(lat_rad)
    elif n == 2 and m == 2:
        return -6 * x * np.cos(lat_rad)
    else:
        # Placeholder for higher degrees
        return np.zeros_like(lat_rad)


def igrf_vector(time, latitude, longitude, altitude):
    """
    Calculate IGRF magnetic field vector components.
    
    Parameters:
    -----------
    time : float or str
        Time for the calculation (decimal year or date string)
    latitude : array-like
        Geodetic latitude in degrees
    longitude : array-like
        Geodetic longitude in degrees
    altitude : array-like
        Altitude in kilometers above Earth's surface
        
    Returns:
    --------
    B_north : ndarray
        North component of magnetic field (nT)
    B_east : ndarray
        East component of magnetic field (nT)
    B_down : ndarray
        Down component of magnetic field (nT)
    """
    # Load IGRF coefficients
    g, h, gh = loadigrfcoefs(time)
    
    # Convert inputs to arrays
    latitude = np.asarray(latitude)
    longitude = np.asarray(longitude)
    altitude = np.asarray(altitude)
    
    # Ensure all inputs have the same shape
    if latitude.shape != longitude.shape or latitude.shape != altitude.shape:
        latitude, longitude, altitude = np.broadcast_arrays(latitude, longitude, altitude)
    
    # Calculate field components
    B_north = _calculate_igrf_field(latitude, longitude, altitude, g, h, 'north')
    B_east = _calculate_igrf_field(latitude, longitude, altitude, g, h, 'east')
    B_down = _calculate_igrf_field(latitude, longitude, altitude, g, h, 'down')
    
    return B_north, B_east, B_down


def main():
    """Example usage of IGRF functions."""
    time = 2020.5
    
    # Test points
    latitudes = np.array([0, 30, 60, 90])
    longitudes = np.array([0, 0, 0, 0])
    altitudes = np.array([0, 0, 0, 0])
    
    print("IGRF Magnetic Field Calculation Example")
    print("=" * 50)
    
    # Calculate total field
    total_field = igrf(time, latitudes, longitudes, altitudes, 'total')
    print(f"Total magnetic field at {time}:")
    for i, (lat, lon, alt, field) in enumerate(zip(latitudes, longitudes, altitudes, total_field)):
        print(f"  Lat: {lat:6.1f}°, Lon: {lon:6.1f}°, Alt: {alt:4.0f} km -> {field:8.1f} nT")
    
    # Calculate vector components
    B_north, B_east, B_down = igrf_vector(time, latitudes, longitudes, altitudes)
    print(f"\nMagnetic field components at {time}:")
    for i, (lat, lon, alt, bn, be, bd) in enumerate(zip(latitudes, longitudes, altitudes, B_north, B_east, B_down)):
        print(f"  Lat: {lat:6.1f}°, Lon: {lon:6.1f}°, Alt: {alt:4.0f} km")
        print(f"    North: {bn:8.1f} nT, East: {be:8.1f} nT, Down: {bd:8.1f} nT")


if __name__ == "__main__":
    main() 