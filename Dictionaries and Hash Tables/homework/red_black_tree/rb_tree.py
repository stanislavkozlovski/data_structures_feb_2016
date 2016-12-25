BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'


class Node:
    def __init__(self, value, color, parent, left=None, right=None):
        self.value = value
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return '{color} {val} Node'.format(color=self.color, val=self.value)


class RedBlackTree:
    NIL_LEAF = Node(value=None, color=NIL, parent=None)

    def __init__(self):
        self.count = 0
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value, color=BLACK, parent=None, left=self.NIL_LEAF, right=self.NIL_LEAF)
            self.count += 1
            return
        parent, node_dir = self.__find_parent(value)
        if node_dir is None:
            return  # value is in the tree
        new_node = Node(value=value, color=RED, parent=parent, left=self.NIL_LEAF, right=self.NIL_LEAF)
        if node_dir == 'L':
            parent.left = new_node
        else:
            parent.right = new_node

        self.try_rebalance(new_node)
        self.count += 1

    def remove(self, value):
        node_to_remove = self.find_node(value)
        if node_to_remove is None:
            return
        if node_to_remove.color == RED:
            # TODO: THANK GOD
            if node_to_remove.left != self.NIL_LEAF and node_to_remove.right != self.NIL_LEAF:
                # find in order successor  # once right, left till end
                # replace node_to_remove with successor and gg
                successor = self.find_in_order_successor(node_to_remove)
                if successor.color == RED:
                    if successor.left == self.NIL_LEAF and successor.right == self.NIL_LEAF:
                        # TODO: THANK GOD MORE
                        # switch the value and remove the successor (they are both red)
                        node_to_remove.value = successor.value
                        successor.parent.left = self.NIL_LEAF
                        del successor
                    else:
                        """
                        Since the successor is red he cannot have children
                        1. Cannot have a left child, otherwise he wouldn't be a successor
                        2. Cannot have a right child either
                            1. If he has a right child, it must be black, otherwise red-red
                            2. Since he has a right black child, his left child must also be black,
                                otherwise the black height of the tree is invalid
                        """
                        raise Exception('Unexpected behavior')
                else:  # successor is black!
                    pass
            else:
                pass
        else:
            pass


    def try_rebalance(self, node):
        parent = node.parent
        value = node.value
        if (parent is None  # what the fuck?
            or parent.parent is None  # at the root
            or parent.color != RED):  # no need to rebalance
            return
        grandfather = parent.parent
        node_dir = 'L' if parent.value > value else 'R'
        parent_dir = 'L' if grandfather.value > parent.value else 'R'
        uncle = grandfather.right if parent_dir == 'L' else grandfather.left
        general_direction = node_dir + parent_dir

        if uncle == self.NIL_LEAF or uncle.color == BLACK:
            # rotate
            if general_direction == 'LL':
                self.right_rotation(node, parent, grandfather, to_recolor=True)
            elif general_direction == 'RR':
                self.left_rotation(node, parent, grandfather, to_recolor=True)
            elif general_direction == 'LR':
                self.right_rotation(node=None, parent=node, grandfather=parent)
                # due to the prev rotation, our node is now the parent
                self.left_rotation(node=parent, parent=node, grandfather=grandfather, to_recolor=True)
            elif general_direction == 'RL':
                self.left_rotation(node=None, parent=node, grandfather=parent)
                # due to the prev rotation, our node is now the parent
                self.right_rotation(node=parent, parent=node, grandfather=grandfather, to_recolor=True)
            else:
                raise Exception("{} is not a valid direction!".format(general_direction))
        else:  # RED
            self.recolor(parent, grandfather)

    def update_parent(self, node, parent_old_child, new_parent):
        """
        Our node 'switches' places with the old child
        Assigns a new parent to the node.
        If the new_parent is None, this means that our node becomes the root of the tree
        """
        node.parent = new_parent
        if new_parent:
            # Determine the old child's position in order to put node there
            if new_parent.value > parent_old_child.value:
                new_parent.left = node
            else:
                new_parent.right = node
        else:
            self.root = node

    def right_rotation(self, node, parent, grandfather, to_recolor=False):
        grand_grandfather = grandfather.parent
        self.update_parent(node=parent, parent_old_child=grandfather, new_parent=grand_grandfather)

        old_right = parent.right
        parent.right = grandfather
        grandfather.parent = parent

        grandfather.left = old_right  # save the old right values
        old_right.parent = grandfather

        if to_recolor:
            parent.color = BLACK
            node.color = RED
            grandfather.color = RED

    def left_rotation(self, node, parent, grandfather, to_recolor=False):
        grand_grandfather = grandfather.parent
        self.update_parent(node=parent, parent_old_child=grandfather, new_parent=grand_grandfather)

        old_left = parent.left
        parent.left = grandfather
        grandfather.parent = parent

        grandfather.right = old_left  # save the old left values
        old_left.parent = grandfather

        if to_recolor:
            parent.color = BLACK
            node.color = RED
            grandfather.color = RED

    def recolor(self, parent, grandfather):
        grandfather.right.color = BLACK
        grandfather.left.color = BLACK
        if grandfather != self.root:
            grandfather.color = RED
        self.try_rebalance(grandfather)

    def __find_parent(self, value):
        """ Finds a place for the value in our binary tree"""
        def __find(parent):
            if value == parent.value:
                return None, None
            elif parent.value < value:
                if parent.right.color == NIL:  # no more to go
                    return parent, 'R'
                return __find(parent.right)
            elif value < parent.value:
                if parent.left.color == NIL:  # no more to go
                    return parent, 'L'
                return __find(parent.left)

        return __find(self.root)

    def find_node(self, value):
        def __find_node(root):
            if root == self.NIL_LEAF:
                return None
            if value > root.value:
                return __find_node(root.right)
            elif value < root.value:
                return __find_node(root.left)
            else:
                return root

        found_node = __find_node(self.root)
        return found_node


    # Too confusing, maybe after the tree is fully implemented.
    # def rotate(self, node, parent, grandfather, rot_dir, to_recolor=False):
    #     RIGHT_ROTATION = rot_dir == 'R'
    #     grand_grandfather = grandfather.parent
    #     self.update_parent(node=parent, parent_old_child=grandfather, new_parent=grand_grandfather)
    #     old_value = parent.right if RIGHT_ROTATION else parent.left
    #
    #     parent.right = grandfather if RIGHT_ROTATION else parent.left = grandfather
    #     grandfather.parent = parent
    #
    #     grandfather.left = old_value if RIGHT_ROTATION else grandfather.right = old_value
    #     old_value.parent = grandfather
    #
    #     if to_recolor:
    #         parent.color = BLACK
    #         node.color = RED
    #         grandfather.color = RED

    def find_in_order_successor(self, node):
        right_node = node.right
        left_node = right_node.left
        if left_node == self.NIL_LEAF:
            return right_node
        while left_node.left != self.NIL_LEAF:
            left_node = left_node.left
        return left_node




