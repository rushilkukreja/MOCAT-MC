#!/usr/bin/env python3
"""
Demo GPS Coordinate Transformations

This script demonstrates GPS coordinate transformations between different
coordinate systems including LLH, TCS, and ECF.

Author: Chuck Rino (Rino Consulting) - Converted from MATLAB
Date: 2024
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Add parent directories to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..'))

# Import required functions (these would need to be implemented)
# from GPS_CoordinateXforms import llh2tcsT, tcs2ecfT, ecf2llhT, tcs2llhT

def llh2tcsT(llh, origin):
    """Convert LLH to TCS coordinates."""
    # Placeholder implementation
    return np.zeros_like(llh)

def tcs2ecfT(tcs, origin):
    """Convert TCS to ECF coordinates."""
    # Placeholder implementation
    return np.zeros_like(tcs)

def ecf2llhT(ecf):
    """Convert ECF to LLH coordinates."""
    # Placeholder implementation
    return np.zeros_like(ecf)

def tcs2llhT(tcs, origin):
    """Convert TCS to LLH coordinates."""
    # Placeholder implementation
    return np.zeros_like(tcs)

def main():
    """Main demonstration function."""
    dtr = np.pi / 180
    
    # Generate a source at Rheight flying at a constant altitude
    nsec = 200
    Rlat = 36.7788
    Rlon = -75.9573
    Rheight = 4000
    
    dsource_llh = 4 * np.array([0.00001, 0.00002, 0])
    source_llh = np.zeros((3, nsec))
    source_llh[:, 0] = np.array([Rlat * dtr, Rlon * dtr, Rheight])
    
    for n in range(1, nsec):
        source_llh[:, n] = source_llh[:, n-1] + dsource_llh
    
    # Generate offset target at same height
    target_llh = np.zeros((3, nsec))
    target_llh[:, 0] = source_llh[:, nsec-1]
    target_llh[2, 0] = 0
    dtarget_llh = -4 * np.array([0.00002, 0.00001, 0])
    
    for n in range(1, nsec):
        target_llh[:, n] = target_llh[:, n-1] + dtarget_llh
    
    # Calculate source positions in target_tcs system
    source_tcs = llh2tcsT(source_llh, target_llh)
    range1 = np.sqrt(source_tcs[0, :]**2 + source_tcs[1, :]**2 + source_tcs[2, :]**2)
    bearing1 = np.arctan2(source_tcs[0, :], source_tcs[1, :])
    
    # Calculate target positions in source_tcs system
    target_tcs = llh2tcsT(target_llh, source_llh)
    range2 = np.sqrt(target_tcs[0, :]**2 + target_tcs[1, :]**2 + target_tcs[2, :]**2)
    bearing2 = np.arctan2(target_tcs[0, :], target_tcs[1, :])
    
    # Plot 1: Range and bearing comparison
    fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    ax1.plot(range1 / 1000, 'b.', label='Source in target TCS', markersize=4)
    ax1.plot(range2 / 1000, 'ro', label='Target in source TCS', markersize=4)
    ax1.grid(True)
    ax1.set_ylabel('Target range (km)')
    ax1.set_title('Switch observer & target')
    ax1.legend()
    
    ax2.plot(bearing1 / dtr, 'b.', label='Source in target TCS', markersize=4)
    ax2.plot(bearing2 / dtr, 'ro', label='Target in source TCS', markersize=4)
    ax2.grid(True)
    ax2.set_ylabel('Target bearing (deg)')
    ax2.set_title('Bearing changes 180 deg')
    ax2.legend()
    
    # Coordinate transformations
    source1_XYZ = tcs2ecfT(source_tcs, target_llh)
    source1_llh = ecf2llhT(source1_XYZ)
    source2_llh = tcs2llhT(source_tcs, target_llh)
    
    target1_XYZ = tcs2ecfT(target_tcs, source_llh)
    target1_llh = ecf2llhT(target1_XYZ)
    
    # Plot 2: Latitude and longitude from TCS
    fig2, ax3 = plt.subplots(figsize=(10, 8))
    
    ax3.plot(target_llh[0, :] / dtr, target_llh[1, :] / dtr, 'r', 
             linewidth=2, label='Target original')
    ax3.plot(source_llh[0, :] / dtr, source_llh[1, :] / dtr, 'b', 
             linewidth=2, label='Source original')
    ax3.plot(target1_llh[0, :] / dtr, target1_llh[1, :] / dtr, 'r.', 
             markersize=6, label='Target from TCS')
    ax3.plot(source1_llh[0, :] / dtr, source1_llh[1, :] / dtr, 'b.', 
             markersize=6, label='Source from TCS (ECF)')
    ax3.plot(source2_llh[0, :] / dtr, source2_llh[1, :] / dtr, 'k.', 
             markersize=6, label='Source from TCS (direct)')
    
    ax3.grid(True)
    ax3.set_xlabel('Latitude (deg)')
    ax3.set_ylabel('Longitude (deg)')
    ax3.set_title('Latitude and longitude from TCS')
    ax3.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main() 