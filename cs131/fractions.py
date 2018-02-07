# Program: fractions.py
# Class:   cs131
# Date:    11/21/14
# Author:  Joel Ristvedt

# Description: This program offers a menu to the user and will continue 
# offering until the user wants to stop. Every time the user choses a menu 
# option, the program will complete the task of that choice. This progarm will
# get two fractions and is able to do basic math operations between the two
# fractions.

# Imports

import Fraction

# Constants

QUIT_CHOICE = 8

# Functions

def Instructions():
    """Prints the name of the program and instructions"""
    print()
    print('Fractions')
    print('The fractions program opens a menu for you to choose an item to do.')
    print('You can enter two fractions and do calculations between them using')
    print('the menu options. The fractions should be entered as an integer, a') 
    print('forward slash, and another integer. The denominators should not ')
    print('be zero. ')       

def Get_Fraction():
    """
    """
    # numerator_str - the string of the numerator
    # denominator_str - the string of the denominator
    numerator_str, denominator_str = input('What is the fraction '+
    '(separate numbers with a forward slash)? ').split('/')
    fraction = Fraction.Fraction(int(numerator_str),
                int(denominator_str))
    return fraction

def Display_Menu():
    """Displays a menu and gets a menu choice from the user
       parameters: none
       returns:
       choice - an integer representing the menu choice of the user
    """
    choice = 0
    while choice < 1 or choice > QUIT_CHOICE:
        print()
        print('Menu')
        print('1. Show instructions')
        print('2. Enter the first fraction')
        print('3. Enter the second fraction')
        print('4. Add the fraction')
        print('5. Subtract second fraction from first fraction')
        print('6. Multiply the fractions')
        print('7. Divide first fraction by second fraction')
        print('8. Quit')
        print()
        choice = int(input('What do you want to do (enter option number)? '))
        if choice < 1 or choice > QUIT_CHOICE:
            print()
            print('\aPlease enter a value from 1 to ', QUIT_CHOICE,'.', sep='')
    return choice

def Do_Choice(choice, fraction1, fraction2):
    """Executes the menu choice of the user
       parameters:
       choice - an integer representing the menu choice of the user
       fraction1 - the first fraction
       fraction2 - the second fraction
       returns:
       fraction1 - the first fraction
       fraction2 - the second fraction
    """
    # sum - the sum of the two entered fractions
    # difference - the difference of the two entered fractions
    # product - the product of the two entered fractions
    # quotient - the quotient of the two entered fractions
    if choice == 1:
        Instructions()
    if choice == 2:
        print()
        fraction1 = Get_Fraction()
    if choice == 3:
        print()
        fraction2 = Get_Fraction()
    if choice == 4:
        sum = fraction1 + fraction2
        print()
        print(fraction1.To_String(),'+', fraction2.To_String(), '=', 
              sum.To_String())
    if choice == 5:
        difference = fraction1 - fraction2
        print()
        print(fraction1.To_String(),'-', fraction2.To_String(), '=', 
              difference.To_String())
    if choice == 6:
        product = fraction1 * fraction2
        print()
        print(fraction1.To_String(),'*', fraction2.To_String(), '=', 
              product.To_String())
    if choice == 7:
        quotient = fraction1 / fraction2
        print()
        print(fraction1.To_String(),'/', fraction2.To_String(), '=', 
              quotient.To_String())
    if choice == 8:
        print()
    
    return fraction1, fraction2

def Main():
    """Continues displaying the menu and executing the chosen choice until
       the user wants to quit
       parameters: none
       returns: none
    """
    # Local variables
    # fraction1 - the first fraction that is by default 1/1
    # fraction2 - the second fraction that is by default 1/1
    # choice - the menu choice of the user

    fraction1 = Fraction.Fraction()
    fraction2 = Fraction.Fraction()
    choice = 0
    while choice < QUIT_CHOICE:
        choice = Display_Menu()
        fraction1, fraction2 = Do_Choice(choice, fraction1, fraction2)
        
# Main
Main()
