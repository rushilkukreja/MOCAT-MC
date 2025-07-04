#!/usr/bin/env python3
"""
Demo DataSpace2Surface Utility

This program demonstrates the DataSpace2Surface utility for radar coordinates
and target tracking in geodetic and TCS coordinate systems.

Author: Converted from MATLAB
Date: 2024
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os

# Add parent directories to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..'))

# Import required functions (these would need to be implemented)
# from GPS_CoordinateXforms import llh2tcsT, GHorizon, Source2Ellipsoid

def llh2tcsT(target_llh, source_llh):
    """
    Convert target LLH coordinates to TCS coordinates relative to source.
    
    This is a placeholder - the actual implementation would need to be
    converted from the MATLAB version.
    """
    # Placeholder implementation
    # This should convert from lat/lon/height to TCS coordinates
    return np.zeros_like(target_llh)

def GHorizon(bearing, source_llh, flag):
    """
    Calculate range to visible horizon at each bearing.
    
    This is a placeholder - the actual implementation would need to be
    converted from the MATLAB version.
    """
    # Placeholder implementation
    return np.ones_like(bearing) * 100000  # 100 km default

def Source2Ellipsoid(range_vals, bearing, source_llh, flag):
    """
    Convert source coordinates to ellipsoid parameters.
    
    This is a placeholder - the actual implementation would need to be
    converted from the MATLAB version.
    """
    # Placeholder implementation
    stheta = np.sin(bearing)
    ctheta = np.cos(bearing)
    return stheta, ctheta

def main():
    """Main demonstration function."""
    # Constants
    dtr = np.pi / 180
    rtd = 180 / np.pi
    
    # Radar coordinates
    Rlat = 36.7788  # 36 46.73' N
    Rlon = -75.9573  # 75 57.44' W
    
    # User input for static or moving source
    try:
        iStatic_input = input('Input 1 for static source, else CR: ')
        iStatic = 1 if iStatic_input.strip() == '1' else 2
    except (EOFError, KeyboardInterrupt):
        iStatic = 2
    
    type_names = ['Static', 'Moving']
    
    # Generate geodetic coordinates of source flying at constant altitude
    nsec = 500
    Rheight = 4000
    source0_llh = np.array([Rlat * dtr, Rlon * dtr, Rheight])
    dsource_llh = 4 * np.array([0.00001, 0.00002, 0])
    
    source_llh = np.zeros((3, nsec))
    source_llh[:, 0] = source0_llh
    
    for n in range(1, nsec):
        source_llh[:, n] = source_llh[:, n-1] + dsource_llh
    
    # Generate a moving ground target track
    target_llh = np.zeros((3, nsec))
    target_llh[:, 0] = source_llh[:, nsec-1]
    target_llh[2, 0] = 0
    dtarget_llh = -4 * np.array([0.00002, 0.00001, 0])
    
    for n in range(1, nsec):
        target_llh[:, n] = target_llh[:, n-1] + dtarget_llh
    
    if iStatic == 1:
        source_llh = source_llh[:, 0:1]
    
    # Plot 1: Geodetic coordinates
    fig1 = plt.figure(figsize=(10, 8))
    ax1 = fig1.add_subplot(111, projection='3d')
    
    ax1.plot3D(target_llh[0, :] * rtd, target_llh[1, :] * rtd, 
               target_llh[2, :], 'r', linewidth=2, label='Target Track')
    ax1.plot3D(target_llh[0, 0] * rtd, target_llh[1, 0] * rtd, 
               target_llh[2, 0], 'r>', markersize=10, label='Target Start')
    ax1.plot3D(source_llh[0, :] * rtd, source_llh[1, :] * rtd, 
               source_llh[2, :], 'b', linewidth=2, label='Source Track')
    ax1.plot3D(source_llh[0, 0] * rtd, source_llh[1, 0] * rtd, 
               source_llh[2, 0], 'b>', markersize=10, label='Source Start')
    
    ax1.grid(True)
    ax1.set_xlabel('Latitude (deg)')
    ax1.set_ylabel('Longitude (deg)')
    ax1.set_zlabel('Height (meters)')
    ax1.set_title(f'{type_names[iStatic-1]} Source & Target Geodetic System')
    ax1.legend()
    
    # Locate the target in a TCS system fixed on the aircraft
    target_tcs = llh2tcsT(target_llh, source_llh)
    
    # Calculate range and bearing to the target
    range_vals = np.sqrt(target_tcs[0, :]**2 + target_tcs[1, :]**2 + target_tcs[2, :]**2)
    bearing = np.arctan2(target_tcs[0, :], target_tcs[1, :])
    bearing = np.mod(bearing, 2 * np.pi)
    
    # Calculate range to visible horizon at each bearing
    rangeH = GHorizon(bearing, source_llh, 0)
    rangeH = rangeH.T
    iOK = range_vals < rangeH
    
    # Plot 2: Radar data
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.plot(bearing * rtd, range_vals / 1000, 'go', label='All Ranges', alpha=0.7)
    ax2.plot(bearing[iOK] * rtd, range_vals[iOK] / 1000, 'b.', 
             label='Visible Ranges', markersize=4)
    ax2.grid(True)
    ax2.set_xlabel('Bearing (deg)')
    ax2.set_ylabel('Range (km)')
    ax2.legend()
    ax2.set_title(f'{type_names[iStatic-1]} Radar Data')
    
    # Reconstruct target positions from radar reports
    stheta, ctheta = Source2Ellipsoid(range_vals, bearing, source_llh, 0)
    v_tcs = np.array([stheta * np.sin(bearing), 
                      stheta * np.cos(bearing), 
                      ctheta])
    tgt_tcs = np.tile(range_vals, (3, 1)) * v_tcs
    
    # Plot 3: TCS coordinates
    fig3 = plt.figure(figsize=(10, 8))
    ax3 = fig3.add_subplot(111, projection='3d')
    
    ax3.plot3D(target_tcs[0, :] / 1000, target_tcs[1, :] / 1000, 
               target_tcs[2, :] / 1000, 'b', linewidth=2, label='Truth')
    ax3.plot3D(tgt_tcs[0, :] / 1000, tgt_tcs[1, :] / 1000, 
               tgt_tcs[2, :] / 1000, 'mo', markersize=4, label='Reports')
    
    ax3.set_xlabel('x (km)')
    ax3.set_ylabel('y (km)')
    ax3.set_zlabel('z (km)')
    ax3.set_title(f'{type_names[iStatic-1]} Source TCS Coordinates of Target')
    ax3.legend()
    ax3.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main() 