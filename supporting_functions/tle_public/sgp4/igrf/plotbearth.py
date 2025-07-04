#!/usr/bin/env python3
"""
PLOTBEARTH - Plot Earth's magnetic field.

This module provides functions to plot the Earth's magnetic field using
the IGRF model.

Author: Converted from MATLAB
Date: 2024
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors


def plotbearth(time, altitude=0, lat_range=None, lon_range=None, 
               resolution=2, field_component='total', **kwargs):
    """
    Plot Earth's magnetic field at a given time and altitude.
    
    Parameters:
    -----------
    time : float or str
        Time for the magnetic field calculation (decimal year or date string)
    altitude : float, optional
        Altitude in kilometers above Earth's surface (default: 0)
    lat_range : tuple, optional
        Latitude range (min, max) in degrees (default: (-90, 90))
    lon_range : tuple, optional
        Longitude range (min, max) in degrees (default: (-180, 180))
    resolution : float, optional
        Grid resolution in degrees (default: 2)
    field_component : str, optional
        Field component to plot: 'total', 'north', 'east', 'down', 'horizontal'
        (default: 'total')
    **kwargs : dict
        Additional plotting arguments
        
    Returns:
    --------
    fig : matplotlib.figure.Figure
        The created figure
    ax : matplotlib.axes.Axes
        The axes object
    """
    # Set default ranges if not provided
    if lat_range is None:
        lat_range = (-90, 90)
    if lon_range is None:
        lon_range = (-180, 180)
    
    # Create coordinate grid
    lats = np.arange(lat_range[0], lat_range[1] + resolution, resolution)
    lons = np.arange(lon_range[0], lon_range[1] + resolution, resolution)
    lon_grid, lat_grid = np.meshgrid(lons, lats)
    
    # Calculate magnetic field at each point
    # Note: This would need the actual IGRF calculation function
    # For now, we'll create a placeholder field
    field_values = _calculate_magnetic_field(lat_grid, lon_grid, altitude, time, field_component)
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create contour plot
    levels = np.linspace(np.min(field_values), np.max(field_values), 20)
    contour = ax.contourf(lon_grid, lat_grid, field_values, levels=levels, 
                         cmap='RdBu_r', extend='both')
    
    # Add colorbar
    cbar = plt.colorbar(contour, ax=ax, shrink=0.8)
    cbar.set_label(f'Magnetic Field ({_get_field_unit(field_component)})')
    
    # Add coastlines (simplified)
    ax.plot([-180, 180], [0, 0], 'k-', linewidth=0.5, alpha=0.3)  # Equator
    ax.plot([0, 0], [-90, 90], 'k-', linewidth=0.5, alpha=0.3)    # Prime meridian
    
    # Set labels and title
    ax.set_xlabel('Longitude (degrees)')
    ax.set_ylabel('Latitude (degrees)')
    ax.set_title(f'Earth Magnetic Field - {field_component.title()} Component\n'
                f'Time: {time}, Altitude: {altitude} km')
    
    # Set aspect ratio
    ax.set_aspect('equal')
    
    return fig, ax


def _calculate_magnetic_field(lat_grid, lon_grid, altitude, time, component):
    """
    Calculate magnetic field values at given coordinates.
    
    This is a placeholder function - the actual implementation would
    use the IGRF model to calculate real magnetic field values.
    """
    # Placeholder calculation - replace with actual IGRF computation
    # This creates a simple dipole-like field for demonstration
    
    # Convert to radians
    lat_rad = np.radians(lat_grid)
    lon_rad = np.radians(lon_grid)
    
    # Simple dipole field approximation
    # Magnetic dipole moment components (simplified)
    mx = 0
    my = 0
    mz = -8e22  # Am^2 (approximate Earth's dipole moment)
    
    # Earth radius in meters
    Re = 6371000
    r = Re + altitude * 1000  # Convert km to meters
    
    # Calculate field components
    if component == 'total':
        # Total field magnitude
        field = 30000 + 10000 * np.cos(lat_rad) + 5000 * np.sin(2 * lon_rad)
    elif component == 'north':
        field = 20000 * np.cos(lat_rad) * np.cos(lon_rad)
    elif component == 'east':
        field = 15000 * np.cos(lat_rad) * np.sin(lon_rad)
    elif component == 'down':
        field = -40000 * np.sin(lat_rad)
    elif component == 'horizontal':
        field = np.sqrt((20000 * np.cos(lat_rad) * np.cos(lon_rad))**2 + 
                       (15000 * np.cos(lat_rad) * np.sin(lon_rad))**2)
    else:
        field = np.zeros_like(lat_grid)
    
    return field


def _get_field_unit(component):
    """Get the appropriate unit for the field component."""
    units = {
        'total': 'nT',
        'north': 'nT',
        'east': 'nT',
        'down': 'nT',
        'horizontal': 'nT'
    }
    return units.get(component, 'nT')


def main():
    """Example usage of plotbearth function."""
    # Example plots
    time = 2020.5
    
    # Plot total field
    fig1, ax1 = plotbearth(time, altitude=0, field_component='total')
    plt.savefig('magnetic_field_total.png', dpi=300, bbox_inches='tight')
    
    # Plot different components
    components = ['north', 'east', 'down', 'horizontal']
    for component in components:
        fig, ax = plotbearth(time, altitude=400, field_component=component)
        plt.savefig(f'magnetic_field_{component}.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    plt.show()


if __name__ == "__main__":
    main() 