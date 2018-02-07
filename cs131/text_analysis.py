# Program:  text_analysis.py
# Class:    cs131
# Date:     11/7/14
# Author:   Joel Ristvedt

# Description:

# Imports

import string

# Constants
WORD_FORMAT = '{:14}'
NUM_FORMAT = '{:>3}'
CHAR_FORMAT = '{:4}'
QUIT_CHOICE = 9
CAPITAL_DIFFERENCE = 32
WORD_GROUPS = 4
CHAR_GROUPS = 8
TABLE = '{:20}'

# Classes

# Functions

def Instructions():
    """Prints the name of the program and instructions"""

    print()
    print('Text_Analysis')
    print('This program presents a menu of options for you do chose what you')
    print('desire. Given a text file, the program is capable of analyzing the')
    print('information and returning statistics back to you.' )

def Get_File():
    """Get a file name from the user
        parameters: none
        returns: 
        name - the file name
    """
    name = input('What is the name of the file (include the file extention)? ')
    return name

def Alphabetize(item_list, frequency_list):
    """
    """
    in_order = False
    while not in_order:
        in_order = True
        index = 0
        while index < len(item_list) - 1:
            if In_Front_Of(item_list[index], item_list[index+1], 0):
                item_list[index], item_list[index + 1] = (item_list[index + 1],
                                                          item_list[index])
                frequency_list[index], frequency_list[index + 1] = (
                frequency_list[index + 1], frequency_list[index])
                in_order = False
            index += 1

def In_Front_Of(string1, string2, char_index):
    """
    """
    in_front_of = False
    if not Conclusive(string1, string2, char_index):
        in_front_of = In_Front_Of(string1, string2, char_index + 1)
    else:
        if Out_Of_Bounds(string1, char_index):
            in_front_of = True
        if Out_Of_Bounds(string2, char_index):
            in_front_of = False
        if len(string1) - 1 >= char_index and len(string2) - 1 <= char_index:

            if Char_In_Front_Of(string1[char_index], string2[char_index]):
                in_front_of = True
            else:
                in_front_of = False
    return in_front_of

def Char_In_Front_Of(char1, char2):
    """
    """
    in_front_of = False
    if ord(char1) - ord(char2) == CAPITAL_DIFFERENCE:
        in_front_of = False
    if ord(char2) - ord(char1) == CAPITAL_DIFFERENCE:
        in_front_of = True
    if abs(ord(char2) - ord(char1)) != CAPITAL_DIFFERENCE:
        if ord(char2) > ord(char1):
            in_front_of = False
        else:
            in_front_of = True
    return in_front_of

def Conclusive(string1, string2, char_index):
    """
    """
    conclusion = False
    if Out_Of_Bounds(string1,char_index) or Out_Of_Bounds(string2,char_index):
        conclusion = True 
    if conclusion == False:
        if ord(string1[char_index]) != ord(string2[char_index]):
            conclusion = True     

    return conclusion

def Out_Of_Bounds(list, index):
    """
    """
    out_of_bounds = False
    if len(list) - 1 > index:
        out_of_bounds = False
    else:
        out_of_bounds = True
    return out_of_bounds

def Into_Char_List(text):
    """Determines the unique characters in a string and their frequency
       parameters:
       text - a string for analysis
       returns:
       unique_char_list - a list of unique characters in the string
       char_frequencies - a list of integers representing the number of 
                          occurrences of the character in the other list
    """
    # char_list - list of all characters
    # index - iterates through char_list

    char_list = list()
    char_frequencies = list()
    for char in text:
        char_list.append(char)
    unique_char_list = list()
    index = 0
    while index < len(char_list):
        if char_list[index] not in unique_char_list:
            unique_char_list.append(char_list[index])
            char_frequencies.append(char_list.count(char_list[index]))
        index += 1
    return unique_char_list, char_frequencies

