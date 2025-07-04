import sys
import os

def setup_python_path():
    """
    Set up Python path for satellite orbit computation.
    This is the Python equivalent of the MATLAB pathdef.m file.
    Adds necessary directories to sys.path for the satellite geometry tools.
    """
    # Get the current directory
    current_dir = os.getcwd()
    
    # Define the base paths (adjust these as needed for your system)
    base_paths = [
        # Add your specific paths here, similar to the MATLAB version
        # Example paths (modify these for your system):
        os.path.join(current_dir, '..', 'utilities'),
        os.path.join(current_dir, '..', 'SGP4'),
        os.path.join(current_dir, '..', 'GPS_Xforms', 'GPS_CoordinateXforms'),
        os.path.join(current_dir, '..', 'IGRF11', 'IGRF'),
        os.path.join(current_dir, '..', 'igrf', 'datfiles'),
        os.path.join(current_dir, '..', 'vallado'),
    ]
    
    # Add paths to sys.path if they exist
    for path in base_paths:
        if os.path.exists(path) and path not in sys.path:
            sys.path.append(path)
            print(f"Added to path: {path}")
    
    # You can also add environment-specific paths here
    # For example, if you have specific installations:
    # sys.path.append('/path/to/your/specific/installation')
    
    print("Python path setup complete.")
    print(f"Current sys.path length: {len(sys.path)}")

def get_python_path():
    """
    Return the current Python path as a string (similar to MATLAB's pathdef function).
    """
    return os.pathsep.join(sys.path)

if __name__ == '__main__':
    setup_python_path()
    print("\nCurrent Python path:")
    for i, path in enumerate(sys.path):
        print(f"{i+1:3d}: {path}") 