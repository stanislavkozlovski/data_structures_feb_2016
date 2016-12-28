
class Node:
    def __init__(self, value, parent, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.balance_factor = 0

    def __iter__(self):
        if self.left is not None:
            yield from self.left.__iter__()
        yield self.value
        if self.right is not None:
            yield from self.right.__iter__()

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

    def __len__(self):
        return self.count

    def __iter__(self):
        yield from self.root.__iter__()

    def print_tree(self):
        if self.root is not None:
            self.root.print_node()

    def add(self, value):
        if self.root is None:
            self.root = Node(value, None)
            self.count += 1
            return
        parent, direction = self._find_parent(value)
        if parent is None:
            return  # value is already in the tree
        new_node = Node(value=value, parent=parent)
        if direction == 'L':
            parent.left = new_node
        else:
            parent.right = new_node
        self.modify_balance_factor(new_node)
        self.count += 1

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
            if parent.balance_factor in [-2, 2]:
                # TODO: ROTATE :)
                if parent.balance_factor == -2:
                    parent_dir = 'R'
                    if node.balance_factor == -1:
                        node_dir = 'R'
                    else:
                        node_dir = 'L'
                    general_dir = node_dir + parent_dir
                    if general_dir == 'RR':
                        self.left_rotation(node=node, parent=parent)
                    elif general_dir == 'LR':
                        # TODO: RIGHT-LEFT ROTATION
                        self.right_rotation(node.left, node)
                        self.left_rotation(node.parent, parent)

                    else:
                        raise Exception('Unexpected behavior!')
                else:
                    parent_dir = 'L'
                    if node.balance_factor == -1:
                        node_dir = 'R'
                    else:
                        node_dir = 'L'
                    general_dir = node_dir + parent_dir
                    if general_dir == 'LL':
                        self.right_rotation(node, parent)
                    elif general_dir == 'RL':
                        # TODO: LEFT-RIGHT ROTATION
                        self.left_rotation(node.right, node)
                        self.right_rotation(node.parent, parent)
                    else:
                        raise Exception('Unexpected behavior!')
            else:
                self.modify_balance_factor(parent)

    def left_rotation(self, node: Node, parent: Node):
        grand_parent = parent.parent
        old_left = node.left
        node.left = parent
        parent.right = old_left
        if old_left is not None:
            old_left.parent = parent
        parent.parent = node
        node.parent = grand_parent
        if grand_parent is None:
            self.root = node
        else:
            if grand_parent.value > node.value:
                grand_parent.left = node
            else:
                grand_parent.right = node
        parent.balance_factor = 0
        node.balance_factor = 0

    def right_rotation(self, node: Node, parent: Node):
        grand_parent = parent.parent
        old_right = node.right
        node.right = parent
        parent.left = old_right
        if old_right is not None:
            old_right.parent = parent
        parent.parent = node
        node.parent = grand_parent
        if grand_parent is None:
            self.root = node
        else:
            if grand_parent.value > node.value:
                grand_parent.left = node
            else:
                grand_parent.right = node
        parent.balance_factor = 0
        node.balance_factor = 0

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
#
# avl = AvlTree()
# avl.add(20)
# avl.add(10)
# avl.add(25)
# avl.add(30)
# avl.add(27)
# print(list(avl))