def Into_Word_List(text):
    """Determines the unique words in a string and their frequencies
       parameters:
       text - a string for analysis
       returns:
       unique_word_list - a list of all unique words in the string
       word_frequencies - a list of integers representing the number of
                          occurrences of the character in the other list
    """
    # word_list - list of all words in the string
    # index - iterates through all words in the string

    word_list = list()
    word_frequencies = list()
    for word in text.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        word_list.append(word)
    unique_word_list = list()
    index = 0
    while index < len(word_list):
        if word_list[index] not in unique_word_list:
            unique_word_list.append(word_list[index])
            word_frequencies.append(word_list.count(word_list[index]))
        index += 1
    return unique_word_list, word_frequencies
    
def Strip_Data(data):
    """Gets rid of unwanted punctuation
       parameters:
       data - text
       return:
       data - changed text
    """
    data = data.replace('#',' ')
    data = data.replace('\n',' ')
    data = data.replace('"','')
    data = data.replace('$',' ')
    data = data.replace('%',' ')
    data = data.replace('&',' ')
    data = data.replace('(',' ')
    data = data.replace(')',' ')
    data = data.replace('*',' ')
    data = data.replace('+',' ')
    data = data.replace(',',' ')
    data = data.replace('-',' ')
    data = data.replace('/',' ')
    data = data.replace(':',' ')
    data = data.replace(';',' ')
    data = data.replace('<',' ')
    data = data.replace('=',' ')
    data = data.replace('>',' ')
    data = data.replace('?',' ')
    data = data.replace('@',' ')
    data = data.replace('[',' ')
    data = data.replace(']',' ')
    data = data.replace('^',' ')
    data = data.replace('_',' ')
    data = data.replace('`',' ')
    data = data.replace('{',' ')
    data = data.replace('|',' ')
    data = data.replace('}',' ')
    data = data.replace('!',' ')
    data = data.replace('?',' ')
    data = data.replace('.',' ')
    data = data.replace('~',' ')
    data = data.replace("'",' ')
    return data


def Process_File(file):
    """Opens and reads the file. Uses the text from file to procure a list
       of all the sentences, lines, words, characters, and their frequencies
       parameters:
       file - name of a text file
       returns:
       line_list - a list of all the lines
       sentence_list - a list of all the sentences
       word_list - a list of all the words 
       char_list - a list of all the characters
       word_frequencies - the frequencies of the words
       char_frequencies - the frequencies of the characters
    """
    # data - all text from file

    sentence_list = list()
    data = open(file).read()
    line_list = list()
    for line in data.split('\n'):
        if len(line) != 0:
            line_list.append(line)
    data = data.replace('?','.')
    data = data.replace('!','.')
    for sentence in data.split('.'):
        sentence = sentence.replace('\n', '')
        sentence_list.append(sentence)
    data = Strip_Data(data)
    word_list, word_frequencies = Into_Word_List(data)
    data = data.replace(' ','')
    char_list, char_frequencies = Into_Char_List(data)
    return (line_list, sentence_list, word_list, word_frequencies, char_list,
           char_frequencies)    


def Print_List(list, freq_list, columns, item_format, freq_format):
    """Prints a list and a list of frequencies using a given number of wanted 
       columns and the formats for each
       parameters:
       list - list of items for printing
       freq_list - frequencies
       columns - number of columns to display the items and frequencies in
       item_format - string representing the format of the item
       freq_format - string representing the format of the number
       returns: none
    """
    # rows - number or rows the table
    # remainder - number of extras 
    # counter - number meaning how many columns have been printed
    # index - the index of the item to be printed
    # counter2 - counter meaining how many rows have been printed
    # index2 - index of the remainders
    # remainder_factor - the number to change the index by based on remainder

    rows = len(list) // columns
    remainder = len(list) % columns
    counter = 0
    index = 0
    counter2 = 1
    remainder_factor = 1
    if remainder != 0:
        remainder_factor = 1
    while index < len(list) and counter2 <= rows:
        while index < len(list) and counter < columns:
            print(item_format.format(list[index]),(
                freq_format.format(freq_list[index])),' ',end='')
            if counter > remainder:
                remainder_factor = 0
            index += rows + remainder_factor
            counter += 1
        print('\n')
        counter = 0
        index = counter2
        counter2 += 1
    index2 = 0
    while index < len(list) and index2 < remainder:   
            print(item_format.format(list[rows*(1+ index2)+index2]),(
                freq_format.format(freq_list[rows*(1+index2)+index2])),' ', end='')
            index2 += 1

