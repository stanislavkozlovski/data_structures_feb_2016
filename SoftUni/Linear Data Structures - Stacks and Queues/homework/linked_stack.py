class Node:
    def __init__(self, value, bottom_node: 'Node'=None):
        self.value = value
        self.__bottom_node = bottom_node

    @property
    def bottom_node(self):
        return self.__bottom_node

    @bottom_node.setter
    def bottom_node(self, node):
        self.__bottom_node = node


class LinkedStack:
    def __init__(self):
        self.first_node = None
        self.count = 0

    def __iter__(self):
        node = self.first_node
        while node:
            yield node.value
            node = node.bottom_node

    def push(self, element):
        if self.count == 0:
            self.first_node = Node(value=element, bottom_node=None)
        else:
            new_node = Node(value=element, bottom_node=self.first_node)
            self.first_node = new_node
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise Exception('Stack is empty!')
        node_value = self.first_node.value
        self.first_node = self.first_node.bottom_node
        self.count -= 1
        return node_value

