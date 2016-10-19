# Unrolled Linked List

## What is an Unrolled Linked List?

An [Unrolled Linked List](https://en.wikipedia.org/wiki/Unrolled_linked_list) is essentially a Linked List, where each node contains a list of elements up to a given max node capacity [more](https://brilliant.org/wiki/unrolled-linked-list/) 

![alt text](https://upload.wikimedia.org/wikipedia/commons/1/16/Unrolled_linked_lists_%281-8%29.PNG)

### Balancing

Here is an example of adding to the end of an Unrolled Linked List with a max node capacity of 4.[this link has a good explaination of insertion / deletion](https://blogs.msdn.microsoft.com/devdev/2005/08/22/unrolled-linked-lists/)

```
{}
{[1]}
{[1, 2]}
{[1, 2, 3]}
{[1, 2, 3, 4]}
{[1, 2], [3, 4, 5]}
{[1, 2], [3, 4, 5, 6]}
{[1, 2], [3, 4], [5, 6, 7]}
{[1, 2], [3, 4], [5, 6, 7, 8]}
```

If I were to remove the value 3, then 4:

```
{[1, 2], [4, 5, 6], [7, 8]}
{[1, 2], [5, 6], [7, 8]}
```

### Pros

* Linked Lists are O(n) access. Having nodes that hold muliple elements in a list / array lowers that cost
* This also helps to lower the amount of memory used in a traditional Linked List

## Specs

The following dunder methods are implemented for you:

* \_\_delitem\_\_ (self,index)
    * Remove the item at the given index.
* \_\_getitem\_\_ (self,index):
    * Returns the item in the given index
* \_\_setitem\_\_ (self,key,value):
    * sets the item at `key` to `value`
* \_\_iter\_\_ (self):
    * Use the Python yield statement to make your list iterable. This will allow you to use it in a for-each loop
* \_\_str\_\_ (self)
    * Create a string representation of the list in the form {[x, x, x], [x, x], [x, x, x, x]}
where each set of [] indicates the list of values within a single node.
* \_\_len\_\_ (self)
    * returns the total # of data in the list, not the number of nodes
* \_\_reversed\_\_ (self)
    * Reverses the list. Allows you to use iterator reversed, like for i in reversed(l)
* \_\_contains\_\_ (self, obj)
    * Returns True if obj is in the data structure, otherwise False
* append(self,data)
    * Add the data to the end of the list

## Dunder Methods

Dunder stands for double underscores. Dunder methods are also refered to as magic methods. They really aren't that magical though.

Classes can implement dunder functions as needed. They allow operators and certain built-in python functions to work on the class. For example: adding two lists using the __add__ dunder function:

```python
l1 = [1,2,3,4]
l2 = [5,6,7,8]

l = l1 + l2
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8]
```

If I were to implement the \_\_getitem\_\_ dunder method for a Linked List, it might look something like this:

```python
    def __getitem__(self, index):
        """Allows you to get an item using the [] syntax
        """
        return self.getNodeAt(index)
```
