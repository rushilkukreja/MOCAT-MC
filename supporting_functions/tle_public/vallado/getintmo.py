"""
----------------------------------------------------------------------------

    getintmo.py

    This function finds the integer equivalent of the 3 character string
    representation of month.

    Author        : David Vallado (original MATLAB)
    Python port   : OpenAI Assistant, 2024

    Inputs:
        monstr    - month name                     'jan','feb' ...

    Outputs:
        mon       - integer month equivalent       1 .. 12

----------------------------------------------------------------------------
"""

def getintmo(monstr):
    # Implementation
    monthtitle = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
                  'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    
    try:
        mon = monthtitle.index(monstr.lower()) + 1
        return mon
    except ValueError:
        raise ValueError(f"Unknown month string: {monstr}") 