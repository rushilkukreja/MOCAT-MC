import matplotlib.pyplot as plt

def bold_fig():
    """
    Make current plots publication bold.
    
    Notes:
    ------
    Source unknown
    This function modifies the current figure to make it suitable for publication
    by setting bold fonts and thicker lines.
    """
    # orient portrait
    fig = plt.gcf()
    hChildren0 = fig.get_children()
    
    # Filter out uicontrol Children
    hChildren = []
    for child in hChildren0:
        if hasattr(child, 'get_type') and child.get_type() == 'axes':
            hChildren.append(child)
    
    nfigs = len(hChildren)
    
    for i in range(nfigs):
        hAxes = hChildren[i]
        
        hAxes.set_linewidth(1.0)
        hAxes.set_fontweight('bold')
        
        # X label
        hXlabel = hAxes.get_xlabel()
        if hXlabel:
            hAxes.set_xlabel(hXlabel, fontweight='bold')
        
        # Y label
        hYlabel = hAxes.get_ylabel()
        if hYlabel:
            hAxes.set_ylabel(hYlabel, fontweight='bold')
        
        # Z label
        hZlabel = hAxes.get_zlabel()
        if hZlabel:
            hAxes.set_zlabel(hZlabel, fontweight='bold')
        
        # Title
        hTlabel = hAxes.get_title()
        if hTlabel:
            hAxes.set_title(hTlabel, fontweight='bold')
        
        # Children (text and line objects)
        hc = hAxes.get_children()
        for child in hc:
            if hasattr(child, 'get_type'):
                obj_type = child.get_type()
                if obj_type == 'text':
                    child.set_fontweight('bold')
                elif obj_type == 'line':
                    child.set_linewidth(2.0) 