def Bubble_Sort(list, list2):
    """Arrange the items in the first list by ascending order
       parameters:
       list - list to sort by
       list2 - second list of values to change based on the first list
       returns: none
    """
    # in_order - true if list is in order and no swapping was done
    # index - counts through the items in the list
    
    in_order = False
    while not in_order:
        in_order = True
        index = 0
        while index < (len(list) - 1):
            if list[index] < list[index + 1]:
                list[index], list[index+1] = list[index+1], list[index]
                list2[index], list2[index+1] = list2[index+1], list2[index]
                in_order = False
            index += 1

    

def Display_Menu():
    """
    """
    choice = 0
    while choice < 1 or choice > QUIT_CHOICE:
        print()
        print('Menu')
        print('1. Identify a file to analyze')
        print('2. Display a list of unique words and their frequency in')
        print('   alphabetical order')
        print('3. Display a list of unique words and their frequency in')
        print('   order by frequency')
        print('4. Display a list of unique characters and their frequency in')
        print('   alphabetical order')
        print('5. Display a list of unique characters and their frequency in')
        print('   order by frequency')
        print('6. Display a summary of the characters in a table')
        print('7. Display a summary of the words in a table')
        print('8. Display a summary of the lines in a table')
        print('9. Quit')
        print()
        choice = int(input('What do you want to do (enter option number)? '))
        if choice < 1 or choice > QUIT_CHOICE:
            print()
            print('\aPlease enter a value from 1 to ', QUIT_CHOICE, '.', 
                  sep = '')
        print()
        return choice

def Char_Analysis(sent_list, char_list, char_freq):
    """
    """
    sent_count = len(sent_list)
    char_count = len(char_list)
    total_char = 0
    for num in char_freq:
        total_char += num
    return sent_count, char_count, total_char    

def Print_Char_Analysis(sent_count, char_count, total_char):
    """
    """
    print(TABLE.format('Sentences: '), CHAR_FORMAT.format(sent_count))
    print(TABLE.format('Unique Characters: '), CHAR_FORMAT.format(
          char_count))
    print(TABLE.format('Characters: '), CHAR_FORMAT.format(total_char))

def Word_Analysis(word_list, word_freq):
    """
    """
    lengths = list()
    for item in word_list:
        lengths.append(len(item))
    dummy_list = [0] * len(lengths)
    Bubble_Sort(lengths, dummy_list)
    longest = lengths[0]
    shortest = lengths[len(lengths) - 1]
    total_length = 0
    for length in lengths:
        total_length += length
    average = total_length / len(lengths)
    word_count = len(word_list)
    total_words = 0
    for num in word_freq:
        total_words += num
    return shortest, longest, average, word_count, total_words

def Print_Word_Analysis(shortest, longest, average, word_count, total_words):
    """
    """
    print(TABLE.format('Shortest Word: '), CHAR_FORMAT.format(shortest))
    print(TABLE.format('Longest Word: '), CHAR_FORMAT.format(longest))
    print(TABLE.format('Average Length: '), '{:>4.1f}'.format(average))
    print(TABLE.format('Unique Words: '), CHAR_FORMAT.format(word_count))
    print(TABLE.format('Words: '), CHAR_FORMAT.format(total_words))    

