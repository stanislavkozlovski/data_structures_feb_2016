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

    def remove(self, value):
        if value not in self.values:
            if not self.__has_children():
                raise Exception('Value not in tree!')
            recursed = False
            if value < self.values[0]:
                # before first
                self.children[0].remove(value)
            elif value > self.values[-1]:
                # after last
                self.children[-1].remove(value)
            else:
                for i in range(len(self.values)-1):
                    if self.values[i] < value < self.values[i+1]:
                        self.children[i+1].remove(value)
                        break
            return

        if not self.__has_children():
            # easy, simple remove
            self.values.remove(value)
            return

        # try to find predecessor
        value_idx = self.values.index(value)
        predecessor: BNode = self.children[value_idx]
        if len(predecessor.values) > 1:
            pass
            # switch with predecessor value
            self.values[value_idx], predecessor.values[-1] = predecessor.values[-1], self.values[value_idx]
            # recursively delete downwards
            return predecessor.remove(value)
        successor: BNode = self.children[value_idx+1]
        if len(successor.values) > 1:
            # switch with successor value
            self.values[value_idx], successor.values[0] = successor.values[0], self.values[value_idx]
            return successor.remove(value)

        # both have 1 child, so, merge VALUE and SUCCESSOR into PREDECESSOR
        for l in successor.values:
            predecessor.add(l)
        predecessor.add(value)
        # TODO: Children lost
        self.values.remove(value)
        # re-order children
        for i in range(value_idx + 1, len(self.children)):
            self.children[i] = self.children[i+1]
        # recursively remove
        predecessor.remove(value)

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
            # set parents
            left_node.values = left_arr

            right_node = BNode(order=self.order, parent=self)
            right_node.values = right_arr

            # copy children
            left_node.children = self.children[:median+1]
            right_node.children = self.children[median+1:]
            # assign parents to  children
            for i in left_node.children:
                if i is not None:
                    i.parent = left_node
            for i in right_node.children:
                if i is not None:
                    i.parent = right_node

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
        to_split = False
        if len(other.values) + len(self.values) >= self.order:
            to_split = True  # we will go past the capacity for this node and will need to split it

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

        if to_split:
            self.split()

    def __has_children(self):
        return any(self.children)

