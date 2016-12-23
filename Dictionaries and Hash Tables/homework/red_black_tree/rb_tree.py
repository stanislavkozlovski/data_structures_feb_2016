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
                    if node_dir == 'left':  # TODO: RIGHT ROTATION
                        # value is on parent's left & parent is on grandfather's left, so we do a right rotation
                        parent.left = new_node
                        parent.right = grandfather
                        parent.color = BLACK

                        grand_grandfather = grandfather.parent
                        parent.parent = grand_grandfather
                        if grand_grandfather:
                            if grand_grandfather.value > grandfather.value:
                                grand_grandfather.left = parent
                            else:
                                grand_grandfather.right = parent
                        else:
                            self.root = parent
                        grandfather.parent = parent
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
                    grandfather.right.color = BLACK
                    grandfather.left.color = BLACK
                    if grandfather != self.root:
                        grandfather.color = RED
                    self._check_after_recolor(grandfather)
            else:
                # parent is on the right
                uncle = grandfather.left
                # check left
                if uncle.color == NIL:
                    if value < parent.value: # new node is on the LEFT
                        """
                        LR => Right-Left rotation
                        """
                        # RIGHT LEFT ROTATION I THINK
                        # RIGHT
                        grandfather.right = new_node
                        new_node.parent = grandfather
                        new_node.right = parent
                        new_node.color = BLACK
                        parent.color = RED
                        grandfather.color = RED
                        parent.parent = new_node
                        parent.left = NIL_LEAF
                        # LEFT
                        grand_grandfather = grandfather.parent
                        if grand_grandfather.value > grandfather.value:
                            grand_grandfather.left = new_node
                        else:
                            grand_grandfather.right = new_node
                        new_node.parent = grand_grandfather
                        new_node.left = grandfather
                        grandfather.right = NIL_LEAF
                        grandfather.parent = new_node
                    else:  # new node is on the RIGHT
                        """
                        RR => Left Rotation
                        """
                        # LEFT ROTATION
                        parent.left = grandfather
                        parent.parent = grandfather.parent
                        grandfather.right = NIL_LEAF
                        grand_grandfather = grandfather.parent
                        grandfather.parent = parent
                        if grand_grandfather.value > grandfather.value:
                            grand_grandfather.left = parent
                        else:
                            grand_grandfather.right = parent
                        parent.right = new_node
                        # recolor
                        parent.color = BLACK
                        new_node.color = RED
                        grandfather.color = RED
                elif uncle.color == BLACK:
                    raise Exception('Should not be here!')
                else:  # RED SIBLING
                    grandfather.right.color = BLACK
                    grandfather.left.color = BLACK
                    if grandfather != self.root:
                        grandfather.color = RED
                    self._check_after_recolor(grandfather)
                    pass
                pass

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
        node.left = parent
        node.parent = grandfather

        parent.right = NIL_LEAF
        parent.parent = node
        grand_grandfather = grandfather.parent

        # RIGHT ROTATION
        node.parent = grandfather.parent
        node.right = grandfather
        grandfather.left = NIL_LEAF
        grandfather.parent = node

        if grand_grandfather:
            if grandfather.value > grand_grandfather.value:
                grand_grandfather.right = node
            else:
                grand_grandfather.left = node
        else:
            self.root = node

        node.color = BLACK
        grandfather.color = RED
        parent.color = RED

    def _check_after_recolor(self, node):
        parent = node.parent
        value = node.value
        if parent is None: return
        if parent.color == RED:  # TODO: RECOLOR
            par_parent = parent.parent
            if not par_parent: return
            if par_parent.value > parent.value:
                # parent is on the left
                # check right
                if par_parent.right.color == NIL:
                    if value < parent.value:  # TODO: RIGHT ROTATION
                        # value is on parent's left & parent is on par_parent's left, so we do a right rotation
                        parent.left = node
                        parent.right = par_parent
                        parent.color = BLACK

                        par_par_parent = par_parent.parent
                        parent.parent = par_par_parent
                        if par_par_parent:
                            if par_par_parent.value > par_parent.value:
                                par_par_parent.left = parent
                            else:
                                par_par_parent.right = parent
                        par_parent.parent = parent
                        par_parent.color = RED
                        par_parent.left = NIL_LEAF
                    else:  # value is on the right
                        """
                        RL => Left-Right rotation
                        """
                        self.left_right_rotation(node, parent, grandfather)
                elif par_parent.right.color == BLACK:
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
                        parent.right = node.left
                        node.left.parent = parent
                        node.left = parent
                        parent.parent = node
                        node.parent = par_parent
                        par_parent.left = node

                        # Right rotation!
                        par_parent.left = node.right
                        node.right.parent = par_parent
                        node.right = par_parent
                        par_par_parent = par_parent.parent  # get the upper parent
                        par_parent.parent = node  # and attach the new one
                        node.parent = par_par_parent
                        if par_par_parent:
                            if par_par_parent.value > par_parent.value:
                                par_par_parent.left = node
                            else:
                                par_par_parent.right = node
                        else:  # parent was the last root
                            self.root = node

                        node.color = BLACK
                        par_parent.color = RED
                        node.left.color = RED
                        # TIME: 17m
                        # TODO: TEST
                        pass
                    # TODO: RUN
                    pass
                else:  # RED SIBLING
                    par_parent.right.color = BLACK
                    par_parent.left.color = BLACK
                    if par_parent != self.root:
                        par_parent.color = RED
                    self._check_after_recolor(par_parent)
                    # TODO: CHECK
                    pass
                pass
            else:
                # parent is on the right
                # check left
                if par_parent.left.color == NIL:
                    # TODO: ROTATE, RECOLOR
                    if value < parent.value: # new node is on the LEFT
                        # RIGHT LEFT ROTATION I THINK
                        # RIGHT
                        par_parent.right = node
                        node.parent = par_parent
                        node.right = parent
                        node.color = BLACK
                        parent.color = RED
                        par_parent.color = RED
                        parent.parent = node
                        parent.left = NIL_LEAF
                        # LEFT
                        par_par_parent = par_parent.parent
                        if par_par_parent.value > par_parent.value:
                            par_par_parent.left = node
                        else:
                            par_par_parent.right = node
                        node.parent = par_par_parent
                        node.left = par_parent
                        par_parent.right = NIL_LEAF
                        par_parent.parent = node
                        pass
                    else:  # new node is on the RIGHT
                        # LEFT ROTATION
                        parent.left = par_parent
                        parent.parent = par_parent.parent
                        par_parent.right = NIL_LEAF
                        par_par_parent = par_parent.parent
                        par_parent.parent = parent
                        if par_par_parent.value > par_parent.value:
                            par_par_parent.left = parent
                        else:
                            par_par_parent.right = parent
                        parent.right = node
                        # recolor
                        parent.color = BLACK
                        node.color = RED
                        par_parent.color = RED
                        pass
                    pass
                elif par_parent.left.color == BLACK:
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
                        pass
                    else:
                        """
                        RR => LEFT ROTATION
                        """
                        par_parent.right = parent.left
                        parent.left.parent = par_parent
                        parent.left = par_parent
                        parent.parent = par_parent.parent
                        par_par_parent = par_parent.parent
                        par_parent.parent = parent
                        if par_par_parent:
                            if par_par_parent.value > par_parent.value:
                                par_par_parent.left = parent
                            else:
                                par_par_parent.right = parent
                        else:
                            self.root = parent
                        parent.right = node
                        # recolor
                        parent.color = BLACK
                        node.color = RED
                        par_parent.color = RED
                        pass
                    # TODO: RUN
                    pass
                else:  # RED SIBLING
                    par_parent.right.color = BLACK
                    par_parent.left.color = BLACK
                    if par_parent != self.root:
                        par_parent.color = RED
                    self._check_after_recolor(par_parent)
                    pass
                pass

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