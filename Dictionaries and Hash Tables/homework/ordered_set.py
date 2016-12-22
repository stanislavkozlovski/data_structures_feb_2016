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

        def add_to_tree(root):
            """
            Traverse the tree to find a place to add the node
            :returns True if it was added successfully
            :returns False if it is already in the tree
            """
            if root.value == value:
                return False
            elif root.value > value:
                if root.left:
                    return add_to_tree(root.left)
                root.left = Node(value, parent=root)
            else:  # root.value < value
                if root.right:
                    return add_to_tree(root.right)
                root.right = Node(value, parent=root)
            return True

        # add to the tree and check if it was already there
        node_was_added = add_to_tree(self.root)
        if not node_was_added:
            return  # it was already there, no need to increment

        self.count += 1

    def remove(self, value):
        element_to_remove, found = self.find_element(value)
        if not found:
            raise Exception('{} is not in the Ordered Set'.format(value))
        self.count -= 1  # it's obvious that we will remove a node now

        removing_root = self.root.value == value
        left_node, parent, right_node = element_to_remove.left, element_to_remove.parent, element_to_remove.right
        if not right_node and not left_node:
            # Node does not have any children
            if removing_root:
                self.root = None
            if parent:
                if parent.value > value:
                    parent.left = None
                else:
                    parent.right = None
            return

        replacement_node = None  # the node that will replace the original node
        if right_node:
            replacement_node = right_node
            # we want the leftest child of the right node to be the parent of the left node of the original node
            if left_node:
                right_leftest_node = self.__get_leftest_node(right_node)  # return the leftest node or the node itself
                left_node.parent = right_leftest_node
                right_leftest_node.left = left_node
        elif left_node:
            replacement_node = left_node

        replacement_node.parent = parent

        if removing_root:
            self.root = replacement_node
        if parent:
            # because we removed a node, we need to change its parent's reference
            if parent.value > replacement_node.value:
                parent.left = replacement_node
            else:
                parent.right = replacement_node

    def __get_leftest_node(self, node):
        if node.left:
            return self.__get_leftest_node(node.left)
        return node

    def find_element(self, value):
        """
        :return: a Tuple holding the Element and a boolean indicating if it found it or not
        """
        def __find(element):
            if value == element.value:
                return element, True
            elif element.right and element.value < value:
                return __find(element.right)
            elif element.left and value < element.value:
                return __find(element.left)

            return None, False

        return __find(self.root)

    def contains(self, value):
        _, found = self.find_element(value)
        return found

