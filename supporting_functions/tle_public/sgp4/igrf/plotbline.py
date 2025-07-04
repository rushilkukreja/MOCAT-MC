#!/usr/bin/env python3
"""
PLOTBLINE - Plot magnetic field lines.

This module provides functions to plot magnetic field lines using
the IGRF model.

Author: Converted from MATLAB
Date: 2024
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plotbline(time, start_points, max_steps=1000, step_size=100, 
              field_model='igrf', **kwargs):
    """
    Plot magnetic field lines starting from given points.
    
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
    field_model : str, optional
        Magnetic field model to use (default: 'igrf')
    **kwargs : dict
        Additional plotting arguments
        
    Returns:
    --------
    fig : matplotlib.figure.Figure
        The created figure
    ax : matplotlib.axes.Axes
        The axes object
    field_lines : list
        List of field line coordinates
    """
    # Create 3D figure
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    field_lines = []
    
    # Calculate field lines for each starting point
    for i, start_point in enumerate(start_points):
        lat, lon, alt = start_point
        
        # Trace the field line
        line_coords = _trace_field_line(lat, lon, alt, time, max_steps, step_size)
        field_lines.append(line_coords)
        
        # Plot the field line
        if len(line_coords) > 1:
            x, y, z = line_coords.T
            ax.plot(x, y, z, linewidth=2, alpha=0.8, 
                   label=f'Field Line {i+1}' if i < 5 else None)
    
    # Add Earth surface
    _plot_earth_surface(ax)
    
    # Set labels and title
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title(f'Magnetic Field Lines\nTime: {time}')
    
    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 1])
    
    # Add legend for first few lines
    if len(start_points) <= 5:
        ax.legend()
    
    return fig, ax, field_lines


def _trace_field_line(lat, lon, alt, time, max_steps, step_size):
    """
    Trace a magnetic field line from a starting point.
    
    This is a placeholder function - the actual implementation would
    use the IGRF model to calculate real magnetic field vectors and
    integrate along the field direction.
    """
    # Convert starting point to cartesian coordinates
    # Earth radius in km
    Re = 6371
    
    # Convert lat/lon to radians
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)
    
    # Convert to cartesian coordinates
    r = Re + alt
    x = r * np.cos(lat_rad) * np.cos(lon_rad)
    y = r * np.cos(lat_rad) * np.sin(lon_rad)
    z = r * np.sin(lat_rad)
    
    # Initialize field line coordinates
    line_coords = [[x, y, z]]
    
    # Simple field line tracing (placeholder)
    # In reality, this would integrate along the magnetic field direction
    for step in range(max_steps):
        # Calculate magnetic field direction at current point
        # This is a simplified dipole field approximation
        current_r = np.sqrt(x**2 + y**2 + z**2)
        
        if current_r < Re:
            break  # Stop if we hit the Earth
        
        # Simple dipole field direction (radial component)
        # In reality, this would be the actual magnetic field vector
        dx = -x / current_r
        dy = -y / current_r
        dz = -z / current_r
        
        # Normalize and scale by step size
        length = np.sqrt(dx**2 + dy**2 + dz**2)
        dx = dx / length * step_size
        dy = dy / length * step_size
        dz = dz / length * step_size
        
        # Update position
        x += dx
        y += dy
        z += dz
        
        line_coords.append([x, y, z])
        
        # Stop if we're too far from Earth
        if current_r > 10 * Re:
            break
    
    return np.array(line_coords)


def _plot_earth_surface(ax):
    """Plot a simplified Earth surface."""
    # Create Earth surface (simplified sphere)
    u = np.linspace(0, 2 * np.pi, 20)
    v = np.linspace(0, np.pi, 20)
    
    Re = 6371  # Earth radius in km
    
    x = Re * np.outer(np.cos(u), np.sin(v))
    y = Re * np.outer(np.sin(u), np.sin(v))
    z = Re * np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Plot Earth surface
    ax.plot_surface(x, y, z, color='lightblue', alpha=0.3, linewidth=0)


def plotbline_2d(time, start_points, projection='equatorial', 
                max_steps=1000, step_size=100, **kwargs):
    """
    Plot magnetic field lines in 2D projection.
    
    Parameters:
    -----------
    time : float or str
        Time for the magnetic field calculation
    start_points : ndarray
        Starting points for field lines (N x 3 array of lat, lon, alt)
    projection : str, optional
        Projection type: 'equatorial', 'meridional' (default: 'equatorial')
    max_steps : int, optional
        Maximum number of integration steps (default: 1000)
    step_size : float, optional
        Step size in kilometers (default: 100)
    **kwargs : dict
        Additional plotting arguments
        
    Returns:
    --------
    fig : matplotlib.figure.Figure
        The created figure
    ax : matplotlib.axes.Axes
        The axes object
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Calculate and plot field lines
    for i, start_point in enumerate(start_points):
        lat, lon, alt = start_point
        
        # Trace the field line
        line_coords = _trace_field_line(lat, lon, alt, time, max_steps, step_size)
        
        if len(line_coords) > 1:
            if projection == 'equatorial':
                # Project to equatorial plane (x-y)
                x, y = line_coords[:, 0], line_coords[:, 1]
                ax.plot(x, y, linewidth=2, alpha=0.8, 
                       label=f'Field Line {i+1}' if i < 5 else None)
            elif projection == 'meridional':
                # Project to meridional plane (r-z)
                r = np.sqrt(line_coords[:, 0]**2 + line_coords[:, 1]**2)
                z = line_coords[:, 2]
                ax.plot(r, z, linewidth=2, alpha=0.8, 
                       label=f'Field Line {i+1}' if i < 5 else None)
    
    # Add Earth circle
    Re = 6371
    if projection == 'equatorial':
        circle = plt.Circle((0, 0), Re, color='lightblue', alpha=0.3)
        ax.add_patch(circle)
        ax.set_xlabel('X (km)')
        ax.set_ylabel('Y (km)')
    elif projection == 'meridional':
        ax.plot([Re, Re], [-Re, Re], 'lightblue', linewidth=3, alpha=0.3)
        ax.set_xlabel('Radial Distance (km)')
        ax.set_ylabel('Z (km)')
    
    ax.set_title(f'Magnetic Field Lines - {projection.title()} Projection\nTime: {time}')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    
    if len(start_points) <= 5:
        ax.legend()
    
    return fig, ax


def main():
    """Example usage of plotbline functions."""
    time = 2020.5
    
    # Define starting points for field lines
    start_points = np.array([
        [60, 0, 100],    # High latitude
        [30, 0, 100],    # Mid latitude
        [0, 0, 100],     # Equator
        [-30, 0, 100],   # Mid latitude (south)
        [-60, 0, 100],   # High latitude (south)
    ])
    
    # 3D plot
    fig1, ax1, lines1 = plotbline(time, start_points)
    plt.savefig('magnetic_field_lines_3d.png', dpi=300, bbox_inches='tight')
    
    # 2D equatorial projection
    fig2, ax2 = plotbline_2d(time, start_points, projection='equatorial')
    plt.savefig('magnetic_field_lines_equatorial.png', dpi=300, bbox_inches='tight')
    
    # 2D meridional projection
    fig3, ax3 = plotbline_2d(time, start_points, projection='meridional')
    plt.savefig('magnetic_field_lines_meridional.png', dpi=300, bbox_inches='tight')
    
    plt.show()


if __name__ == "__main__":
    main() 