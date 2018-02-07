# Program: Stack.py
# Author:  Joel Ristvedt
# Date:    04/01/2015
# Class:   CS141

from Array import Array

class Stack(Array):
    """An array where the element put in last is the first one taken out."""
    
    def __init__(self, size=50):
        """ Creates a Stack object. """
        self.top = -1
        super().__init__(size)
        
        
    def pop(self):
        """ Saves the element at the top of the stack, deletes it from the stack
            and returns the element
            Params:
             None
            Returns:
             stack_top - the element at the top of the stack
        """
        if self.top >= 0:
            stack_top = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1
        try:
            return stack_top
        except:
            pass
            
        
    def push(self, new_element):
        """ Put a new element on to the top of the stack
            Params:
             new_element - element to be pushed onto the top of the stack
            Returns:
             None
        """
        self.top += 1
        self.data[self.top] = new_element
        
        
    def is_empty(self):
        """ Returns true if the stack is empty and false if the stack is not """
        return (self.top == -1)
        
        
    def peek(self):
        """ Pops the last element off of the stack, saves it, pushes the last 
            element back onto the stack and returns the saved last element
            Params:
             None
            Returns:
             last_element - element currently at the top of the stack
        """
        last_element = self.pop()
        self.push(last_element)
        return last_element
    
            
