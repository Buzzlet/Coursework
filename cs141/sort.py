
# Program: sort.py
# Author:  Joel Ristvedt
# Date:    1/26/2015
# Class:   CS141

from SortedArray import *

def complete_test():
    """ Comprehensively test combinations of edge cases for all sorts. """
    # Local Variables
    # test_sizes - list of predetermined sizes to test
    # test_sorts - list of predetermined sorts to test
    # test_fills - list of predetermined fills to test
    # sortx - the SortedArray made for the test
    
    # Initialize the default test sizes, sorts, and fills
    test_sizes = [0, 1, 20, 900]
    test_sorts = ["insertion", "shell", "heap", "quick"]
    test_fills = ["random", "ordered", "reverse ordered", 
                  "same numbers"]
    
    # Print the column headings
    print("{:>9} {:>17} {:>6} {:>25}".format("Sort", "Fill", "Size", 
                                             "Sort Status"))
    print("------------------------------------------------------------")
    
    for chosen_sort in test_sorts:
        for chosen_fill in test_fills:
            for chosen_size in test_sizes:
                # Create the array with the specified size
                sortx = SortedArray(chosen_size)
                
                # Fill the array. The deafault is a random fill
                if chosen_fill == "random":
                    sortx.fill_random()
                elif chosen_fill == "ordered":
                    sortx.fill_ordered()
                elif chosen_fill == "reverse ordered":
                    sortx.fill_reverse_ordered()
                elif chosen_fill == "same numbers":
                    sortx.fill_same_num()
                
                # Do the sort. The default is to skip the sort.
                if chosen_sort == "insertion":
                    sortx.insertion_sort()
                elif chosen_sort == "shell":
                    sortx.shell_sort()
                elif chosen_sort == "heap":
                    sortx.heap_sort()
                elif chosen_sort == "quick":
                    sortx.quick_sort()
                else:
                    pass

                print("{:9} {:>17} {:>6} {:>25}".format(chosen_sort, 
                                                         chosen_fill, 
                                                         chosen_size, 
                                                         sortx.check_msg()))

def Main():
    """ Order of events to happen upon execution"""
    complete_test()


# Main Function Call
if __name__ == '__main__':
    Main()
