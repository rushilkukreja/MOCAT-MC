#!/usr/bin/env python3
"""
IGRFLINE - Trace magnetic field lines using IGRF model.

This module provides functions to trace magnetic field lines using the
International Geomagnetic Reference Field (IGRF) model.

Author: Converted from MATLAB
Date: 2024
"""

import numpy as np
from igrf import igrf_vector


def igrfline(time, start_points, max_steps=1000, step_size=100, 
             direction='both', field_model='igrf'):
    """
    Trace magnetic field lines using IGRF model.
    
    Parameters:
    -----------
    time : float or str
        Time for the magnetic field calculation (decimal year or date string)
    start_points : ndarray
        Starting points for field lines (N x 3 array of lat, lon, alt)
    max_steps : int, optional
        Maximum number of integration steps (default: 1000)
    step_size : float, optional
        Step size in kilometers (default: 100)
    direction : str, optional
        Direction to trace: 'forward', 'backward', 'both' (default: 'both')
    field_model : str, optional
        Magnetic field model to use (default: 'igrf')
        
    Returns:
    --------
    field_lines : list
        List of field line coordinates arrays
    """
    field_lines = []
    
    for start_point in start_points:
        lat, lon, alt = start_point
        
        # Trace field line
        line_coords = _trace_igrf_field_line(lat, lon, alt, time, max_steps, 
                                           step_size, direction)
        field_lines.append(line_coords)
    
    return field_lines


def _trace_igrf_field_line(lat, lon, alt, time, max_steps, step_size, direction):
    """
    Trace a single IGRF field line from a starting point.
    
    Parameters:
    -----------
    lat : float
        Starting latitude in degrees
    lon : float
        Starting longitude in degrees
    alt : float
        Starting altitude in kilometers
    time : float or str
        Time for the calculation
    max_steps : int
        Maximum number of integration steps
    step_size : float
        Step size in kilometers
    direction : str
        Direction to trace: 'forward', 'backward', 'both'
        
    Returns:
    --------
    line_coords : ndarray
        Field line coordinates (N x 3 array of x, y, z in km)
    """
    # Earth radius in km
    Re = 6371.2
    
    # Convert starting point to cartesian coordinates
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)
    
    r = Re + alt
    x = r * np.cos(lat_rad) * np.cos(lon_rad)
    y = r * np.cos(lat_rad) * np.sin(lon_rad)
    z = r * np.sin(lat_rad)
    
    # Initialize field line coordinates
    line_coords = [[x, y, z]]
    
    # Determine tracing directions
    if direction == 'both':
        directions = [1, -1]  # Forward and backward
    elif direction == 'forward':
        directions = [1]
    elif direction == 'backward':
        directions = [-1]
    else:
        raise ValueError(f"Unknown direction: {direction}")
    
    # Trace in each direction
    for dir_sign in directions:
        current_x, current_y, current_z = x, y, z
        
        for step in range(max_steps):
            # Convert current position to lat/lon/alt
            current_r = np.sqrt(current_x**2 + current_y**2 + current_z**2)
            
            if current_r < Re:
                break  # Stop if we hit the Earth
            
            # Convert to lat/lon/alt
            current_lat = np.arcsin(current_z / current_r)
            current_lon = np.arctan2(current_y, current_x)
            current_alt = current_r - Re
            
            # Calculate magnetic field at current position
            try:
                B_north, B_east, B_down = igrf_vector(time, 
                                                    np.degrees(current_lat), 
                                                    np.degrees(current_lon), 
                                                    current_alt)
                
                # Convert to cartesian components
                B_x, B_y, B_z = _convert_field_to_cartesian(B_north, B_east, B_down, 
                                                          current_lat, current_lon)
                
                # Normalize field vector
                B_magnitude = np.sqrt(B_x**2 + B_y**2 + B_z**2)
                if B_magnitude > 0:
                    B_x /= B_magnitude
                    B_y /= B_magnitude
                    B_z /= B_magnitude
                else:
                    break  # Stop if field is zero
                
                # Step along field line
                current_x += dir_sign * B_x * step_size
                current_y += dir_sign * B_y * step_size
                current_z += dir_sign * B_z * step_size
                
                line_coords.append([current_x, current_y, current_z])
                
                # Stop if we're too far from Earth
                if current_r > 10 * Re:
                    break
                    
            except Exception as e:
                print(f"Warning: Error calculating field at step {step}: {e}")
                break
    
    return np.array(line_coords)


