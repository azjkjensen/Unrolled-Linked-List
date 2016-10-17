from ..unrolled_linked_list.module import UnrolledLinkedList
import unittest


class UnrolledLinkedList_Test(unittest.TestCase):
    """
    Test class for all UnrolledLinkedList tests.
    """
    def test_default_node_capacity(self):
        """
        Test that the default node capacity is being set, and is set to 16
        """
        l = UnrolledLinkedList()
        self.assertEqual(l.max_node_capacity, 16)

    def test_custom_node_capacity(self):
        '''
        Tests that a custom passed in node capacity is actually set 
        to various values.
        '''
        l = UnrolledLinkedList(4)
        self.assertEqual(l.max_node_capacity, 4)

        l = UnrolledLinkedList(15)
        self.assertEqual(l.max_node_capacity, 15)

        l = UnrolledLinkedList(1)
        self.assertEqual(l.max_node_capacity, 1)

    def test_empty(self):
        """
        Tests that a just-constructed list and 
        a list that has been appended to - and then
        removed from - is empty.
        """
        l = UnrolledLinkedList()
        self.assertEqual(str(l), "{}")

        l.append(1)
        del l[0]
        self.assertEqual(str(l), "{}")

    def test_add_item(self):
        '''Tests appending several items to a list'''
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        self.assertEqual(str(l), '{[1, 2, 3]}')

    def test_delete_item(self):
        '''Tests deleting an item after appending several.'''
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        del l[2]
        self.assertEqual(str(l), '{[1, 2]}')

    def test_get_item(self):
        '''Tests getting an item by index'''
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        self.assertEqual(str(l[1]), '2')
        
    def test_set_item(self):
        '''Tests setting an item by index'''
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l[1]=42
        self.assertEqual(str(l[1]), '42')

    def test_iteration(self):
        '''Tests that the list is iterable.'''
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        arr = []
        for i in l:
            arr.append(i)

        self.assertEqual(arr[0], l[0])
        self.assertEqual(arr[1], l[1])
        self.assertEqual(arr[2], l[2])

    def test_len(self):
        '''Tests that the length of a list is reported correctly.'''
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        
        self.assertEqual(str(len(l)), '3')

        l.append(4)
        
        self.assertEqual(str(len(l)), '4')

    def test_reverse(self):
        '''
        Tests that a list is reversed correctly 
        when reverse(listname) is called.
        '''
        testL = [3,2,1]
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)

        newL = []

        for x in reversed(l):
            newL.append(x)
        self.assertEqual(newL, testL)

    def test_contains(self):
        '''
        Tests that the contains dunder 
        method works.
        '''
        l = UnrolledLinkedList()
        l.append(1)
        l.append(2)
        l.append(3)

        self.assertEqual(1 in l, True)
        self.assertEqual(42 in l, False)

        
        