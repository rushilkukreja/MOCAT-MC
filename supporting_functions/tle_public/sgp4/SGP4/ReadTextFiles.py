import os

def ReadTextFiles(filename):
    """
    Read text files.
    
    Parameters:
    -----------
    filename : str
        Name of the file to read
    
    Returns:
    --------
    data : str or list
        File contents
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} not found")
    
    with open(filename, 'r') as f:
        data = f.read()
    
    return data 