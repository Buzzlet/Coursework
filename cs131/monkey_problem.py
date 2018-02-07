# Program:             monkey_problem.py
# Class:               cs131
# Date:                10/8/14
# Author:              Joel Ristvedt

# Description: The Monkey Problem program solves for the number of coconuts
# in the problem in the instructions function over a range designated by the
# user. The user specifies what range to search over, how many sailors they
# want to watch suffer on the island, and whether or not they want to see
# all of the results found.

# Imports

import time

# Functions

def Instructions():
    """Prints the name of the program, story, and instructions.
       Requires none
       Returns none
    """
    
    print()
    print('Monkey Problem')
    print('Five sailors are shipwrecked on an island. Fearing a long stay')
    print('before rescue, they gather together a large pile of coconuts as')
    print('a source of nourishment. Night falls before they are able to')
    print('divide the coconuts among themselves. So the sailors agree to go')
    print('to sleep and divide the pile of coconuts in the morning. During')
    print('the night, one of the sailors wakes up and decides to make sure')
    print('that he gets his fair share of coconuts. He divides the pile into')
    print('five equal piles, one for each sailor, with one coconut left')
    print('over. he hides his pile. pushes the other four piles together and')
    print('tosses the extra coconut to a monkey that is watching him. A')
    print('little while later, a second sailor wakes up and does the same')
    print('dividing and hiding. He ends up with two extra coconuts, which he')
    print('tosses to the monkey. As the night goes by, the other sailors')
    print('wake up in turn to divide the pile of coconuts left over, the')
    print('fourth sailor has four coconuts left over but the fifth sailor')
    print('has no coconuts left over. This works out well, since by the time')
    print('the fifth sailor awakens to divide the pile, it is fairly late')
    print('and the monkey has gone to bed. In the light of day, the pile of')
    print('coconuts is much smaller, but no one points this out since each')
    print('thinks he is responsible. The sailors do one last official')
    print('division in which each sailor receives the same number of')
    print('coconuts with one coconut left over. The sailors agree to give')
    print('the extra coconut to the monkey for breakfast. Each sailor then')
    print('takes his official pile and settles in to wait for rescue.')
    print()
    print('This program will ask for a range of coconuts to search for the')
    print('possible number of coconuts in the pile at the beginning. The')
    print('program will also ask for how many sailors there are on the')
    print('island, as it can solve for a variable number of sailors. Next')
    print('the program will ask if you want to see all of the possible')
    print('number of coconuts in the range entered for the number of sailors')
    print('entered (Enter range like 1337-9001).')
    print()

def Get_Input():
    """Gets the output from the user and returns it
       returns coconut_test, coconut_test_limit, sailors, print_results
       coconut_test = integer
       coconut_test_limit = integer
       sailors = integer
       print_results = boolean
       coconut_test - number to start checking for solutions with
       coconut_test_limit - the highest number to search for solutions
       sailors - number of sailors on the island
       print_results - boolean pertaining to whether the user wants to see the
                       working solutions or not
    """
    # coconut_test_string - string representing the starting number to check
    # answer - users string answer

    coconut_test_string, coconut_test_limit = input(
    'What is the range of coconuts to test? ').split('-')
    coconut_test = int(coconut_test_string)
    coconut_test_limit = int(coconut_test_limit)
    sailors = int(input('How many sailors are on the island? '))
    answer = input('Do you want to see the successful numbers (y/n)? ')
    print_results = (answer == 'y' or answer == 'Y')
    print()
    
    return coconut_test, coconut_test_limit, sailors, print_results

