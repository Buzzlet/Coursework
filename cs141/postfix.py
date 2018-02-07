# Program: postfix.py
# Author:  Joel Ristvedt
# Date:    04/01/2015
# Class:   CS141

from Stack import Stack

def precedence(char):
    """ Given an allowable operator character, an integer precedence is 
        returned
       Params:
        char - an operator character 
       Returns:
        precedence - an integer corresponding to the order of operations
                     precedence of char
    """
    precedence = None
    if char == '(':
        precedence = 1
    if char in '-+':
        precedence = 2
    elif char in '*/':
        precedence = 3
    elif char == '^':
        precedence = 4
    return precedence



def empty_stack(stack):
    """ Pops all items from the given stack until the character '(', makes a
        string of popped items and pops the '(' character
       Params:
        stack - a stack object to empty
       Returns:
        popped_items - a string of operators popped from the stack
    """
    popped_items = ''
    while stack.is_empty() == False and stack.peek() != '(':
        popped_items += stack.pop()
    stack.pop()
    return popped_items


def infix_to_postfix(infix_string):
    """ Takes an infix string and returns the postfix equivalent string
       Params:
        infix_string - a string of an expression in infix notation
       Returns:
        postfix_string - the postfix string equivalent of the given infix 
                         string
    """
    # Local Variables
    # operator_stack - a stack for storing operators (and '(')
    
    postfix_string = ''
    operator_stack = Stack(len(infix_string))
    
    for char in infix_string:
        # Immediately move any operands to the output
        if char in '0123456789':
            postfix_string += char
    
        elif char == '(':
           operator_stack.push(char)
           
        # Empty the operator stack until the first '('
        elif char == ')':
            postfix_string += empty_stack(operator_stack)
            
        if char in '+-*/^':
            # Empty the operator stack until either the stack is empty, the 
            # precedence of the character operator is greater than the top of 
            # the stack, or both the top of the stack and the character are '^'
            while (operator_stack.is_empty() == False and 
            precedence(char) <= precedence(operator_stack.peek()) and 
            not (precedence(char) == 4 and 
            precedence(operator_stack.peek()) == 4)):
                postfix_string += operator_stack.pop()
            # Always move the current operator to the top of the operator stack
            operator_stack.push(char)
    # empty the operator stack if there are any left over
    postfix_string += empty_stack(operator_stack)

    return postfix_string
    
    
def user_input():
    """ A loop that continuously asks for a mathematical expression using 
        binary operators and printing the postfix expression until the user
        wants to end.
        Params:
         None
        Returns:
         None
    """
    # Local Variables
    # answer - string storing the answer of the user about if they'd like to 
    #          finish entering expressions
    # done - boolean corresponding to the state of the loop
    # infix_string - string of an expression in infix format
    # postfix_string - string of infix_string in postfix format
    
    done = False
    while not done:
        infix_string = input('Enter an infix expression to convert to postfix'+
                        ' (max of 50 characters and single digit operands): ')

        postfix_string = infix_to_postfix(infix_string)
        print("Infix:    {:50}".format(infix_string))
        print("Postfix:  {:50}".format(postfix_string))
        answer = input('Would you like to enter another expression (y/n)? ')
        done = (answer == 'n' or answer == 'N')
    
    
def file_input():    
    """ Reads mathematical expressions in infix notation from a file and prints 
        the postfix expression equivalent until the end of the file
        Params:
         None
        Returns:
         None
    """
    # Local Variables
    # data - data of the file submitted by the user
    # postfix_string - string of infix_string in postfix format
    
    data = open(input('What is the name of the file for conversion? '))
    for line in data:
        line = line.strip('\n')
        postfix_string = infix_to_postfix(line)
        print("Infix:    {:50}".format(line))
        print("Postfix:  {:50}".format(postfix_string))
    
    
def Main():
    """ Order of events to happen upon execution """
    #file_input()
    user_input()
    

# Main function call
if __name__ == '__main__':
    Main()
    
    
