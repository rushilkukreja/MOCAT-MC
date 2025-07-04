import matplotlib.pyplot as plt
import numpy as np

def colors(iDisplay=0):
    """
    Display 31 non-standard colors, the 8 standard colors, and their RGB values.
    
    Parameters:
    -----------
    iDisplay : int, optional
        If 1, displays the colors on white and black backgrounds
    
    Returns:
    --------
    newColors : list
        List of color names and RGB values
    
    Notes:
    ------
    R. Martinez
    10.24.03
    """
    newColors = [
        ['Aquamarine', [0.26, 0.72, 0.73]],
        ['Coral', [0.97, 0.40, 0.25]],
        ['Dark Green', [0.15, 0.25, 0.09]],
        ['Dark Khaki', [0.72, 0.68, 0.35]],
        ['Dark Olive Green', [0.29, 0.25, 0.09]],
        ['Dark Salmon', [0.88, 0.55, 0.42]],
        ['Dark Sea Green', [0.55, 0.70, 0.51]],
        ['Deep Pink', [0.96, 0.16, 0.53]],
        ['Deep Sky Blue', [0.23, 0.73, 1.00]],
        ['Forest Green', [0.31, 0.57, 0.35]],
        ['Ghost White', [0.97, 0.97, 1.00]],
        ['Gold', [0.83, 0.63, 0.09]],
        ['Khaki', [0.68, 0.66, 0.43]],
        ['Lavender Blush', [0.99, 0.93, 0.96]],
        ['Lawn Green', [0.53, 0.97, 0.09]],
        ['Lemon Chiffon', [1.00, 0.97, 0.78]],
        ['Maroon', [0.51, 0.02, 0.25]],
        ['Medium Aquamarine', [0.20, 0.53, 0.51]],
        ['Midnight Blue', [0.08, 0.11, 0.33]],
        ['Mint Cream', [0.96, 1.00, 0.98]],
        ['Navy Blue', [0.08, 0.02, 0.40]],
        ['Old Lace', [0.99, 0.95, 0.89]],
        ['Plum', [0.73, 0.23, 0.56]],
        ['Saddle Brown', [0.49, 0.19, 0.09]],
        ['Salmon', [0.88, 0.55, 0.42]],
        ['Sandy Brown', [0.93, 0.60, 0.30]],
        ['Tan', [0.85, 0.69, 0.47]],
        ['Tomato', [0.97, 0.33, 0.19]],
        ['Turquoise', [0.26, 0.78, 0.86]],
        ['Violet', [0.55, 0.22, 0.79]],
        ['Wheat', [0.95, 0.85, 0.66]]
    ]
    
    standardColors = [
        ['yellow', [1, 1, 0]],
        ['magenta', [1, 0, 1]],
        ['cyan', [0, 1, 1]],
        ['red', [1, 0, 0]],
        ['green', [0, 1, 0]],
        ['blue', [0, 0, 1]],
        ['white', [1, 1, 1]],
        ['black', [0, 0, 0]]
    ]
    
    if iDisplay == 1:
        # First, the new colors on white background
        fig1 = plt.figure()
        plt.plot(0, 0)
        plt.axis([0, 40, 0, 65])
        plt.gca().set_facecolor('white')
        
        for i in range(31):
            plt.text(2, 64-i*2, newColors[i][0], 
                    color=newColors[i][1], fontweight='bold')
            plt.text(10, 64-i*2, str(newColors[i][1]), 
                    color=newColors[i][1], fontweight='bold')
        
        # Then the standard colors
        for i in range(8):
            plt.text(25, i*5, standardColors[i][0], 
                    color=standardColors[i][1], fontweight='bold')
            plt.text(30, i*5, str(standardColors[i][1]), 
                    color=standardColors[i][1], fontweight='bold')
        
        # New colors on black background
        fig2 = plt.figure()
        plt.plot(0, 0)
        plt.axis([0, 40, 0, 65])
        plt.gca().set_facecolor('black')
        
        for i in range(31):
            plt.text(2, 64-i*2, newColors[i][0], 
                    color=newColors[i][1], fontweight='bold')
            plt.text(10, 64-i*2, str(newColors[i][1]), 
                    color=newColors[i][1], fontweight='bold')
        
        # Then the standard colors
        for i in range(8):
            plt.text(25, i*5, standardColors[i][0], 
                    color=standardColors[i][1], fontweight='bold')
            plt.text(30, i*5, str(standardColors[i][1]), 
                    color=standardColors[i][1], fontweight='bold')
    
    return newColors 