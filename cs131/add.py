# Program:  add.py
# Class:    CS13101
# Date:     25-Aug-2014
# Author:   Joel Ristvedt

# Description: This program asks the user for two numbers. It then
# adds them and prints the result in the form of an equation.
#     x + y = z

# Functions

def Instructions():
    """Print the title of the program and instructions
       for the user.
    """

    print()
    print('Add')
    print('This program accepts two numbers, adds them and')
    print('displays the result of an equation.')

def Main():
    """Display the instructions, get two numbers from the user,
       add them and display the result as an equation.

       num1 - Any number from the user, decimal places optional
       num2 - Any number from the user, decimal places optional
       sum  - Result of adding the user's two numbers
    """

    Instructions()

    print()
    num1 = float(input('What is the first number? '))
    num2 = float(input('What is the second number? '))

    sum = num1 + num2

    print()
    print(num1, ' + ', num2, ' = ', sum)
    print()

# Main Program

Main()
