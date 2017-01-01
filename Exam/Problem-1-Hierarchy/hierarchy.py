from collections import deque

import collections

class OrderedSet(collections.MutableSet):

    def __init__(self, iterable=None):
        self.end = end = []
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.children = OrderedSet()

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def bfs(self):
        queue = deque()
        queue.append(self)
        order = []
        while queue:
            el = queue.popleft()
            yield el
            order.append(el)
            for ch in el.children:
                queue.append(ch)

    def add_child(self, child):
        self.children.add(child)


class Hierarchy:
    def __init__(self, root):
        self.root = Node(value=root, parent=None)
        self.hierarchy = {root: self.root}
        self.elements = {root}
        self.count = 0

    def __len__(self):
        return self.count

    def __iter__(self):
        yield from self.root.bfs()

    def __contains__(self, item):
        return item in self.hierarchy

    def add(self, element, child):
        """
        Add(element, child) - adds child to the hierarchy as a child of element.
            Throws an exception if element does not exist in the hierarchy.
            Throws an exception if child already exists (duplicates are not allowed).
        """
        if element not in self.hierarchy or child in self.hierarchy:
            raise Exception()
        # add in tree/dict
        parent = self.hierarchy[element]
        child = Node(value=child, parent=parent)
        parent.add_child(child)
        self.hierarchy[child.value] = child

        self.elements.add(child.value)
        self.count += 1

    def remove(self, element):
        """
        Remove(element) - removes the element from the hierarchy.
            If it has children, they become children of the element's parent.
            If element is root node, throws an exception.
        """
        if self.root.value == element or element not in self.hierarchy:
            raise Exception()
        el_to_remove = self.hierarchy[element]
        parent = el_to_remove.parent
        # remove the element from the parent's children
        parent.children.remove(el_to_remove)
        # migrate the children of the removed node to the parent
        for child in el_to_remove.children:
            parent.add_child(child)
        
        self.count -= 1

    def get_children(self, element):
        if element not in self.hierarchy:
            raise Exception()
        return self.hierarchy[element].children

    def get_parent(self, element):
        if element not in self.hierarchy:
            raise Exception()

        parent = self.hierarchy[element]

        return parent.value if parent is not None else None

    def get_common_elements(self, other: 'Hierarchy'):
        return self.elements.intersection(other.elements)


hrh = Hierarchy(3)
hrh.add(3, 2)
hrh.add(3, 5)
hrh.add(5, 1)
print(len(hrh))
print(hrh.get_children(10))
print('BAA')
for l in hrh:
    print(l)