from copy import deepcopy
from homework.red_black_tree.rb_tree import RedBlackTree


class OrderedSet:
    def __init__(self, elements=None):
        self.tree = RedBlackTree()
        if elements is not None:
            self.__add_elements(elements)

    def __len__(self):
        return self.tree.count

    def __iter__(self):
        yield from self.tree.__iter__()

    def add(self, element):
        self.tree.add(element)

    def remove(self, element):
        self.tree.remove(element)

    def clear(self):
        self.tree = RedBlackTree()

    def contains(self, element):
        return self.tree.contains(element)

    def union(self, other_set):
        if not isinstance(other_set, type(self)):
            raise Exception("You cannot union a set with something that's not a set!")
        new_set = deepcopy(self)
        for other_el in other_set:
            new_set.add(other_el)

        return new_set

    def intersection(self, other_set):
        if not isinstance(other_set, type(self)):
            raise Exception("You cannot union a set with something that's not a set!")
        new_set = OrderedSet()
        for other_el in other_set:
            if self.contains(other_el):
                new_set.add(other_el)

        return new_set

    def __add_elements(self, elements):
        for element in elements:
            self.tree.add(element)
