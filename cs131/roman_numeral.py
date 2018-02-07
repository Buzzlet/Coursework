# Program:             roman_numeal.py
# Class:               cs131
# Date:                9/30/2014
# Author:              Joel Ristvedt

# Description: The Roman Numeral program accepts an integer value from 1 to
# 3999 and returns to the user a series of Roman numeral characters that 
# correctly represent the number entered by the user

# Functions
def Instructions():
    """Print the title of the program and he instructions for the user."""

    print()
    print('Roman Numeral')
    print("This program asks you for a number and will return the number's")
    print('Roman numeral equivalent back to you. (Ex. Enter 1337, and you')
    print('will get MCCCXXXVII back.)')
    print()

def Determine_Ones_Characters(digit):
    """Based on what the ones digit is this function will return  a 
       Roman numeral character representation of it.
       digit = integer
       returns string
    """
    # ones_digit_string = the string of characters used in Roman numeral
    #                     notation to represent the ones digit
    # digit = the arguement entered into the function that is the number
    #         in the ones place of the number the user entered

    ones_digit_string = ''
    if digit <= 3:
        ones_digit_string = 'I' * digit
    elif digit == 4:
        ones_digit_string = 'IV'
    elif digit == 5:
        ones_digit_string = 'V'
    elif digit >= 6 and digit <= 8:
        ones_digit_string = 'V' + ('I' * (digit - 5))
    elif digit == 9:
        ones_digit_string = 'IX'
    return ones_digit_string
    

def Determine_Tens_Characters(digit):
    """Based on what the tens digit is this function will return a Roman
       numeral character representation of it.
       digit = integer
       returns string
    """
    # tens_digit_string = the string of characters used in Roman numeral 
    #                     notation to represent the tens digit
    # digit = the arguement entered into the function that is the number in
    #         the tens place of the number the user entered    

    tens_digit_string = ''
    if digit <= 3:
        tens_digit_string = 'X' * digit
    elif digit == 4:
        tens_digit_string = 'XL'
    elif digit == 5:
        tens_digit_string = 'L'
    elif digit >= 6 and digit <= 8:
        tens_digit_string = 'L' + ('X' * (digit - 5))
    elif digit == 9:
        tens_digit_string = 'XC'
    return tens_digit_string

def Determine_Hundreds_Characters(digit):
    """Based on what the hundreds digit is this function will return a Roman
       numeral character representation of it.
       digit = integer
       returns string
    """
    # hundreds_digit_string = the string of characters used in Roman numeral
    #                         notation to represent the hundreds digit
    # digit = the arguement entered into the function that is the number in
    #         the hundreds place of the number the user entered

    hundreds_digit_string = ''
    if digit <= 3:
        hundreds_digit_string = 'C' * digit
    elif digit == 4:
        hundreds_digit_string = 'CD'
    elif digit == 5:
        hundreds_digit_string = 'D'
    elif digit >= 6 and digit <= 8:
        hundreds_digit_string = 'D' + ('C' * (digit - 5))
    elif digit == 9:
        hundreds_digit_string = 'CM'
    return hundreds_digit_string

def Determine_Thousands_Characters(digit):
    """Based on what the thousands digit is this function will return a
       Roman numeral character representation of it.
       digit = integer
       returns string
    """
    # thousands_digit_string = the string of characters used in Roman numeral
    #                          notation to represent the thousands digit
    # digit = the arguement entered into the function that is the number in 
    #         the thousands place of the number the user entered

    thousands_digit_string = 'M' * digit
    return thousands_digit_string    
    

def Display_Output(number, ones, tens, hundreds, thousands):
    """Prints the output in sentence form with the Roman numeral 
       representation of the number.
       ones, tens, hudnreds, thousands = strings
       no return / void
    """
    # roman_numeral = the final string of Roman numeral characters that 
    #                 fully represent the number entered by the user
    # number = the arguement entered that is the integer number entered by
    #          the user
    # thousands = the arguement entered that is a string to represent the
    #             thousands Roman numeral  
    # hundreds = the arguement entered that is a string to represent the 
    #            hundreds Roman numeral
    # tens = the arguement entered that is a string to represent the tens
    #        Roman numeral
    # ones = the arguement entered that is a string to represent the ones
    #        Roman numeral

    roman_numeral = thousands + hundreds + tens + ones
    print()
    print('The number', number, 'is equivalent to', roman_numeral,
          'in Roman numeral form.')
    print()

def Main():
    """Splits the number into the different digits and then for each digit
       determines which character representation is appropriate
    """
    # done = boolean variable determining whether the user is done or
    #        would like to continue to run Main again
    # number = the integer number entered by the user
    # two_right_digits = the number of whole hundreds in the given number
    # two_left_digits = the right two digits of the number
    # ones_digit = number in the ones spot
    # tens_digit = number in the tens spot
    # hundreds_digit = number in the hundreds spot
    # thousands_digit = number in the thousand spot
    # ones_string = Roman numeral string representation of the number in 
    #               the ones spot
    # tens_string = Roman numeral string representation of the number in
    #               the tens spot
    # hundreds_string = Roman numeral string representation of the number in
    #                   the hundreds spot
    # thousands_string = Roman numeral string representation of the number in
    #                    the thousands spot
    # answer = string response from the user and determines whether the 
    #          program should end or not
    
    Instructions()
    done = False
    while not done:
        number = int(input('What is the number (1-3999)? '))
        two_right_digits = number % 100
        two_left_digits = number // 100
        ones_digit = two_right_digits % 10
        tens_digit = two_right_digits // 10
        hundreds_digit = two_left_digits % 10
        thousands_digit = two_left_digits // 10

        ones_string = Determine_Ones_Characters(ones_digit)
        tens_string = Determine_Tens_Characters(tens_digit)
        hundreds_string = Determine_Hundreds_Characters(hundreds_digit)
        thousands_string = Determine_Thousands_Characters(thousands_digit)

        Display_Output(number, ones_string, tens_string, hundreds_string,
                       thousands_string)

        answer = input('Would you like to enter another number (y/n)? ')
        done = (answer == 'n' or answer == 'N')
        print()

# Main Function
Main()
