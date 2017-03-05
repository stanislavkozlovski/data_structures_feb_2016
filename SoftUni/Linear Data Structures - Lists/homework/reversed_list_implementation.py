"""
Implement a data structure ReversedList<T> that holds a sequence of elements of generic type T.
 It should hold a sequence of items in reversed order. The structure should have some capacity that grows twice when it is filled.
  The reversed list should support the following operations:
    Add(T item)  adds an element to the sequence (grow twice the underlying array to extend its capacity in case the capacity is full)
    Count  returns the number of elements in the structure
    Capacity  returns the capacity of the underlying array holding the elements of the structure
    this[index]  the indexer should access the elements by index (in range 0 … Count-1) in the reverse order of adding
    Remove(index)  removes an element by index (in range 0 … Count-1) in the reverse order of adding

IEnumerable<T>  implement an enumerator to allow iterating over the elements in a foreach loop in a reversed order of their addition
Hint: you can keep the elements in the order of their adding, by access them in reversed order (from end to start).
"""


# Can't even use the array because it has it's own methods, whatever, let's embrace python


class ReversedList(list):
    """
    Add and store the items in a normal way but access and iterate them in reversed order

    Come to think of it, it sounds like a bad idea really, but the required implementation is not too clear how
    we should store newly added items and if they should be at the 'start'
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):
        for item in reversed(self):
            yield item

    def __str__(self):
        return str(list(reversed(self)))

    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(reversed(super().__getitem__(slice(
                self.__get_reversed_key(item.stop if item.stop else self.__len__()-1),
                self.__get_reversed_key(item.start) + 1,
                item.step
            ))))
        else:
            return super().__getitem__(self.__get_reversed_key(item))

    # noinspection PyTypeChecker
    def __setitem__(self, key, value):
        if isinstance(key, slice):
            super().__setitem__(slice(
                self.__get_reversed_key(key.stop if key.stop else self.__len__()-1),
                self.__get_reversed_key(key.start) + 1,
                key.step
            ),
            value)
        else:
            idx = self.__get_reversed_key(key)
            super().__setitem__(idx, value)

    # noinspection PyTypeChecker
    def __delitem__(self, key):
        if isinstance(key, slice):
            super().__delitem__(slice(
                self.__get_reversed_key(key.stop if key.stop else self.__len__() - 1),
                self.__get_reversed_key(key.start) + 1,
                key.step
            ))
        else:
            idx = self.__get_reversed_key(key)
            super().__delitem__(idx)

    def remove(self, index):
        self.__delitem__(index)

    def __get_reversed_key(self, key):
        if key >= 0:
            reversed_idx = (self.__len__() - 1) - key
        else:
            reversed_idx = abs(key)
        return reversed_idx

    def count(self):  # overriden, whoops
        return self.__len__()

    def capacity(self):
        raise NotImplementedError()  # can't find such a thing for python

reversd = ReversedList([1,2,3,4,5,6])
print(reversd[-1])  # 2
print(reversd[1])  # 5

reversd[1] = 33
print(reversd[1])  # 33

print(reversd[0:2])  # 6, 33, 4
print(reversd[-2:])  # 3, 2, 1
reversd[0:1] = [3, 3]
print(reversd[0:2])  # 3, 3, 4
reversd.remove(0)
print(reversd[0:2])  # 3, 4, 3
reversd.remove(0)
print(reversd[0:2])  # 4, 3, 2

for i in reversd:
    print(i)  # 4 3 2 1
print(reversd)


