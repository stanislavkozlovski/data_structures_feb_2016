"""
Implement the data structure singly linked list LinkedList<T> that holds a sequence of linked elements. Define two classes:
ListNode<T> holding the value and a pointer to the next element.
LinkedList<T> holding the first element + operations
    Add(T item),
    Remove(index),
    Count,
    IEnumerable<T>,
    FirstIndexOf(T item),
    LastIndexOf(T item).
The LinkedList<T> is very similar to DoublyLinkedList<T> but holds a pointer to the next element only (not to both next and previous elements).
"""


class LinkedListNode:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.__count = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next_node

    def add(self, value):
        if self.__count == 0:
            self.head = LinkedListNode(value, self.tail)
        else:
            new_tail = LinkedListNode(value, None)
            if self.tail:
                self.tail.next_node = new_tail
            else:
                self.head.next_node = new_tail
            self.tail = new_tail
        self.__count += 1

    def remove(self, index):
        if index == 0:
            old_head = self.head
            self.head = self.head.next_node
            return old_head.value
        for idx, node in enumerate(self):
            if idx == index-1:
                next_node = node.next_node
                if not next_node:
                    raise Exception("No node at index {}".format(index))
                node.next_node = next_node.next_node
                return next_node.value

        raise Exception("No node at index {}".format(index))

    def first_index_of(self, value):
        for idx, node in enumerate(self):
            if node.value == value:
                return idx

        return -1

    def last_index_of(self, value):
        last_index = -1
        for idx, node in enumerate(self):
            if node.value == value:
                last_index = idx

        return last_index

    @property
    def count(self):
        return self.__count

ll = LinkedList()
ll.add(5)
ll.add(6)
ll.add(6)
ll.add(6)
ll.add(7)
print([v.value for v in ll])
ll.remove(0)
print([v.value for v in ll])
print(ll.first_index_of(6))
print(ll.last_index_of(6))
print(ll.count)
for node in ll:
    print(node.value, end=" ")

