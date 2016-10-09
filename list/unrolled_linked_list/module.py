class Node():
    '''This '''
    def __init__(self):
        self.arr = None
        self.next = None

class UnrolledLinkedList():
    """This is the class name you should use. You should also have a
    max_node_capacity. Also, you should remove this comment and possibly
    replace it with your own
    """
    def __init__(self, max_node_capacity=16):
        self.max_node_capacity = max_node_capacity
        self.head = None

    '''Remove the item at the given index.
    If the index is negative, then you should remove starting from the back 
    (i.e. deleting at -2 would delete the second-to-last element)
    If the index is too large, raise an IndexError'''
    def __delItem__(self,index):

    """Returns the item in the given index.
    If the index is negative, return with the index starting from the back 
    (i.e. getting at -1 returns the last item)
    If the index is too large, raise an IndexError"""
    def __getitem__ (self,index):

    '''Sets the item at key to value
    If the key is too large, raise an IndexError'''
    def __setitem__ (self,key,value):

    '''Use the Python yield statement to make your list iterable. 
    This will allow you to use it in a for-each loop'''
    def __iter__ (self):
    
    '''Create a string representation of the list in the form 
    {[x, x, x], [x, x], [x, x, x, x]} where each set of [] indicates
    the list of values within a single node.'''
    def __str__ (self):
    
    '''returns the total # of data in the list, not the 
    number of nodes'''
    def __len__ (self):
    
    '''Reverses the list. Does not return a new list - 
    actually mutates the data structure'''
    def __reversed__ (self):
    
    '''Returns True if obj is in the data structure, 
    otherwise False'''
    def __contains__ (self, obj):
    
    '''Add the data to the end of the list
    If a node has reached its max capacity, 
    you must create a new node to put the data in'''
    def append(self,data):
    