"""
----------------------------------------------------------------------------

    getintda.py

    This function finds the integer equivalent of the 3 character string
    representation of the day of the week.

    Author        : David Vallado (original MATLAB)
    Python port   : OpenAI Assistant, 2024

    Inputs:
        daystr    - day name string                'sun','mon' ...

    Outputs:
        dayn      - integer day equivalent         1 .. 7

----------------------------------------------------------------------------
"""

def getintda(daystr):
    # Implementation
    daytitle = ['sun', 'mon', 'tue', 'wed', 'thr', 'fri', 'sat']
    
    try:
        dayn = daytitle.index(daystr.lower()) + 1
        return dayn
    except ValueError:
        raise ValueError(f"Unknown day string: {daystr}") 