def Line_Analysis(line_list):
    """
    """
    lengths = list()
    for item in line_list:
        lengths.append(len(item))
    dummy_list = [0] * len(lengths)
    Bubble_Sort(lengths, dummy_list)
    longest_line = lengths[0]
    shortest_line = lengths[len(lengths) - 1]
    total_lengths = 0
    for item in lengths:
        total_lengths += item
    line_average = total_lengths / len(lengths)
    total_lines = len(line_list)
    return shortest_line, longest_line, line_average, total_lines

def Print_Line_Analysis(shortest_line, longest_line, line_average, 
                        total_lines):
    """
    """
    print(TABLE.format('Shortest Line: '), CHAR_FORMAT.format(shortest_line))
    print(TABLE.format('Longest Line: '), CHAR_FORMAT.format(longest_line))
    print(TABLE.format('Average Line: '), '{:>4.1f}'.format(line_average))
    print(TABLE.format('Number of Lines: '), CHAR_FORMAT.format(total_lines))


def Do_Choice(choice, word_list, word_frequencies, char_list, char_frequencies,
              sentence_list, line_list, sent_count, char_count, total_char,
              shortest, longest, average, word_count, total_words,
              shortest_line, longest_line, line_average, total_lines):
    """
    """
    
    if choice == 1:
        file = Get_File()
        (line_list, sentence_list, word_list, word_frequencies, char_list,
        char_frequencies) = Process_File(file)

    elif choice == 2:
        Alphabetize(word_list, word_frequencies)
        Print_List(word_list, word_frequencies, WORD_GROUPS, WORD_FORMAT,
                   NUM_FORMAT)
    elif choice == 3:
        Bubble_Sort(word_frequencies, word_list)
        Print_List(word_list, word_frequencies, WORD_GROUPS, WORD_FORMAT,
                   NUM_FORMAT)
    elif choice == 4:
        Alphabetize(char_list, char_frequencies)
        Print_List(char_list, char_frequencies, CHAR_GROUPS, CHAR_FORMAT,
                   NUM_FORMAT)
    elif choice == 5:
        Bubble_Sort(char_frequencies, char_list)
        Print_List(char_list, char_frequencies, CHAR_GROUPS, CHAR_FORMAT,
                   NUM_FORMAT)
    elif choice == 6:
        sent_count, char_count, total_char = Char_Analysis(sentence_list,
                                             char_list, char_frequencies)
        Print_Char_Analysis(sent_count, char_count, total_char)
    elif choice == 7:
        shortest, longest, average, word_count, total_words = Word_Analysis(
                                                word_list, word_frequencies)
        Print_Word_Analysis(shortest, longest, average, word_count, 
                            total_words)
    elif choice == 8:
        shortest_line, longest_line, line_average, total_lines = Line_Analysis(
                                                                line_list)
        Print_Line_Analysis(shortest_line, longest_line, line_average,
                            total_lines)
    if choice == 9:
        pass

    return (line_list, sentence_list, word_list, word_frequencies, char_list,
               char_frequencies, sent_count, char_count, total_char, )

def Main():
    """
    """
    # Local variables
    
    Instructions()
    choice = 0
    shortest = 0
    longest = 0
    average = 0
    word_count = 0
    total_words = 0
    sent_count = 0
    char_count = 0
    total_char = 0
    line_list = list()
    char_list = list()
    char_frequencies = list()
    sentence_list = list()
    word_list = list()
    word_frequencies = list()
    shortest_line = 0
    longest_line = 0
    line_average = 0
    total_lines = 0

    while choice < QUIT_CHOICE: 
        choice = Display_Menu()
        (line_list, sentence_list, word_list, word_frequencies, char_list, 
        char_frequencies, sent_count, char_count, total_char) = Do_Choice(
        choice, word_list, word_frequencies, char_list, char_frequencies,
        sentence_list, line_list, sent_count, char_count, total_char,
        shortest, longest, average, word_count, total_words, shortest_line,
        longest_line, line_average, total_lines)

# Main
if __name__ == "__main__":
    Main()
