"""
Implement the ordered set data structure. It should store unique elements in a binary search tree.
The elements should be kept sorted at all times. The ordered set should be generic and support the following operations:
    Add(T element) -
        adds the element to the set
    Contains(T element)
        determines whether the element is present in the set
    Remove(T element)
        removes the element from the set. Its place should be taken by the bigger child node.
    Count
        property that returns the number of unique elements in the set

The set should be foreach-able (just like arrays, lists and other data structures).
Implement the IEnumerable<T> interface to achieve this. The set should yield all elements, sorted, in ascending order.
Tip: Use in-order traversal.
"""


class OrderedSet:
    def __init__(self):
        self.count = 0