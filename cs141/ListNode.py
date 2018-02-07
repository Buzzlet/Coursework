# Program: ListNode.py
# Author:  Joel Ristvedt
# Date:    04/25/2015
# Class:   CS141

class ListNode(object):
    """ An object that encapsulates one item in a singly linked list. """
    
    def __init__(self, word):
        """ Makes a ListNode object. """
        self.data = word
        self.next = None
        self.count = 1
        
    def print_node(self):
        """ Prints the data and occurrence of the data.
           Params: None
           Returns: None
        """
        print('{:15}{:3}'.format(self.data, self.count))
        