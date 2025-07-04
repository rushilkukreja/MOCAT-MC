import os
import tkinter as tk
from tkinter import filedialog

def pickfile(filter_pattern='*.*', title='Select File to Open', indir=None, permission='r'):
    """
    Simplify file selection interface.
    
    Parameters:
    -----------
    filter_pattern : str, optional
        File filter pattern (default: '*.*')
    title : str, optional
        Dialog title (default: 'Select File to Open')
    indir : str, optional
        Initial directory (default: None)
    permission : str, optional
        File permission mode ('r' for read, 'w' for write, default: 'r')
    
    Returns:
    --------
    filename : str
        Selected file path, or 0 if cancelled
    """
    # Note: This is a simplified version that uses tkinter file dialog
    # The original MATLAB version has more complex directory handling
    
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    if permission.lower() == 'w':
        filename = filedialog.asksaveasfilename(
            title=title,
            filetypes=[('All files', filter_pattern)],
            initialdir=indir
        )
    else:
        filename = filedialog.askopenfilename(
            title=title,
            filetypes=[('All files', filter_pattern)],
            initialdir=indir
        )
    
    if not filename:
        return 0
    
    return filename 