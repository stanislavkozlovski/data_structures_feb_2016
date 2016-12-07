"""
Follow the concepts from the CircularQueue<T> class from the exercises in class.
The stack is simpler than the circular queue, so you will need to follow the same logic, but more simplified. Some hints:
The stack capacity is this.elements.Length
Keep the stack size (number of elements) in this.Count

Push(element) just saves the element in elements[this.Count] and increases this.Count
Push(element) should invoke Grow() in case of this.Count == this.elements.Length
Pop() decreases this.Count and returns this.elements[this.Count]
Grow() allocates a new array newElements of size 2 * this.elements.Length
and copies the first this.Count elements from this.elements to newElements. Finally, assign this.elements = newElements
ToArray() just creates and returns a sub-array of this.elements[0…this.Count-1]
"""


class ArrayStack:
    def __init__(self, capacity: int=16):
        self.elements = [None] * capacity
        self.__count = 0
        self.capacity = capacity

    def __iter__(self):
        return list(reversed([element for element in self.elements if element is not None])).__iter__()

    def push(self, element):
        self.elements[self.__count] = element
        self.__count += 1
        if self.__count == self.capacity:
            self.__extend()

    def pop(self):
        if self.__count == 0:
            raise Exception('Stack is empty!')
        element = self.elements[self.__count-1]
        del self.elements[self.__count-1]
        self.__count -= 1
        return element

    def __extend(self):
        self.elements = self.elements + ([None] * self.capacity)
        self.capacity *= 2

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        self.__count = value

stack = ArrayStack()
stack.push(5)
stack.push(5)
stack.push(5)
stack.pop()
print(stack)