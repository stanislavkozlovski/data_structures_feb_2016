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

    def has_children(self) -> bool:
        """ Returns a boolean indicating if the node has children """
        if self.color == NIL:
            return False
        return self.left.color != NIL or self.right.color != NIL


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
        """
        1.Always try to find a successor so that the node has 0 or 1 children :)
        2.Replace value with said successor
        """
        if node_to_remove.left != self.NIL_LEAF and node_to_remove.right != self.NIL_LEAF:
            # find in order successor  # once right, left till end
            # replace node_to_remove with successor and gg
            successor = self.find_in_order_successor(node_to_remove)
            node_to_remove.value = successor.value  # switch the value
            if successor.color == RED:
                if successor.left == self.NIL_LEAF and successor.right == self.NIL_LEAF:
                    # TODO: THANK GOD
                    # remove the successor from the tree
                    if successor.value == successor.parent.value:
                        # in those weird cases where
                        # the successor is the right node
                        successor.parent.right = self.NIL_LEAF
                    else:
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
                right_node = successor.right
                if right_node.has_children(): raise Exception('The red right child of a black successor cannot have children, otherwise the black height of the tree becomes invalid! ')
                if successor.right.color == RED:
                    # swap the values with the right node and remove the right node
                    successor.value = right_node.value
                    successor.right = self.NIL_LEAF
                    del right_node
                elif successor.right == self.NIL_LEAF:
                    # 6 cases :o
                    self.f_remove(successor)
                else:
                    raise Exception('Black successor cannot have a black right child, black height is invalid')
        else:
            # has 0 or 1 children!
            if node_to_remove == self.root:
                if self.root.left != self.NIL_LEAF:
                    self.root = self.root.left
                elif self.root.right != self.NIL_LEAF:
                    self.root = self.root.right
                else:
                    self.root = None
                    return
                self.root.parent = None
                self.root.color = BLACK
                return

            if node_to_remove.color == RED:
                if node_to_remove.left == self.NIL_LEAF and node_to_remove.right == self.NIL_LEAF:
                    # TODO: THANK GOD
                    # remove the node_to_remove from the tree
                    if node_to_remove.value > node_to_remove.parent.value:
                        node_to_remove.parent.right = self.NIL_LEAF
                    else:
                        node_to_remove.parent.left = self.NIL_LEAF
                    del node_to_remove
            else:
                right_node = node_to_remove.right
                if right_node.has_children(): raise Exception(
                    'The red right child of a black node_to_remove cannot have children, otherwise the black height of the tree becomes invalid! ')
                if node_to_remove.right.color == RED:
                    # swap the values with the right node and remove the right node
                    node_to_remove.value = right_node.value
                    node_to_remove.right = self.NIL_LEAF
                    del right_node
                elif node_to_remove.right == self.NIL_LEAF:
                    # 6 cases :o
                    self.f_remove(node_to_remove)
                else:
                    raise Exception('Black node with one child cannot have a black right child, black height is invalid')

    def f_remove(self, node):
        # recursively call each case
        # if the case is not terminating, call case_1 again and go through the chain of cases
        self.case_1(node)
        if node.value >= node.parent.value:
            node.parent.right = self.NIL_LEAF
        else:
            node.parent.left = self.NIL_LEAF

    def case_1(self, node):
        if self.root == node:
            node.color = BLACK
            return
        self.case_2(node)

    def case_2(self, node):
        parent = node.parent
        sibling, direction = self.get_sibling(node)
        if sibling.color == RED and parent.color == BLACK and (sibling.left.color != RED and sibling.right.color != RED):
            if direction == 'R':
                self.left_rotation(node=None, parent=sibling, grandfather=parent)
                parent.color = RED
                sibling.color = BLACK
            else:
                self.right_rotation(node=None, parent=sibling, grandfather=parent)
                parent.color = RED
                sibling.color = BLACK
            return self.case_1(node)
        self.case_3(node)

    def case_3(self, node):
        parent = node.parent
        sibling, _ = self.get_sibling(node)
        if (sibling.color == BLACK
           and sibling.left.color != RED
           and sibling.right.color != RED
           and parent.color == BLACK):
            # color the sibling red and forward the double black node upwards
            # (call the cases again for the parent)
            sibling.color = RED
            self.case_1(parent)
            return

        self.case_4(node)

    def case_4(self, node):
        if node.parent.color == RED:
            sibling, direction = self.get_sibling(node)
            if sibling.color == BLACK and (sibling.left.color != RED and sibling.right.color != RED):
                # switch colors
                node.parent.color = BLACK
                sibling.color = RED
                return
        self.case_5(node)

    def case_5(self, node):
        # TODO: Case 5 is always followed by 6 methinks
        sibling, direction = self.get_sibling(node)
        if node.parent.color != NIL and sibling.color == BLACK:  # HUH?
            if direction == 'L':
                if sibling.left.color != RED and sibling.right.color == RED:
                    right_sib = sibling.right
                    self.left_rotation(node=None, parent=sibling.right, grandfather=sibling)
                    right_sib.color = BLACK
                    sibling.color = RED
                    return self.case_1(node)
            else:
                # sibling is at the right
                if sibling.left.color == RED and sibling.right.color != RED:
                    left_sib = sibling.left
                    self.right_rotation(node=None, parent=sibling.left, grandfather=sibling)
                    left_sib.color = BLACK
                    sibling.color = RED
                    return self.case_1(node)

        self.case_6(node)

    def case_6(self, node):
        sibling, direction = self.get_sibling(node)
        if direction == 'R':
            if (sibling.color == BLACK
               and sibling.right.color == RED):
                parent_color = sibling.parent.color
                self.left_rotation(node=None, parent=sibling, grandfather=sibling.parent)
                # new parent is sibling
                sibling.color = parent_color
                sibling.right.color = BLACK
                sibling.left.color = BLACK
                return
        else:
            if (sibling.color == BLACK
               and sibling.left.color == RED):
                parent_color = sibling.parent.color
                self.right_rotation(node=None, parent=sibling, grandfather=sibling.parent)
                # new parent is sibling
                sibling.color = parent_color
                sibling.right.color = BLACK
                sibling.left.color = BLACK
                return

        raise Exception('We should have ended here, something is wrong')

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

    def contains(self, value) -> bool:
        """ Returns a boolean indicating if the given value is present in the tree """
        return bool(self.find_node(value))


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

    def get_sibling(self, node):
        parent = node.parent
        if node.value >= parent.value:
            sibling = parent.left
            direction = 'L'
        else:
            sibling = parent.right
            direction = 'R'
        return sibling, direction



