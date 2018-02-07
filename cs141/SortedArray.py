# Program: Sorted_Array.py
# Author:  Joel Ristvedt
# Date:    2/9/2015
# Class:   CS141

from Array import Array
from random import *

class SortedArray(Array):
    """ A fancy array with new abilities """

    def __init__(self,size,default_value=None):
        """ Cretaes a SortedArray object. """
        super().__init__(size,default_value)
        
        
    def count_sums(self):
        """ Saves the current sum and sum of squares of the SortedArray. """
        self.sum = 0
        self.sum_sq = 0
        for i in range(0, self.size):
            self.sum += self.data[i]
        for j in range(0, self.size):
            self.sum_sq += self.data[j]**2


    def fill_random(self, low=-100, high=100):
        """ Fill the SortedArray with values ranging from low to high"""
        for item in range(self.size):
            self.data[item] = randint(low, high)
        self.count_sums()


    def fill_ordered(self):
        """ Populates the SortedArray with numbers of ascending value. """
        for item in range(self.size):
            self.data[item] = item
        self.count_sums()


    def fill_reverse_ordered(self):
        """ Populates the SortedArray with numbers of descending value. """
        for item in range(self.size):
            self.data[item] = self.size - item - 1
        self.count_sums()


    def fill_same_num(self, low=-100, high=100):
        """ Populates the SortedArray with of the same number. """
        # Local Variables
        # rand_num - the randomly selected integer within the range to be
        #            duplicated
        rand_num = randint(low, high)
        for item in range(self.size):
            self.data[item] =  rand_num
        self.count_sums()


    def in_order(self):
        """ Determines if the SortedArray is in order.
           Returns:
            in_order - boolean pertaining to whether the SortedArray is in order
        """
        in_order = True
        for item in range(0, self.size - 1):
                if self.data[item] > self.data[item + 1]:
                    in_order = False
        return in_order


    def check_msg(self):
        """ Creates a string stating the ordered state of the SortedArray. 
           Returns:
            result_msg - string telling if the SortedArray is in order
        """
        # Local Variables
        # sum_before - sum of elements before sort
        # sum_sq_before - sum of the squares of the elements before sort
        # same_sums - boolean that is true if the the current sum and sum_sq 
        #             match up with the ones before the sort
        
        result_msg = "The array is "
        sum_before = self.sum
        sum_sq_before = self.sum_sq
        self.count_sums()
        same_sums = False
        if sum_before == self.sum and sum_sq_before == self.sum_sq:
            same_sums = True
        if same_sums == False and self.in_order() == False:
            result_msg += "not "
        result_msg += "in order."
        return result_msg
        

    def insertion_sort_h(self, h=1):
        """ Sort the items in the SortedArray using the insertion sort. """
        # Local Variables
        # key - number to be compared to others in the list
        
        # Forward iteration
        for i in range(1, self.size):
            key = self.data[i]
            j=i
            # Backward iteration to put number in correct spot
            while (j > h-1 and self.data[j-h] > key):
                self.data[j] = self.data[j-h]
                j -= h
            self.data[j] = key

    def insertion_sort(self):
        """ Sorts the items in a SortedArray using the insertion sort
            referenced by a more friendly name.
        """
        self.insertion_sort_h(1)


    def shell_sort(self):
        """ Sorts the items in a SortedArray using the shell sort. """
        h = 1
        while (h < self.size):
            h = (3 * h) + 1
        while (h > 1):
            h = (h-1) // 3
            self.insertion_sort_h(h)


    def heap_sort(self):
        """ Sorts the items in a SortedArray using the heap sort. """
        def downheap(n,k):
            """Params:
                n - length of SortedArray
                k - current heap
            """
            # Don't do this if the given length is 0 or smaller
            if n > 1:
                isHeap = False
                key = self.data[k]
                while (k <= (n-2)//2 and not isHeap):
                    # point j at smallest child
                    j = 2*k + 1
                    if j + 1 < n:
                        if self.data[j] < self.data[j+1]:
                            j+=1
                    # if the heap is in order, no switching required
                    if key > self.data[j]:
                        isHeap = True
                    # if the heap isn't in order, switch child and parent
                    else:
                        self.data[k] = self.data[j]
                        k = j
                self.data[k] = key

        n = self.size
        # PHASE 1
        # iterates k from lowest subtree with a child to the top of tree
        # and brings the highest number to the top
        for k in range((n-2)//2, -1, -1):
            downheap(n,k)

        # PHASE 2
        # after the highest number is at the top of the tree, switch
        # it to the bottom of the tree and do the downheap on a tree
        # one item smaller
        for m in range(n-1, 0, -1):
            self.data[m], self.data[0] = self.data[0], self.data[m]
            downheap(m, 0)


    def partition(self, left, right):
        """ Partitions the SortedArray within the indices given into two
            sections: one of items less than the pivot and one of items
            greater than the pivot.
           Params:
            left - left starting index
            right - final ending index
           Returns:
            i - integer of how far the i counter got until crossing with
                the j counter
        """
        # Local Variables
        # pivot - integer to compare elements in the list to to partition it 
        #         into sides less than the pivot and greater than  it
        # i - integer counter from the start of list
        # j - integer counter from the end of the list
        
        # pivot selected by the number in the first index (can be changed
        # to be more effective)
        pivot = self.data[left]
        i = left
        j = right
        # until the two counters cross
        while i <= j:
            # find an i where the number is greater than the pivot
            while self.data[i] < pivot:
                i += 1
            # find a j where the number is less than the pivot
            while self.data[j] > pivot:
                j -= 1
            if i <= j:
                self.data[i], self.data[j] = (self.data[j],
                                              self.data[i])
                i += 1
                j -= 1
        return i


    def quicksort(self, left, right):
        """ Partitions the SortedArray into two smaller lists with numbers
            smaller than a pivot number on the left side and those larger
            on the right side until the list is completely sorted
           Params:
            left - left starting index
            right - final ending index
        """
        # stop recursion if it's sorted
        if left < right:
            q = self.partition(left, right)
            self.quicksort(left, q-1)
            self.quicksort(q, right)


    def quick_sort(self):
        """Driver routine for recursive quick sort"""
        self.quicksort(0, self.size-1)


    def print_array(self, columns=10):
        """ Prints each element in a grid with a defined number of
            columns.
           Params:
            columns - number of columns in print table
        """
        # Local Variables
        # rows - number of rows in print table
        # i - counter for rows
        # j - counter for columns
        # index - index of the array to be printed
        rows = self.size // columns
        i, index = 0, 0
        while (i <= rows):
            j = 0
            while (j < columns and index < self.size):
                print("{:5}".format(self.data[index]), end='')
                index += 1
                j += 1
            print()
            i += 1







