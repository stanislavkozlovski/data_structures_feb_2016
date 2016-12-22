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
from collections import deque


class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __iter__(self):
        if self.left:
            yield from self.left.__iter__()

        yield self.value

        if self.right:
            yield from self.right.__iter__()


class OrderedSet:
    def __init__(self):
        self.count = 0
        self.root = None

    def __iter__(self):
        return (val for val in self.root.__iter__())

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.count += 1
            return
        parent = self.__find_parent(value)
        if parent is None:
            return  # value is already in the tree

        if parent.value < value:
            parent.right = Node(value, parent=parent)
        elif value < parent.value:
            parent.left = Node(value, parent=parent)
        else:
            raise Exception('Error while adding!')

        self.count += 1

    def remove(self, value):
        element_to_remove = self.find_element(value)
        if element_to_remove == False:
            raise Exception("Element is not in the set, You can't remove it!")
        parent = element_to_remove.parent
        right_node = element_to_remove.right
        left_node = element_to_remove.left
        if right_node:
            if self.root.value == value:
                self.root = right_node
            right_node.parent = parent
            if parent:
                if parent.value > right_node:
                    parent.left = right_node
                else:
                    parent.right = right_node
            if left_node:
                leftest_node = self.__get_leftest_node(right_node)
                left_node.parent = leftest_node
                leftest_node.left = left_node
                # TODO: get leftest and etc
        elif left_node:
            if self.root.value == value:
                self.root = left_node
            left_node.parent = parent
            if parent:
                if parent.value > left_node:
                    parent.left = left_node
                else:
                    parent.right = left_node
        else:
            if parent:
                if parent.value > value:
                    parent.left = None
                else:
                    parent.right = None
        self.count -= 1



    def __get_leftest_node(self, node):
        if node.left:
            return self.__get_leftest_node(node.left)
        return node

    def find_element(self, value):
        def __find(element):
            if value == element.value:
                return element
            elif element.value < value:
                if not element.right:  # no more to go
                    return False
                return __find(element.right)
            elif value < element.value:
                if not element.left:  # no more to go
                    return False
                return __find(element.left)

        return __find(self.root)

    def contains(self, value):
        return self.__find_parent(value) is None

    def __find_parent(self, value):
        """ Finds a place for the value in our binary tree"""
        def __find(parent):
            if value == parent.value:
                return None
            elif parent.value < value:
                if not parent.right:  # no more to go
                    return parent
                return __find(parent.right)
            elif value < parent.value:
                if not parent.left:  # no more to go
                    return parent
                return __find(parent.left)
        return __find(self.root)