def _convert_field_to_cartesian(B_north, B_east, B_down, lat, lon):
    """
    Convert magnetic field components from local to cartesian coordinates.
    
    Parameters:
    -----------
    B_north : float
        North component of magnetic field
    B_east : float
        East component of magnetic field
    B_down : float
        Down component of magnetic field
    lat : float
        Latitude in radians
    lon : float
        Longitude in radians
        
    Returns:
    --------
    B_x : float
        X component of magnetic field
    B_y : float
        Y component of magnetic field
    B_z : float
        Z component of magnetic field
    """
    # Transformation matrix from local to cartesian coordinates
    cos_lat = np.cos(lat)
    sin_lat = np.sin(lat)
    cos_lon = np.cos(lon)
    sin_lon = np.sin(lon)
    
    # Transformation matrix
    # [B_x]   [ -sin(lat)*cos(lon)  -sin(lon)  -cos(lat)*cos(lon) ] [B_north]
    # [B_y] = [ -sin(lat)*sin(lon)   cos(lon)  -cos(lat)*sin(lon) ] [B_east ]
    # [B_z]   [  cos(lat)            0         -sin(lat)          ] [B_down ]
    
    B_x = (-sin_lat * cos_lon * B_north - sin_lon * B_east - cos_lat * cos_lon * B_down)
    B_y = (-sin_lat * sin_lon * B_north + cos_lon * B_east - cos_lat * sin_lon * B_down)
    B_z = (cos_lat * B_north - sin_lat * B_down)
    
    return B_x, B_y, B_z


def igrfline_2d(time, start_points, projection='equatorial', **kwargs):
    """
    Trace magnetic field lines and project to 2D.
    
    Parameters:
    -----------
    time : float or str
        Time for the magnetic field calculation
    start_points : ndarray
        Starting points for field lines (N x 3 array of lat, lon, alt)
    projection : str, optional
        Projection type: 'equatorial', 'meridional' (default: 'equatorial')
    **kwargs : dict
        Additional arguments passed to igrfline
        
    Returns:
    --------
    projected_lines : list
        List of projected field line coordinates
    """
    # Trace 3D field lines
    field_lines = igrfline(time, start_points, **kwargs)
    
    projected_lines = []
    
    for line_coords in field_lines:
        if len(line_coords) > 1:
            if projection == 'equatorial':
                # Project to equatorial plane (x-y)
                projected = line_coords[:, :2]  # x, y coordinates
            elif projection == 'meridional':
                # Project to meridional plane (r-z)
                r = np.sqrt(line_coords[:, 0]**2 + line_coords[:, 1]**2)
                z = line_coords[:, 2]
                projected = np.column_stack([r, z])
            else:
                raise ValueError(f"Unknown projection: {projection}")
            
            projected_lines.append(projected)
    
    return projected_lines


def main():
    """Example usage of igrfline functions."""
    time = 2020.5
    
    # Define starting points for field lines
    start_points = np.array([
        [60, 0, 100],    # High latitude
        [30, 0, 100],    # Mid latitude
        [0, 0, 100],     # Equator
        [-30, 0, 100],   # Mid latitude (south)
        [-60, 0, 100],   # High latitude (south)
    ])
    
    print("IGRF Field Line Tracing Example")
    print("=" * 40)
    
    # Trace field lines
    field_lines = igrfline(time, start_points, max_steps=500, step_size=50)
    
    print(f"Traced {len(field_lines)} field lines")
    for i, line in enumerate(field_lines):
        print(f"  Line {i+1}: {len(line)} points")
    
    # Project to 2D
    equatorial_lines = igrfline_2d(time, start_points, projection='equatorial')
    meridional_lines = igrfline_2d(time, start_points, projection='meridional')
    
    print(f"\nProjected to {len(equatorial_lines)} equatorial lines")
    print(f"Projected to {len(meridional_lines)} meridional lines")


if __name__ == "__main__":
    main() 