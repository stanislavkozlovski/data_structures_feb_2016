class BNode:
    def __init__(self, parent=None, order=6):
        self.parent = parent
        self.order = order
        self.max_values_count = order-1
        self.values = []
        self.children = [None for _ in range(order)]

    def add(self, value):
        if not self.__has_children():
            # Leaf: Add here
            self.values.append(value)
            self.values = sorted(self.values)
            if len(self.values) == self.max_values_count+1:
                self.split()
        else:
            # Find downwards node :)
            # try max left and max right first
            if value < self.values[0]:
                # go left
                wanted_child = self.children[0]
                wanted_child.add(value)
            elif value > self.values[-1]:
                # go right
                wanted_child = self.children[-1]
                wanted_child.add(value)
            else:
                # find middle
                for i in range(1, len(self.values)):
                    if value > self.values[i-1] and value < self.values[i]:
                        wanted_child = self.children[i]
                        wanted_child.add(value)
                        break

    def split(self):
        if len(self.values) % 2 == 0:
            median = (len(self.values) // 2) - 1
        else:
            median = (len(self.values) // 2)
        median_value = self.values[median]
        left_arr = self.values[:median]
        right_arr = self.values[median+1:]

        if self.parent is None:
            # easy shit, create two children
            left_node = BNode(order=self.order, parent=self)
            left_node.values = left_arr

            right_node = BNode(order=self.order, parent=self)
            right_node.values = right_arr

            # copy children
            left_node.children = self.children[:median+1]
            right_node.children = self.children[median+1:]

            self.values = [median_value]
            self.children = [left_node, right_node]
        else:
            left_node = BNode(order=self.order, parent=self)
            left_node.values = left_arr

            right_node = BNode(order=self.order, parent=self)
            right_node.values = right_arr

            # copy children
            left_node.children = self.children[:median + 1]
            right_node.children = self.children[median + 1:]

            self.values = [median_value]
            self.children = [left_node, right_node]
            # Merge nodes
            self.parent.merge_with_child(self)

    def merge_with_child(self, other: 'BNode'):
        # add the values
        if len(other.values) + len(self.values) >= self.order:
            raise NotImplementedError("can't handle case when it overfills recursively")
        if other not in self.children:
            raise Exception('A BNode can only merge with its children!')
        other_idx = self.children.index(other)
        # from other_idx-1 onwards, insert all the values
        insert_idx = other_idx
        for other_val in other.values:
            self.values.insert(insert_idx, other_val)
            insert_idx += 1
        if self.values != sorted(self.values):
            raise Exception('Sort err while adding values with merge!')

        # copy children
        # copy first child
        self.children[other_idx] = other.children[0]
        self.children[other_idx].parent = self
        insert_idx = other_idx + 1
        for child in other.children[1:]:
            self.children.insert(insert_idx, child)
            child.parent = self
            insert_idx += 1

    def __has_children(self):
        return any(self.children)
