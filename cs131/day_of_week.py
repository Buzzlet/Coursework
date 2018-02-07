# Program:         day_of_week.py
# Class:           cs131
# Date:            9/19/14
# Author:          Joel Ristvedt

# Description: This program will accept a date in the format mm/dd/yyyy
# (Ex. 12/12/1984 would be December 12, 1984) and will determine the day of 
# the week on that given day.

# Constants

JANUARY = 1
FEBRUARY = 2
MARCH = 3
APRIL = 4
MAY = 5
JUNE = 6
JULY = 7
AUGUST = 8
SEPTEMBER = 9
OCTOBER = 10
NOVEMBER = 11
DECEMBER =12

SATURDAY = 0
SUNDAY = 1
MONDAY = 2
TUESDAY = 3
WEDNESDAY = 4
THURSDAY = 5
FRIDAY = 6

# Functions

def Instructions():
    """Print the title of the program and the instructions for the user."""

    print()
    print('Day of the Week')
    print('This program will accept the day from the user and will use a ')
    print('series of calculations to determine the day of the week for the')
    print('given day. This day will then be returned to the user. The date')
    print('should be entered in the format month/day/year. (Ex. 3/6/1996')
    print('would represent March 6, 1996.')

def Cast_Out_Sevens(number):
    """Divides the number by seven and returns the remainder"""
    result = int(number) % 7
    return result

def Find_Month_Adjust(month):
    """Compares the month to each of the month's constants and returns
       the month adjustment.
    """
    month_adjustment = 0
    if month == APRIL or month == JULY:
        month_adjustment = 0
    elif month == JANUARY or month == OCTOBER:
        month_adjustment = 1
    elif month == MAY:
        month_adjustment = 2
    elif month == AUGUST:
        month_adjustment = 3
    elif month == FEBRUARY or month == MARCH or month == NOVEMBER:
        month_adjustment = 4
    elif month == JUNE:
        month_adjustment = 5
    elif month == SEPTEMBER or month == DECEMBER:
        month_adjustment = 6
    return month_adjustment

def Find_Century_Adjust(century):
    """Determines which century the date is in and returns the adjustment
       required.
    """
    century_adjustment = 0
    if century == 19:
        century_adjustment = 0
    elif century == 18:
        century_adjustment = 2
    elif century == 17 or century == 21:
        century_adjustment = 4
    elif century == 20:
        century_adjustment = 6
    return century_adjustment

def Is_Leap_Year(century, non_century):
    """Divides the non_century year by 4 and if it is evenly divisible it
       is a leap year. However, if the non_century year is 00, it must
       pass another test in which the century is divided by 4 and if it
       divides evenly then it will return the boolean true otherwise it
       will return false.
    """
    state = False
    if non_century % 4 == 0:
        state = True
    else:
        state = False

    if non_century == 0:
        if century % 4 == 0:
            state = True
        else:
            state = False

    return state            

def Determine_Day(number):
    """Compares the number to each of the day's constants and returns
       a string containing the day.
    """
    if number == SATURDAY:
        return 'saturday'
    elif number == SUNDAY:
        return 'sunday'
    elif number == MONDAY:
        return 'monday'
    elif number == TUESDAY:
        return 'tuesday'
    elif number == WEDNESDAY:
        return 'wednesday'
    elif number == THURSDAY:
        return 'thursday'
    elif number == FRIDAY:
        return 'friday'

def Main():
    """Main displays the instructions, gets the day from the user, breaks 
       down the string input into integers, determines what century date lies
       in and the non-century year then follows strict protocol for 
       determining the day of the week the user entered and then displays
       the day of the week for the user to see.
    """
    # month_string - all characters the user entered before a '/'
    # day_string - all characters the user entered between '/'s
    # year_string - all characters after the last '/'
    # month - the month_string converted into an integer
    # day - the day_string converted into an integer
    # year - the year_string converted into an integer
    # century - the first 2 digits of the year
    # non_century - last 2 digits of the year
    # remainder - what is left over after the non_century year is divided
    #             by 12
    # result - the running calculated number that represents the day of the
    #          week
    # month_adjustment - integer to be added to the result to adjust for 
    #                    the month
    # century_adjustment - integer to be added to the result to adjust for
    #                      the century
    # leap_year_adjustment - integer to be subtracted from the result to 
    #                        adjust for leap years

    Instructions()
    print()
    done = False
    while not done:
        month_string, day_string, year_string = input(
        'What is the date? ').split('/')
        month = int(month_string)
        day = int(day_string)
        year = int(year_string)
        century = year // 100
        non_century = year % 100

        # Step 1
        result = non_century // 12

        # Step 2
        remainder = non_century % 12
        result += remainder

        # Step 3
        result += (remainder // 4)

        # Step 4
        result = Cast_Out_Sevens(result)

        # Step 5
        result += Find_Month_Adjust(month)
 
        # Step 6
        result = Cast_Out_Sevens(result) + day

        # Step 7
        result = Cast_Out_Sevens(result) + Find_Century_Adjust(century)

        # Step 8
        leap_year_adjustment = 0
        if month == JANUARY or month == FEBRUARY:
            if Is_Leap_Year(century, non_century):
                leap_year_adjustment = 1
        result -= leap_year_adjustment

        # Step 9
        if result < 0:
            result += 7

        # Step 10
        result = Cast_Out_Sevens(result)

        print()
        print('The day of the week on ', month, '/', day, '/', year, ' is ',
              Determine_Day(result), '.', sep='')
        print()
        answer = input('Would you like to enter another date (y/n) ? ')
        done = (answer == 'n' or answer == 'N')
        print()

# Main Function
Main()
