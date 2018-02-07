# Program: List.py
# Author:  Joel Ristvedt
# Date:    04/25/2015
# Class:   CS141

from TreeNode import TreeNode

class Tree(object):
    """ A binary search tree. """
    
    def __init__(self):
        """ Makes a Tree. """
        self.root = None
        self.size = 0
       
        
    def insert_ptr(self, ptr, value):
        """ Given a value it determines whether it belongs in the tree's left
            subtree or its right subtree and then inserts it there using 
            recursion
           Params:
            ptr - a pointer to the current TreeNode
            value - value to insert into the tree
           Returns: None
        """
 
        # Tree is empty
        if self.root == None:
            self.root = TreeNode(value)
        # Already in the Tree
        elif value == ptr.data:
            ptr.count += 1
        # Insert somewhere in the left subtree
        elif value < ptr.data:
            # There is no left subtree
            if ptr.left == None:
                ptr.left = TreeNode(value)
            # There is already a left subtree
            else:
                self.insert_ptr(ptr.left, value)
        # Insert somewhere in the right subtree
        else:
            # There is no right subtree
            if ptr.right == None:
                ptr.right = TreeNode(value)
            # There is already a right subtree
            else:
                self.insert_ptr(ptr.right, value)
                
        
    def insert(self, value):
        """ A pretty auxiliary method to run insert_ptr with an initial pointer
           Params: 
            value - value to be inserted into the tree
           Returns: None
        """
        self.insert_ptr(self.root, value)
        self.size = self.update_size()
            
            
    def update_size_ptr(self, ptr):
        """ Updates the size of the tree by counting the size of the left
            subtree and the right subtree using recursion and adding them 
            together to return the final size of the tree
           Params:
            ptr - the pointer to the current TreeNode
           Returns: 
            count - the current count of TreeNodes in the tree
        """
        # Local Variables
        # count - the count of how many TreeNodes are in the tree
        
        count = 1
        # If the tree isn't empty
        if ptr != None:
            # If there is a left subtree
            if ptr.left != None:
                # Add the size of the left subtree to the count
                count += self.update_size_ptr(ptr.left)
            # If there is a right subtree
            if ptr.right != None:
                # Add the size of the right subtree to the count
                count += self.update_size_ptr(ptr.right)
        return count
    
    
    def update_size(self):
        """ A pretty auxiliary method to run update_size_ptr with an initial
            pointer
           Params: None
           Returns: the size of tree
        """
        return self.update_size_ptr(self.root)
        
        
    def print_tree_ptr(self, ptr):
        """ Prints everything in the left subtree, the node being pointed to,
            then everything in the right subtree using recursion
           Params:
            ptr - pointer to the current node
           Returns: None
        """
        if ptr != None:
            self.print_tree_ptr(ptr.left)
            ptr.print_node()
            self.print_tree_ptr(ptr.right)
        
        
    def print_tree(self):
        """ A pretty auxiliary method to run print_tree_ptr with an initial
            pointer
            Params: None
            Returns: None
        """
        self.print_tree_ptr(self.root)
    