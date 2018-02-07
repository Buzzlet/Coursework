# Program:    cross_country.py
# Class:      cs131
# Date:       9/12/14
# Author:     Joel Ristvedt

# Description: This program will accept the runners number, the elapsed
# time for the first mile, second mile, and the final elapsed time.
# Using these timestamps, the program will determine the split times of
# each leg of the race. 

# Functions

def Instructions():
    """Print the title of the program and the instructions for the user."""

    print()
    print('Cross Country')
    print('This program accepts the number of the runner, the elapsed time at')
    print('each leg of the race and determines the split time for each')
    print('section of the race. Elapsed times are to be entered in the')
    print('format MM:ss.ms. (Ex. 12:36.92 would be 12 mins 36.92 seconds.)')

def Convert_to_seconds(minutes):
    """Multiplies the amount of minutes by 60 to determine the amount of 
       seconds in the given amount of minutes.
    """
    seconds = minutes * 60
    return seconds

def Main():
    """Display the instructions, get the runner's number, get the elapsed
       times at each leg of the race, split the input into two different 
       variables and use those to calculate the total elapsed seconds at
       each leg, then convert back to minutes and seconds for the output.
    """
    
    # runner_number = number of the runner whose times will be entered and
    #                 is entered by the user

    # time_string1 = the entered characters representing the time it took
    #                the runner to complete mile 1

    # time_string2 = the entered characters representing the time it took
    #                the runner to complete mile 2
    
    # time_string3 = the entered characters representing the time it took 
    #                the runner to complete mile 3

    # mile1_minutes = the number of whole minutes the runner takes to have 
    #                 completed the first mile

    # mile1_seconds = the number of seconds left in the last minute of the
    #                 runner's first mile 

    # mile2_minutes = the number of whole minutes the runner takes to have
    #                 completed the second mile

    # mile2_seconds = the number of seconds left in the last minute of the
    #                 runner's second mile

    # mile3_minutes = the number of whole minutes the runner takes to have
    #                 completed the third mile 

    # mile3_seconds = the number of seconds left in the last minute of the
    #                 runner's third mile

    # mile1_elapsed_seconds = the number of seconds from the beginning of
    #                         the race to the completion of the first mile

    # mile2_elapsed_seconds = the number of seconds from the beginning of
    #                         the race to the completion of the second mile

    # mile3_elapsed_seconds = the number of seconds from the beginning of 
    #                         the race to the completion of the third mile

    # seconds_for_mile2 = the difference between the elapsed seconds at
    #                     mile 1 and mile 2

    # seconds_for_mile3 = the difference between the elapsed seconds at
    #                     mile 2 and mile 3

    # split2_minutes = the number of whole minutes it takes the runner to
    #                  complete the second mile

    # split3_minutes = the number of whole minutes it takes the runner to
    #                  complete the third mile

    # split2_seconds = the remaining number of seconds it took the runner 
    #                  to complete the second mile

    # split3_seconds = the remaining number of seconds it took the runner
    #                  to complete the third mile
    
    # done = boolean variable used to exit the while loop

    # Note: We don't have to determine the number of seconds and minutes
    #       for mile one as they are provided by the user.


    Instructions()

    done = 0

    while not done:
        print()
    
        runner_number = int(input("What is the runner's number? "))
        time_string1 = input('What is the elapsed time at mile 1? ')
        time_string2 = input('What is the elapsed time at mile 2? ')
        time_string3 = input('What is the elapsed time at mile 3? ')
        mile1_minutes, mile1_seconds = time_string1.split(':')
        mile2_minutes, mile2_seconds = time_string2.split(':')
        mile3_minutes, mile3_seconds = time_string3.split(':')
        mile1_minutes = int(mile1_minutes)
        mile2_minutes = int(mile2_minutes)
        mile3_minutes = int(mile3_minutes)
        mile1_seconds = float(mile1_seconds)
        mile2_seconds = float(mile2_seconds)
        mile3_seconds = float(mile3_seconds)

        mile1_elapsed_seconds = Convert_to_seconds(mile1_minutes) + \
                                mile1_seconds
        mile2_elapsed_seconds = Convert_to_seconds(mile2_minutes) + \
                                mile2_seconds
        mile3_elapsed_seconds = Convert_to_seconds(mile3_minutes) + \
                                mile3_seconds
    
        seconds_for_mile2 = mile2_elapsed_seconds - mile1_elapsed_seconds
        seconds_for_mile3 = mile3_elapsed_seconds - mile2_elapsed_seconds

        split2_minutes = int(seconds_for_mile2 // 60)
        split3_minutes = int(seconds_for_mile3 // 60)
        split2_seconds = seconds_for_mile2 % 60
        split3_seconds = seconds_for_mile3 % 60

        print()
    
        print('Times for runner', runner_number)

        print()

        print('Elapsed Times')
        print('Mile 1{:>16}'.format(time_string1))
        print('Mile 2{:>16}'.format(time_string2))
        print('Finish{:>16}'.format(time_string3))

        print()

        print('Split Times')
        print('Split 1{:>15}'.format(time_string1))
        print('Split 2{:>9}'.format(split2_minutes), 
              ':{:.2f}'.format(split2_seconds), sep='')
        print('Split 3{:>9}'.format(split3_minutes),
              ':{:.2f}'.format(split3_seconds), sep='')

        answer = input('Would you like to re-enter values? (Y/N) ')
        done = (answer == 'n' or answer == 'N')

# Main Program

Main()
