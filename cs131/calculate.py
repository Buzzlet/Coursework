# Program:  calculate.py
# Class:    CS13101
# Date:     29-Aug-2014
# Author:   Joel Ristvedt

# Description: This program asks the user for two numbers. It then
# calculates the sum, difference, product and quotient of the two numbers
# and prints the results in the form of equations.
# x + y = z
# x - y = z
# x * y = z
# x / y = z

# Functions

def Instructions():
    """Print the title of the program and instructions
       for the user.
    """

    print()
    print('Calculate')
    print('This program accepts two numbers and adds, subtracts, multiplies,')
    print('and divides them and displays the result of the equations.')

def Main():
    """Display the instructions, get two numbers from the user,
       add, subtract, multiply and divide them and display the result
       as an equation.

       num1 - Any number from the user, decimal places optional
       num2 - Any number from the user, decimal places optional
       sum  - Result of adding the user's two numbers
       difference - Result of subtracting the user's two numbers
       quotient - Result of dividing the user's two numbers
       product - Result of dividing the user's two numbers
    """

    Instructions()

    print()
    num1 = float(input('What is the first number? '))
    num2 = float(input('What is the second number? '))

    sum = num1 + num2
    difference = num1 - num2
    quotient = num1 / num2
    product = num1 * num2

    print()
    print(num1, ' + ', num2, ' = ', sum)
    print()
    print(num1, ' - ', num2, ' = ', difference)
    print()
    print(num1, ' / ', num2, ' = ', quotient)
    print()
    print(num1, ' * ', num2, ' = ', product)

# Main Program

Main()
