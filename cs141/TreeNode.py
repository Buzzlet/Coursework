# Program: ListNode.py
# Author:  Joel Ristvedt
# Date:    04/25/2015
# Class:   CS141

class TreeNode(object):
    """ An object that encapsulates one item in a binary search tree. """
    
    def __init__(self, word):
        """ Makes a TreeNode object. """
        self.data = word
        self.left = None
        self.right = None
        self.count = 1
    
    
    def print_node(self):
        """ Prints the data and occurrence of the data.
           Params: None
           Returns: None
        """
        print('{:15}{:3}'.format(self.data, self.count))