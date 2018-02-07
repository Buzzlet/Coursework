# Program:       temperature_analysis.py
# Class:         cs131
# Date:          10/24/4
# Author:        Joel Ristvedt

# Description: The temperature analysis program asks the user for a file to 
# read. The program then reads the temperature information from the file, 
# sorts it based on day, high temperature and low temperature, and finally
# displays the sorted temperatures along with the average low temperature and
# high temperature. The program repeats for as many files as the user wants
# to enter.

# Imports

# Constants
LOW_INDEX = 2
HIGH_INDEX = 1
DAY_INDEX = 0

# Functions

def Instructions():
    """Prints the name of the program and instructions"""
    
    print()
    print('Temperature Analysis')
    print('The temperature analysis program uses a file of temperatures to')
    print('determine the range of temperatures for each day, the average low')
    print('temperature, the average high temperature, and sorts the ')
    print('temperatures based on the day, low temperature, or high ')
    print('temperature and displays them back to you.')

def Get_File():
    """Gets the name of a file from the user
       parameters: none
       returns: 
       name - the name of the file
    """
    print()
    name = input('What is the name of the file (include the file extention)? ')
    return name

def File_Into_List(filename):
    """Iterates through the lines in a file and assigns a list of days, highs,
       and lows into a comprehensive list of all the needed data from the file
       parameters:
       filename - name of file to get the temperatures from
       returns:
       temperatures - the comprehensive list of lists containing each day
                      and its corresponding high and low temperatures
    """
    # data - all of the contents of the entered file
    # line - a single line of the entered file
    # high - the high temperature in each line
    # low - the low temperature in each line
    # day - the day corresponding with the entered temepratures
    # daily_temp - a list containing a day and its temperatures

    temperatures = list()
    data = open(filename)
    day = 1
    for line in data:
        line = line.strip('\n')
        high, low = line.split(' ')
        daily_temp = [day, int(high), int(low)]
        temperatures.append(daily_temp)
        day += 1
    data.close()
    return(temperatures)

def Bubble_Sort(list, sort_index):
    """Arrange the items in the given list in ascending order.
       parameters:
       list - a list of lists
       sort_index - index of the arrays to sort the arrays based on
       returns:
       list - the same list of lists, but sorted in ascending order based
              on the indicated sort_index 
    """
    # in_order - true if list is in order and no swapping was done
    # index - counts through the items in the list
    
    in_order = False
    while not in_order:
        in_order = True
        index = 0
        while index < (len(list) - 1):
            if list[index][sort_index] > list[index + 1][sort_index]:
                list[index], list[index +1] = list[index + 1], list[index]
                in_order = False
            index += 1
    return list
    
def Sort_By_High(list):
    """Sorts a list of lists based on the high temperatures
       parameters:
       list - a list of lists
       returns:
       list - the same list of lists, but sorted by high temperatures
    """
    list = Bubble_Sort(list, HIGH_INDEX)
    return list

def Sort_By_Low(list):
    """Sorts a list of lists based on the low temperatures
       parameters:
       list - a list of lists
       returns:
       list - the same list of lists, but sorted by low temperatures
    """
    list = Bubble_Sort(list, LOW_INDEX)
    return list

def Sort_By_Day(list):
    """Sorts a list of lists based on the day
       parameters:
       list - a list of lists
       returns:
       list - the same list of lists, but sorted by day
    """
    list = Bubble_Sort(list, DAY_INDEX)
    return list

def Find_Means(list):
    """Finds the average temperature for the high temperatures and the low
       temperatures
       parameters:
       list - list of lists
       returns:
       low_mean - the average low temperature
       high_mean - the average high temperagure
    """
    # total_low - the sum of all low temperatures
    # total_high - the sum of all high temperatures
    # index - the index of the list of lists being added into the sum of 
    #         temperatures
  
    total_low = 0
    total_high = 0
    index = 0
    while index < len(list):
        total_low += list[index][LOW_INDEX]
        total_high += list[index][HIGH_INDEX]
        index += 1
    low_mean = total_low / len(list)
    high_mean = total_high / len(list)
    return low_mean, high_mean

def Find_Range(list):
    """Iterates through a list of lists and finds the range between the high
       and low temperature for each day
       parameters:
       list - list of lists
       returns:
       range_list - a list containing lists with the day and temperature range
                    for that day
    """
    # index - the index of the list of lists being checked
    # range_list - the eventual comprehensive list of ranges
    # range - the range for one day
    # range_data - a list containing a day and its range

    index = 0
    range_list = []
    while index < len(list):
        range = abs(list[index][HIGH_INDEX] - list[index][LOW_INDEX])
        range_data = (index+1, range)
        range_list.append(range_data)
        index += 1
    return range_list

def Print_List(list, columns):
    """Iterates through the entered list and format and print the contents
       of the list.
       parameters:
       list - a list of lists
       columns - the number of columns for the contents of each list to be
                 printed in
       returns: none
    """
    # index - index of list being printed
    
    index = 0
    while index < len(list):
        if columns == 3: 
            print('{:>6}'.format(list[index][DAY_INDEX]), end ='')
            print('{:>6}'.format(list[index][HIGH_INDEX]), end ='')
            print('{:>6}'.format(list[index][LOW_INDEX]))
        if columns == 2:            
            print('{:>6}'.format(list[index][DAY_INDEX]), end ='')
            print('{:>6}'.format(list[index][1]))
        index += 1
    
def Print_Headings(title1, title2, title3):
    """Prints up to three titles
       parameters:
       title1 - first string title
       title2 - second string title
       title3 - third string title
       return: none
    """
    print('{:>6}'.format(title1),'{:>5}'.format(title2),'{:>5}'.format(title3))

def Main():
    """Gets a file name from the user, loads the file and interprets the file
       into an array. Based on this array of temperatures and days, main
       finds the range, mean, and sorts by day, high temperatures, and low
       temperatures and prints the results in tables.
    """
    # file - the name of the file to search
    # temp_list - a list of lists with each inner list containing the day,
    #             low temperature, and high temperature
    # low_mean - the average low temperature
    # high_mean - the average high temperature
    # done - the boolean to determine if main should keep looping or not
    # answer - the users answer as to whether they want to enter another
    #          file

    Instructions()

    done = False
    while not done:
        file = Get_File()
        temp_list = File_Into_List(file)

        print()
        print('Temperature Ranges')
        Print_Headings('Day', 'Range', '')
        Print_List(Find_Range(temp_list), 2)

        print()
        print('Sorted by Day')
        Print_Headings('Day', 'High', 'Low')
        Print_List(Sort_By_Day(temp_list), 3)

        print()
        print('Sorted by High Temperatures')
        Print_Headings('Day', 'High', 'Low')
        Print_List(Sort_By_High(temp_list), 3)

        print()
        print('Sorted by Low Temperatures')
        Print_Headings('Day', 'High', 'Low')
        Print_List(Sort_By_Low(temp_list), 3)
    
        print()
        print('Averages')
        Print_Headings('Low', 'High', '')
        low_mean, high_mean = Find_Means(temp_list)
        print('{:>6.1f}'.format(low_mean), '{:>5.1f}'.format(high_mean))
        print()
        
        answer = input(
                'Would you like to enter another file for evaluation (y/n)? ')
        done = (answer == 'n' or answer == 'N')

# Main
if __name__ == "__main__":
    Main()
