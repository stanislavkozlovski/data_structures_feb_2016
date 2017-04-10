from collections import deque


class FibNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.rank = 0

    def add_child(self, value):
        if self.rank == 0:
            self.rank = 1
        self.rank += value.rank
        self.children.append(value)

    def __lt__(self, other):
        if not isinstance(other, FibNode):
            return self.value < other
        return self.value < other.value

    def __eq__(self, other):
        if not isinstance(other, FibNode):
            return self.value == other
        return self.value == other.value


class FibHeap:
    def __init__(self):
        self.root_list = []
        self.min = float('inf')

    def add_node(self, value):
        if value < self.min:
            self.min = value
        self.root_list.append(value)

    def delete_min(self):
        min_node = self.min
        self.root_list.remove(self.min)
        for child in self.min.children:
            self.add_node(child)

        if not self.root_list:
            self.min = None
            return min_node
        self.min = min(self.root_list)

        ranks = {}
        # Consolidate trees so that no two trees have the same rank
        for root in self.root_list:
            if root.rank in ranks:
                if ranks[root.rank] != root:
                    continue
                taken_root = ranks[root.rank]
                if taken_root < root:
                    taken_root.add_child(root)
                else:
                    root.add_child(taken_root)
            else:
                ranks[root.rank] = root

        return min_node

fh = FibHeap()
fh.add_node(FibNode(5))
fh.add_node(FibNode(2))
fh.add_node(FibNode(6))
fh.add_node(FibNode(1431))
fh.add_node(FibNode(0))
fh.add_node(FibNode(1))


assert 0 == fh.delete_min()
assert 1 == fh.delete_min()
assert 2 == fh.delete_min()
assert 5 == fh.delete_min()
print(fh.delete_min().value)
print(fh.delete_min().value)
# print(fh.delete_min().value)
# print(fh.delete_min().value)
