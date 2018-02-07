# Constants
PI = 3.14159

def Instructions():
    """Print the title, purpose, required information and results for the
       program.
    """

    print()
    print('Circumference')
    print('This program will accept a radius for a circle and print')
    print('the circumference.')

def Ask_Radius():
    """Ask the user for the radius of a circle.
       returns the users radius.
    """
    print()
    radius = float(input('What is the radius of the circle? '))
    return radius

def Calc_Circumference(radius):
    """Calculate the circumference for the given radius
       radius - radius for any circle
       returns the circumference for the radius
    """
    circumference = 2 * PI * radius
    return circumference    

def Print_Circumference(radius, circumference):
    print()
    print('A circle with a radius of', radius)
    print('has a circumference of {:.1f}'.format(circumference), '.', sep='')

def Main():
    Instructions()
    radius = Ask_Radius()
    Print_Circumference(radius, Calc_Circumference(radius))


Main()
