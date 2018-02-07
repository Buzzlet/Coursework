# Program: count_john.py
# Author:  Joel Ristvedt
# Date:    04/25/2015
# Class:   CS141

from List import List

STOP_WORDS = ['a', 'an', 'the']

def delete_stop_words(list, wordset):
    """ Given a list and a list of words to delete from the list this deletes
        those words from the list
       Params: 
        list - the base list
        wordset - the list of words to delete from list
       Returns: None
    """
    for word in wordset:
        list.delete(word)


def fill_list_file(list, file):
    """ Given a file name and a list this populates the list with words from
        the file
       Params: 
        list - list for population
        file - name of file for data to populate the list with
       Returns: None
    """
    # Local Variables
    # data = data from the file
    
    data = open(file)
    for line in data:
        for word in line.split():
            list.insert(word)
        

def eval_from_file():
    """ Gets files from the user and creates a list containing all the words
        in the file, prints the list, deletes the stop words, prints the list
        again and the statistics of the number of words until the user wants to
        stop
       Params: None
       Returns: None
    """
    # Local Variables
    # done - the state of whether the user wants to continuing entering files
    # file - name of file
    # word_list - list of words from the file
    # answer - string of 'n' or 'N' if the user wants to stop
    
    done = False
    while done == False:
        file = input('What is the name of the text file? ')
        
        word_list = List()
        fill_list_file(word_list, file)
        
        word_list.print_list()
        
        print()
        print("List without stop words:")
        delete_stop_words(word_list, STOP_WORDS)
        word_list.print_list()
        
        print()
        print("Number of unique words: " + str(word_list.length))
        print("Number of processed words: " + str(word_list.items))
        print()
        
        answer = input('Would you like to enter another file (y,n)? ')
        done = (answer == 'n' or answer == 'N')
          

def Main():
    """ """
    eval_from_file()
        

# Main function call
if __name__ == '__main__':
    Main()