# File name: my_module.py

# Description: These are the separate functions that I would rather not
#              bother writing everytime I need them and instead can import
#              them into the code to be used.

# Imports
import math

def Round(float):
    """Takes a float and rounds it up or down based on if the decimal is
       greater than or less than .5

       returns integer value
    """
    integer = math.floor(float + 0.5)
    return integer


