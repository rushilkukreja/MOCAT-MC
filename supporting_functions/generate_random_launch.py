"""
Random launch generation function
"""

import numpy as np

def generate_random_launch(param):
    """
    Generate a random launch based on parameters
    
    Parameters:
    -----------
    param : dict
        Simulation parameters
        
    Returns:
    --------
    launch_objects : array
        Array of launched objects
    """
    
    # This is a simplified random launch generator
    # In practice, this would be more sophisticated based on historical data
    
    # Generate random orbital elements
    n_objects = np.random.poisson(5)  # Average 5 objects per launch
    
    if n_objects == 0:
        return []
    
    # Random semi-major axis (LEO range)
    a = np.random.uniform(1.05, 1.2)  # Earth radii
    
    # Random eccentricity
    e = np.random.uniform(0, 0.1)
    
    # Random inclination
    i = np.random.uniform(0, np.pi/2)
    
    # Random other orbital elements
    omega = np.random.uniform(0, 2*np.pi)
    argp = np.random.uniform(0, 2*np.pi)
    M = np.random.uniform(0, 2*np.pi)
    
    # Create launch objects
    launch_objects = []
    for j in range(n_objects):
        # Random mass and radius
        mass = np.random.uniform(100, 1000)  # kg
        radius = np.random.uniform(0.5, 2.0)  # m
        
        # Create object array (simplified format)
        obj = np.array([
            a, e, i, omega, argp, M,  # Orbital elements
            0.0,  # bstar
            mass, radius,  # Physical properties
            0, 1, 0, 0,  # errors, controlled, a_desired, missionlife
            0,  # constellation
            param.get('current_time', 0), 0,  # date_created, launch_date
            0, 0, 0,  # r (will be calculated)
            0, 0, 0,  # v (will be calculated)
            1,  # objectclass (satellite)
            param['maxID'] + j + 1  # ID
        ])
        
        launch_objects.append(obj)
    
    return np.array(launch_objects) 