class Node:
    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next_node

    def for_each(self, fn):
        """ Execute a function on every item """
        for el in self.__iter__():
            fn(el)

    def add_first(self, element):
        if not self.head:
            self.head = self.tail = Node(value=element, prev_node=None, next_node=None)
        else:
            node = Node(value=element, prev_node=None, next_node=self.head)
            self.head.prev_node = node
            self.head = node
        self.count += 1

    def add_last(self, element):
        if self.tail:
            node = Node(value=element, prev_node=self.tail, next_node=None)
            self.tail.next_node = node
            self.tail = node
        else:
            self.head = self.tail = Node(value=element, prev_node=None, next_node=None)

        self.count += 1

    def remove_first(self):
        if self.count == 0:
            raise Exception('Our linked list is empty!')

        old_head_value = self.head.value
        if self.count > 2:
            new_head = self.head.next_node
            new_head.prev_node = None
            self.head = new_head
            self.count -= 1
        elif self.count == 2:
            self.head = self.tail = Node(value=self.tail.value, prev_node=None, next_node=None)
            self.count -= 1
        elif self.count == 1:
            self.head = self.tail = None
            self.count -= 1

        return old_head_value

    def remove_last(self):
        if self.count == 0:
            raise Exception('Our linked list is empty!')

        old_tail_value = self.tail.value

        if self.count > 2:
            new_tail = self.tail.prev_node
            new_tail.next_node = None
            self.tail = new_tail
            self.count -= 1
        elif self.count == 2:
            self.head = self.tail = Node(value=self.head.value, prev_node=None, next_node=None)
            self.count -= 1
        elif self.count == 1:
            self.head = self.tail = None
            self.count -= 1

        return old_tail_value
