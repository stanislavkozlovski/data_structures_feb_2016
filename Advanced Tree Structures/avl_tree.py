
class Node:
    def __init__(self, value, parent, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.balance_factor = 0

    def __repr__(self):
        return 'Node {val} with BF {bf}'.format(val=self.value, bf=self.balance_factor)

    def print_node(self, tab=0):
        if self.right is not None:
            self.right.print_node(tab+2)
        print((' '*tab) + str(self.value))
        if self.left is not None:
            self.left.print_node(tab+2)


class AvlTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def print_tree(self):
        if self.root is not None:
            self.root.print_node()

    def add(self, value):
        if self.root is None:
            self.root = Node(value, None)
            self.count += 1
            return
        parent, direction = self._find_parent(value)
        new_node = Node(value=value, parent=parent)
        if direction == 'L':
            parent.left = new_node
        else:
            parent.right = new_node
        self.modify_balance_factor(new_node)

    def modify_balance_factor(self, node):
        """ Modifies the balance factor for each node upwards of the given one"""
        parent = node.parent
        if parent is None:
            return
        direction = 'L' if parent.value > node.value else 'R'
        if direction == 'L':
            parent.balance_factor += 1
        else:
            parent.balance_factor += -1
        if parent.balance_factor != 0:
            self.modify_balance_factor(parent)

    def _find_parent(self, value):
        """ Find the appropriate parent for a newly-added value """
        def _find(root: Node):
            if root.value == value:
                return None, None  # value is already in the tree
            if root.value > value:
                if root.left is not None:
                    return _find(root.left)
                else:
                    return root, 'L'
            else:
                if root.right is not None:
                    return _find(root.right)
                else:
                    return root, 'R'

        return _find(self.root)

avl = AvlTree()
avl.add(2)
avl.add(3)
avl.add(1)
avl.add(5)
avl.add(2.5)
avl.add(6)
avl.print_tree()