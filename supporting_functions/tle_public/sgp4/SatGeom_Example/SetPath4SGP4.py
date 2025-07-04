import sys
import os
from tkinter import Tk, filedialog

def set_path_for_sgp4():
    """
    Set up the environment for Satellite Orbit Computation in Python.
    Adds required directories to sys.path.
    Prompts user to select GPS_CoordinateXforms and IGRF directories if needed.
    """
    current_directory = os.getcwd()
    path2codes = os.path.dirname(current_directory)
    
    # Add utilities and SGP4 directories
    sys.path.append(os.path.join(path2codes, 'utilities'))
    sys.path.append(os.path.join(path2codes, 'SGP4'))
    
    # Prompt user for GPS_CoordinateXforms and IGRF directories
    root = Tk()
    root.withdraw()
    ff = filedialog.askdirectory(title='Select GPS_CoordinateXforms directory')
    if ff:
        sys.path.append(ff)
    ff = filedialog.askdirectory(title='Select IGRF directory')
    if ff:
        sys.path.append(ff)

if __name__ == '__main__':
    set_path_for_sgp4() 