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


NIL_LEAF = Node(value=None, color=NIL, parent=None)


class RedBlackTree:
    def __init__(self):
        self.count = 0
        self.root = None

    def add(self, value):
        # TODO: Rebalance function
        if not self.root:
            self.root = Node(value, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
            self.count += 1
            return
        parent, node_dir = self.__find_parent(value)
        if node_dir is None:
            return  # value is in the tree
        new_node = Node(value=value, color=RED, parent=parent, left=NIL_LEAF, right=NIL_LEAF)
        if node_dir == 'L':
            parent.left = new_node
        else:
            parent.right = new_node
        grandfather = parent.parent
        if not grandfather:
            return

        parent_dir = 'L' if grandfather.value > parent.value else 'R'
        general_dir = node_dir + parent_dir
        uncle = grandfather.right if parent_dir == 'L' else grandfather.left
        if parent.color != RED:
            return

        if uncle.color == NIL:
            if general_dir == 'LL':  # ==> R
                self.right_rotation(new_node, parent, grandfather, to_recolor=True)
            elif general_dir == 'RR': # ==> L
                self.left_rotation(new_node, parent, grandfather, to_recolor=True)
            elif general_dir == 'LR': # ==> RL
                self.right_rotation(node=None, parent=new_node, grandfather=parent)
                # due to the prev rotation, our node is now the parent
                self.left_rotation(node=parent, parent=new_node, grandfather=grandfather, to_recolor=True)
            elif general_dir == 'RL':  # ==> LR
                self.left_rotation(node=None, parent=new_node, grandfather=parent)
                self.right_rotation(node=parent, parent=new_node, grandfather=grandfather, to_recolor=True)
            else:
                raise Exception('{} is not a valid direction!'.format(general_dir))
        elif uncle.color == BLACK:
            raise Exception('Uncle should not be black before a recolor')
        else:  # RED
            self.recolor(parent, grandfather)
        return
      
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
        self._check_after_recolor(grandfather)

    def _check_after_recolor(self, node):
        parent = node.parent
        value = node.value
        if parent is None or parent.parent is None:  # at the root
            return
        if parent.color != RED:
            return
        grandfather = parent.parent
        node_dir = 'L' if parent.value > value else 'R'
        parent_dir = 'L' if grandfather.value > parent.value else 'R'
        uncle = grandfather.right if parent_dir == 'L' else grandfather.left
        general_direction = node_dir + parent_dir

        if uncle == NIL_LEAF:
            raise Exception('The uncle cannot be NIL after a recolor!')
        elif uncle.color == BLACK:
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







