# Program: count_john.py
# Author:  Joel Ristvedt
# Date:    04/25/2015
# Class:   CS141

from Tree import Tree


def fill_list_file(tree, file):
    """ Given a file name and a tree this populates the tree with words from
        the file
       Params: 
        tree - tree for population
        file - name of file for data to populate the list with
       Returns: None
    """
    # Local Variables
    # data = data from the file
    
    words_processed = 0
    data = open(file)
    for line in data:
        for word in line.split():
            tree.insert(word)
            words_processed += 1
    return words_processed


def eval_from_file():
    """ Gets files from the user and creates a tree containing all the words
        in the file, prints the tree and the statistics of the number of words 
        until the user wants to stop
       Params: None
       Returns: None
    """
    # Local Variables
    # done - state corresponding to the if the user wants to enter more files
    # file - name of the file entered
    # john_tree - tree containing the words of John
    # words_processed - the number of words processed
    # answer - string of 'n' or 'N' if the user wants to stop
    
    done = False
    while done != True:
        file = input("What is the name of the text file? ")
        john_tree = Tree()
        words_processed = fill_list_file(john_tree, file)
        john_tree.print_tree()
        print()
        print("Number of unique words: " + str(john_tree.size))
        print("Number of words processed: " + str(words_processed))
        print()
        
        answer = input("Would you like to enter another text file (y/n)? ")
        done = (answer == 'n' or anwer == 'N')


def Main():
    """ Gets a file, puts it in a tree, prints out the tree and some word
        statistics
    """
    eval_from_file()
        

# Main function call
if __name__ == '__main__':
    Main()