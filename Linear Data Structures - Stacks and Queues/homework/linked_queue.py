class Node:
    def __init__(self, value, next_node: 'Node'=None, prev_node: 'Node'=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedQueue:
    def __init__(self):
        self.head = self.tail = None
        self.count = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next_node

    def enqueue(self, value):
        if self.count == 0:
            self.head = self.tail = Node(value=value)
        elif self.count == 1:
            self.tail = Node(value=value, prev_node=self.head)
            self.head.next_node = self.tail
        else:
            new_node = Node(value=value, prev_node=self.tail, next_node=None)
            self.tail.next_node = new_node
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception('Queue is empty!')
        elif self.count == 1:
            value = self.head.value
            self.head = self.tail = None
        else:
            value = self.head.value
            self.head = self.head.next_node
        self.count -= 1
        return value

lq = LinkedQueue()
lq.enqueue(1)
lq.enqueue(2)
lq.enqueue(3)
lq.enqueue(4)
print(lq.dequeue())
print(lq.dequeue())
print(lq.dequeue())
print(lq.dequeue())