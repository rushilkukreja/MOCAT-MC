"""
Object class filtering for fragments
Assigns appropriate object classes to fragments based on parent object
"""

def filter_objclass_fragments_int(parent_class):
    """
    Assign object class to fragments based on parent object
    
    Parameters:
    -----------
    parent_class : int
        Object class of parent object
        
    Returns:
    --------
    fragment_class : int
        Object class for fragments
    """
    
    # Fragment object class mapping
    # 1 = Satellite, 2 = Debris, 5 = Rocket Body, etc.
    
    if parent_class == 1:  # Satellite
        return 2  # Debris
    elif parent_class == 5:  # Rocket Body
        return 2  # Debris
    elif parent_class == 2:  # Debris
        return 2  # Debris
    else:
        return 2  # Default to debris 