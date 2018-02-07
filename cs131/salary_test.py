# Program:  salary.py
# Class:    cs131
# Date:     9/5/14
# Author:   Joel Ristvedt

# Description: This program will ask for the base salary, the bonus per
# carpet sold, the number of carpets sold, percent of commission, and the
# total monthly sales from the user. The program will then calculate and 
# display the total monthly salary to the user. 

# Functions

def Instructions():
    """Print the title of the program and instructions for the user."""

    print()
    print('Salary')
    print('This program accepts values for the base salary, the bonus per')
    print('carpet sold, the number of carpets sold, percent of commision,')
    print('and the total monthly sales. Using this information, the program')
    print('will evaluate the total monthly salary.')

def Display_Results():
    """Prints the results.""" 

    print()
    
    print('Base salary               ${:>10}'.format('{:.2f}'.format(base_salary)))

    print()

    print('Bonus per carpet          ${:>10}'.format('{:.2f}'.format(carpet_bonus)))
    print('Quantity of carpets        {:>10}'.format(carpet_quantity))
    print('Total bonus salary        ${:>10}'.format('{:.2f}'.format(bonus_salary)))

    print()

    print('Total sales               ${:>10}'.format('{:.2f}'.format(monthly_sales)))
    print('Commission rate           {:>10}%'.format(commission))
    print('Total commission          ${:>10}'.format('{:.2f}'.format(total_commission)))

    print()
    print('Total monthly salary      ${:>10}'.format('{:.2f}'.format(total_salary)))


def Main():
    """Display the instructions, get the five values needed to complete
       the evaluation of the total monthly sales from the user, evaluate
       the bonus_salary, commission, and finally the total monthly salary
       and print it to the terminal.

       carpet_bonus = number from the user to indicate the ammount of money
                      rewarded for each carpet sale
       carpet_quantity = a number from the user to indicate the ammount of
                         carpets sold in the month
       bonus_salary = the final ammount gained from carpet sale bonus
       monthly_sales = number from the user indicating the ammount of money
                       made from sales that month
       commission = the percentage (entered as x not .xx) of monthly sales
                    rewarded to to the salesman
       total_commission = the final ammount gained from the commission of
                          monthly sales
       base_salary = a number from the user indicating the starting monthly
                     salary of the salesman
       total_salary = the final sum of the base_salary, total_commission,
                      and bonus_salary that is displayed at the end 
    """

    Instructions()

    print()

    base_salary = float(input('What is the base salary? '))
    carpet_bonus = float(input('What is the carpet bonus? '))
    carpet_quantity = float(input('How many carpets were sold? '))
    commission = float(input('What is the commission rate? '))
    monthly_sales = float(input('What is the total monthly sales? '))

    bonus_salary = carpet_bonus * carpet_quantity
    total_commission = monthly_sales * commission / 100
    total_salary = base_salary + total_commission + bonus_salary

    Display_Results()

# Main Program

Main()
