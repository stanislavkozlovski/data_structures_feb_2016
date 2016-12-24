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
        if not self.root:
            self.root = Node(value, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
            self.count += 1
            return
        parent, node_dir = self.__find_parent(value)
        if node_dir is None:
            return  # value is in the tree
        new_node = Node(value=value, color=RED, parent=parent, left=NIL_LEAF, right=NIL_LEAF)
        if node_dir == 'left':
            parent.left = new_node
        else:
            parent.right = new_node

        if parent.color == RED:
            grandfather = parent.parent
            if not grandfather: return
            if grandfather.value > parent.value:
                # parent is on the left
                uncle = grandfather.right
                # check right
                if uncle.color == NIL:
                    if node_dir == 'left':
                        """
                        LL => Right Rotation!
                        """
                        parent.left = new_node
                        parent.right = grandfather

                        grand_grandfather = grandfather.parent
                        self.update_parent(node=parent, parent_old_child=grandfather, new_parent=grand_grandfather)
                        grandfather.parent = parent
                        parent.color = BLACK
                        grandfather.color = RED
                        grandfather.left = NIL_LEAF
                    else:  # value is on the right
                        """
                        RL => Left-Right rotation!
                        """
                        self.left_right_rotation(new_node, parent, grandfather)

                elif uncle.color == BLACK:
                    raise Exception('Should not be here')
                else:  # RED UNCLE
                    self.recolor(parent, grandfather)
            else:
                # parent is on the right
                uncle = grandfather.left
                # check left
                if uncle.color == NIL:
                    if node_dir == 'left':
                        """
                        LR => Right-Left rotation
                        """
                        # RIGHT
                        grandfather.right = new_node
                        new_node.parent = grandfather
                        new_node.right = parent
                        parent.parent = new_node
                        parent.left = NIL_LEAF
                        # LEFT
                        # due to the prev rotation, our node is now the parent
                        self.left_rotation(node=parent, parent=new_node, grandfather=grandfather, to_recolor=True)

                    else:  # new node is on the RIGHT
                        """
                        RR => Left Rotation
                        """
                        self.left_rotation(node=new_node, parent=parent, grandfather=grandfather, to_recolor=True)
                elif uncle.color == BLACK:
                    raise Exception('Should not be here!')
                else:  # RED SIBLING
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

    def left_right_rotation(self, node, parent, grandfather):
        """
        LEFT -> RIGHT ROTATION
        """
        # LEFT ROTATION
        """
        __2B__                                                    __2B__             RIGHT ROTATION (RECOLOR) TO
     1B      ___5R___             ---LEFT  ROTATION TO-->       1B   ___5R___             __2B__
           4B      _9B_                                             4B      9B          1B    ___5R___
         3R       6R                                               3R      7R                4B      7B
                   7R                                                     6B                3R     6R  9R
        """
        self.left_rotation(node=None, parent=node, grandfather=parent)

        # node.left = parent
        # node.parent = grandfather
        #
        # parent.right = NIL_LEAF
        # parent.parent = node

        # RIGHT ROTATIONs
        grand_grandfather = grandfather.parent
        if grand_grandfather:
            if grandfather.value > grand_grandfather.value:
                grand_grandfather.right = node
            else:
                grand_grandfather.left = node
        else:
            self.root = node
        node.parent = grand_grandfather
        node.right = grandfather
        grandfather.left = NIL_LEAF
        grandfather.parent = node


        node.color = BLACK
        grandfather.color = RED
        parent.color = RED

    def recolor(self, parent, grandfather):
        grandfather.right.color = BLACK
        grandfather.left.color = BLACK
        if grandfather != self.root:
            grandfather.color = RED
        self._check_after_recolor(grandfather)

    def _check_after_recolor(self, node):
        parent = node.parent
        value = node.value
        if parent is None: return
        if parent.color == RED:  # TODO: RECOLOR
            grandfather = parent.parent
            if not grandfather: return
            if grandfather.value > parent.value:
                # parent is on the left
                # check right
                if grandfather.right.color == NIL:
                    if value < parent.value:  # TODO: RIGHT ROTATION
                        # value is on parent's left & parent is on par_parent's left, so we do a right rotation
                        parent.left = node
                        parent.right = grandfather
                        parent.color = BLACK

                        par_par_parent = grandfather.parent
                        parent.parent = par_par_parent
                        if par_par_parent:
                            if par_par_parent.value > grandfather.value:
                                par_par_parent.left = parent
                            else:
                                par_par_parent.right = parent
                        grandfather.parent = parent
                        grandfather.color = RED
                        grandfather.left = NIL_LEAF
                    else:  # value is on the right
                        """
                        RL => Left-Right rotation
                        """
                        self.left_right_rotation(node, parent, grandfather)
                elif grandfather.right.color == BLACK:
                    """
                    LL => R
                    RL => LR
                    """
                    # since we're here, the second letter is always L
                    if parent.value > value:
                        # Right rotation with recolor!
                        """
                           15                          10
                Node---> 10       should become      1   15
                        1  12                           12
                        """
                        parent.left = node.right
                        node.right.parent = parent
                        node.right = parent
                        grandfather = parent.parent
                        parent.parent = node
                        if grandfather:
                            if grandfather.value > parent.value:
                                grandfather.left = node
                            else:
                                grandfather.right = node
                                raise Exception('Not sure, but I think we dont need to be here')
                        else:  # grandfather was the root
                            self.root = node
                        node.parent = grandfather
                        node.color = BLACK
                        node.left.color = RED
                        node.right.color = RED
                    else:
                        # TODO: MOVE TO RECURSION BELOWW
                        # TODO RL = LR => Left rotation, right rotation
                        # Left rotation!
                        self.left_rotation(node=None, parent=node, grandfather=parent)

                        # Right rotation!
                        grandfather.left = node.right
                        node.right.parent = grandfather
                        node.right = grandfather
                        par_par_parent = grandfather.parent  # get the upper parent
                        grandfather.parent = node  # and attach the new one
                        node.parent = par_par_parent
                        if par_par_parent:
                            if par_par_parent.value > grandfather.value:
                                par_par_parent.left = node
                            else:
                                par_par_parent.right = node
                        else:  # parent was the last root
                            self.root = node

                        node.color = BLACK
                        grandfather.color = RED
                        node.left.color = RED
                        # TIME: 17m
                        # TODO: TEST
                        pass
                    # TODO: RUN
                    pass
                else:  # RED SIBLING
                    grandfather.right.color = BLACK
                    grandfather.left.color = BLACK
                    if grandfather != self.root:
                        grandfather.color = RED
                    self._check_after_recolor(parent)
                    # TODO: CHECK
                    pass
                pass
            else:
                # parent is on the right
                # check left
                if grandfather.left.color == NIL:
                    # TODO: ROTATE, RECOLOR
                    if value < parent.value: # new node is on the LEFT
                        # RIGHT LEFT ROTATION I THINK
                        # RIGHT
                        grandfather.right = node
                        node.parent = grandfather
                        node.right = parent
                        node.color = BLACK
                        parent.color = RED
                        grandfather.color = RED
                        parent.parent = node
                        parent.left = NIL_LEAF
                        # LEFT
                        par_par_parent = grandfather.parent
                        if par_par_parent.value > grandfather.value:
                            par_par_parent.left = node
                        else:
                            par_par_parent.right = node
                        node.parent = par_par_parent
                        node.left = grandfather
                        grandfather.right = NIL_LEAF
                        grandfather.parent = node
                        pass
                    else:
                        """
                        RR => Left rotation
                        """
                        self.left_rotation(node=node, parent=parent, grandfather=grandfather)
                    pass
                elif grandfather.left.color == BLACK:
                    """
                    RR => L
                    LR => RL
                    """
                    # Since we're here, second letter is always R
                    if parent.value > value:
                        # value is at the left: LR
                        """
                        LR => RIGHT-LEFT ROTATION
                        """
                        # RIGHT
                        grandfather.right = node
                        node.parent = grandfather
                        node.right = parent
                        parent.parent = node
                        parent.left = NIL_LEAF
                        # LEFT
                        # due to the prev rotation, our node is now the parent
                        self.left_rotation(node=parent, parent=node, grandfather=grandfather, to_recolor=True)
                        pass
                    else:
                        """
                        RR => LEFT ROTATION
                        """
                        self.left_rotation(node=node, parent=parent, grandfather=grandfather, to_recolor=True)
                else:  # RED SIBLING
                    grandfather.right.color = BLACK
                    grandfather.left.color = BLACK
                    if grandfather != self.root:
                        grandfather.color = RED
                    self._check_after_recolor(parent)
                    pass
                pass

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

    def __find_parent(self, value):
        """ Finds a place for the value in our binary tree"""
        def __find(parent):
            if value == parent.value:
                return None, None
            elif parent.value < value:
                if parent.right.color == NIL:  # no more to go
                    return parent, 'right'
                return __find(parent.right)
            elif value < parent.value:
                if parent.left.color == NIL:  # no more to go
                    return parent, 'left'
                return __find(parent.left)

        return __find(self.root)