def Calculations(coconut_test, coconut_test_limit, sailors, print_results):
    """Finds the difference between two working solutions
       requires: (int) coconut_test, (int) coconut_test_limit, (int) sailors,
                 (boolean) print_results
       returns:  (int)results
       coconut_test = the number of coconuts under scrutiny
       coconut_test_limit = the highest number of coconuts that will be 
       results - the number of solutions found
       sailors - the number of sailors on the island put there by the malicious
                 user
       print_results - boolean pertaining to whether the user wants to see all
                       the results or just the number of how many results
                       there are
    """
    # first_result = the first working solution
    #                      scrutinized
    # sailor_count = the number of sailors that have taken their secret share
    # plausible - boolean pertaining to whether the coconut value is a 
    #             possible solution based on if the coconut value passed for
    # coconuts_in_pile - the running total of coconuts in the pile
    # leftover_coconuts - coconuts remaining after every secret division that
    #                     get thrown to the monkey
    # coconuts_taken - number taken during every secret division
    results = 0
    while coconut_test < coconut_test_limit:
        sailor_count = 1
        plausible = True
        coconuts_in_pile = coconut_test
        coconuts_taken, leftover_coconuts = divmod(coconuts_in_pile, sailors)
        while sailor_count < sailors and plausible == True:
            if leftover_coconuts == sailor_count:
                coconuts_in_pile -= (leftover_coconuts + coconuts_taken)
                coconuts_taken, leftover_coconuts = divmod(coconuts_in_pile,
                                                           sailors)
            else:
                plausible = False
            sailor_count += 1
        coconuts_in_pile -= (leftover_coconuts + coconuts_taken)
        if (plausible and leftover_coconuts == 0 and coconuts_in_pile % 
            sailors == 1):
            if print_results:
                print(coconut_test)
            results += 1
        coconut_test += 1
    return results

def Print_Output(results, coconut_test, coconut_test_limit, cpu_secs,
                 wall_secs):
    """Prints the number of results over the specified range and the ammount
       of time the calculations took.
       requires: (int)results, (int)coconut_test, (int)coconut_test_limit,
                 (float)cpu_secs, (float)wall_secs
       returns none
    
       results - the number of working solutions found
       coconut_test - the lowest number for checking for solutions
       coconut_test_limit - the highest number for checking for solutions
       cpu_secs - elapsed time it took for the cpu to do calculations
       wall_secs - elapsed time it took for the calculations to be finished
    """
    if results == 0:
        results = 'no'
    s = 's'
    are = 'are'
    if results == 1:
        s = ''
        are = 'is' 
    print()
    print('There ', are,' ', results, ' result', s,' within the range ', coconut_test,
          '-', coconut_test_limit, '.', sep='')
    print('CPU secs: ', '{0:.3f}'.format(cpu_secs))
    print('Elapsed secs: ', '{0:.3f}'.format(wall_secs))
    print()


def Main():
    """Prints the story with the instructions, gets the input from the user,
       starts timing, finds the difference between the first two working 
       solutions and applies that to complete and print all working solutions,
       stops the timing returns output to the user.
       Requires none
       Returns none
    """
    # coconut_test - the lowest number for checking for solutions
    # coconut_test_limit - the highest number for checking for solutions
    # sailors - the number of sailors put on the forsaken island
    # print_results - the boolean pertaining to whether the user wants to see
    #                 the results of just the number of how many results there
    #                 are
    # wall_start - the programs run time at the start of the calculations
    # cpu_start - the time spent computing at the beginning of the 
    #             calcluations
    # second_solution - the second working solution
    # results - the number of working solutions found
    # increment - the difference between any two working solutions
    # wall_stop - the programs run time at the end of the calculations
    # cpu_stop - the time spent computing at the end of the calculations
    # wall_secs - the elapsed time it took the program to complete the calcs
    # cpu_secs - the total time spent computing during the calculations

    Instructions()


    done = False
    while not done:
        coconut_test, coconut_test_limit, sailors, print_results = Get_Input()
    
        wall_start = time.time()
        cpu_start = time.clock()

        results = Calculations(coconut_test, coconut_test_limit, sailors, 
                               print_results)

        wall_stop = time.time()
        cpu_stop = time.clock()

        wall_secs = wall_stop - wall_start
        cpu_secs = cpu_stop - cpu_start
    
        Print_Output(results, coconut_test, coconut_test_limit, cpu_secs,
                     wall_secs)

        answer = input('Would you like to enter numbers again (y/n)? ')
        done = (answer == 'n' or answer == 'N')
        print()
# Main Function
Main()
