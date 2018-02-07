# Program: List.py
# Author:  Joel Ristvedt
# Date:    04/25/2015
# Class:   CS141

from ListNode import ListNode

class List(object):
    """ A dynamic singly linked list. """
    
    def __init__(self):
        """ Makes a List. """
        self.head = None
        self.items = 0
        self.length = 0
        
        
    def insert(self, value):
        """ Given a word to put in the List, insert creates a ListNode and 
            links it up to the lexicographically correct place
           Params: 
            value - a comparable object to be inserted into the List
           Returns: None
        """
        # Local Variables
        # q - the previous ListNode
        # p - the current ListNode
        # x - the new ListNode
        # done - the state of whether value has been successfully inserted
        
        q = None
        p = self.head
        done = False
        while not done:
            # Empty list
            if self.head == None:
                x = ListNode(value)
                self.head = x
                self.length += 1
                done = True
            # Insert at the end
            elif p == None:
                x = ListNode(value)
                q.next = x
                self.length += 1
                done = True
            # Already in list
            elif p.data == value:
                p.count += 1
                done = True
            # Insert a new value into an already made list
            elif value < p.data:
                # Insert at front
                if p == self.head:
                    x = ListNode(value)
                    self.head = x
                    x.next = p
                    self.length += 1
                    done = True
                # Insert between two nodes
                else:
                    x = ListNode(value)
                    q.next = x
                    x.next = p
                    self.length += 1
                    done = True
            # if none of these, move on to the next node
            else:
                q = p
                p = p.next
        self.items += 1
        
        
    def delete(self, value):
        """ Given a word to deleted from the List, delete rewires the list to
            ignore the deleted value
           Params: 
            value - a comparable object to be deleted from the List
           Returns: None
        """
        # Local Variables
        # q - the previous ListNode
        # p - the current ListNode
        # done - the state of whether value has been successfully deleted
        
        q = None
        done = False
        p = self.head
        while not done:
            
            # the List is empty
            if self.head == None:
                done = True
            # the loop fell off the end
            elif p == None:
                done = True
            # p is the ListNode to delete
            elif value == p.data:
                # first node
                if p == self.head:
                    self.head = p.next
                    done = True
                # a middle node
                elif p.next != None:
                    q.next = p.next
                    done = True
                # end node
                elif p.next == None:
                    q.next = None
                    done = True
            # if none of these are true, look at the next node
            else:
                q = p
                p = p.next
        
        
    def print_list(self):
        """ Follows the list having every ListNode print itself
           Params: None
           Returns: None
        """
        # Local Variables
        # p = the current ListNode
        
        p = self.head
        while p != None:
            p.print_node()
            p = p.next
    
    
    def is_in_list(self, value):
        """ Given a value, is_in_list searches the List for the value and 
            returns true if it is in the List and false if it is not
           Params:
            value - the value to search for in the List
           Returns:
            is_in_list - a boolean value corresponding to value's presence in
                         the list
        """
        # Local Variables
        # is_in_list - a boolean value corresponding to value's presence in the
        #              list
        # p - the current ListNode

        is_in_list = False
        p = self.head
        while is_in_list == False and p != None:
            if value == p.data:
                is_in_list = True
            p = p.next
            
        return is_in_list
    
    
    
