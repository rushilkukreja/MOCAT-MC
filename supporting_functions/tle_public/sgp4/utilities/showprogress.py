def showprogress(j):
    """
    Display progress indicators.
    
    Parameters:
    -----------
    j : int
        Current iteration number
    """
    if j % 10 == 0:
        print('*', end='')
    else:
        print('.', end='')
    
    if j % 50 == 0:
        print() 