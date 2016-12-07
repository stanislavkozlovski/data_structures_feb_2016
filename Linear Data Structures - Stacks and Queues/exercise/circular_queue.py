class CircularQueue:
    def __init__(self, capacity: int=16):
        self.__count = 0
        self.head_idx = 0
        self.tail_idx = 0
        self.__queue = [None] * capacity

    def __iter__(self):
        # Iterate through the list, skipping the None objects
        for item in [part for part in self.__reconstruct_queue() if part is not None]:
            yield item

    def enqueue(self, element):
        if self.head_idx == self.tail_idx and self.__count < 1:
            # first element!
            self.__queue[self.head_idx] = element
        else:
            self.tail_idx += 1
            if self.tail_idx == self.head_idx:
                #  Extend queue!
                self.tail_idx = len(self.__queue)
                self.__extend()
                self.__queue[self.tail_idx] = element
            elif self.tail_idx >= len(self.__queue):
                # Try to add at the front
                if self.head_idx > 0:
                    self.tail_idx = 0
                    self.__queue[self.tail_idx] = element
                else:
                    # Extend the queue!
                    self.__extend()
                    self.__queue[self.tail_idx] = element
            elif self.tail_idx < self.head_idx or self.tail_idx < len(self.__queue):
                #  valid addition
                self.__queue[self.tail_idx] = element

        self.__count += 1

    def dequeue(self):
        element = self.__queue[self.head_idx]
        if element is None:
            raise Exception('Queue is empty!')
        self.__queue[self.head_idx] = None
        self.head_idx += 1

        if self.head_idx >= len(self.__queue):
            self.head_idx = 0

        self.__count -= 1
        if self.__count == 0:
            self.head_idx = self.tail_idx = 0  # reset the indexes
        return element

    def __extend(self):
        """ Reconstruct the circular queue and make it twice as big """
        new_queue = (self.__reconstruct_queue()
                     + ([None] * len(self.__queue)))  # increase size 2 times
        self.__queue = new_queue

    def __reconstruct_queue(self):
        """ Reconstructs our circular queue in a linear fashion. """
        return (self.__queue[self.head_idx:]
                + (self.__queue[0:self.tail_idx + 1]
                   # If our queue's tail is before our head, this means that we have done a circle
                   if self.tail_idx < self.head_idx  # so  we need to get the items from that start too
                   else [])
                )
    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, val):
        self.__count = val


# queue = CircularQueue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)
# queue.enqueue(50)
# print(queue.count)
# print(list(queue))
# print(queue.dequeue())
# print(queue.count)
#
# print(queue.dequeue())
# print(queue.count)
#
# print(queue.dequeue())
# print(queue.count)
#
# print(queue.dequeue())
# print(queue.count)
# print(list(queue))
#
# print(queue.dequeue())
# print(queue.count)
#
# print(list(queue))
