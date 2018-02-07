class Array(object):
    """ Implement an Array object
    DRS 2015.01.05
    Fixed size
    Standard index operations
    Zero-based indexing

    Note that bounds checking is done in the underlying Python list
    """


    def __init__(self,size,default_value=None):
        """ __init()__ create an Array object

        Param
        size            Number of elements in the array
        default_value   The array is initialized to the default value

        Class variables
        data   The array contents, stored in a Python list
        size   The number of elts in the array
        default_value   The default_value for the array contents, or None
        """
        self.data = list()
        self.size = size
        self.default_value = default_value
        self.data = [default_value for i in range(size)]
        # for i in range(size):
        #       self.data.append(default_value)

    def __setitem__(self,index,new_value):
        """ Set the datum with subscript index to new_value. """
        self.data[index] = new_value

    def __getitem__(self,index):
        """ Retrieve the datum with subscript index. """
        return self.data[index]

    def __len__(self):
        """ Return the number of datums in data. """
        return len(self.data)

    def __iter__(self):
        """ Return an iterator for the array. """
        return iter(self.data)
