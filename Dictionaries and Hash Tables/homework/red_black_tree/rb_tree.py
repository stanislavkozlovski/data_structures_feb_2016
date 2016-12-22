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
        parent, dir = self.__find_parent(value)
        if dir is None:
            return  # value is in the tree
        new_node = Node(value=value, color=RED, parent=parent, left=NIL_LEAF, right=NIL_LEAF)
        if dir == 'left':
            parent.left = new_node
        else:
            parent.right = new_node

        if parent.color == RED:  # TODO: RECOLOR
            par_parent = parent.parent
            if not par_parent: return
            if par_parent.value > parent.value:
                # parent is on the left
                # check right
                if par_parent.right.color != RED:
                    if value < parent.value:  # TODO: RIGHT ROTATION
                        # value is on parent's left & parent is on par_parent's left, so we do a right rotation
                        parent.left = new_node
                        parent.right = par_parent
                        parent.color = BLACK

                        par_par_parent = par_parent.parent
                        if par_par_parent:
                            if par_par_parent.value > par_parent.value:
                                par_par_parent.left = parent
                            else:
                                par_par_parent.right = parent
                        par_parent.parent = parent
                        par_parent.color = RED
                        par_parent.left = NIL_LEAF

                    # TODO: ROTATE, RECOLOR
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
                if par_parent.left.color != RED:
                    # TODO: ROTATE, RECOLOR
                    pass
                else:  # RED SIBLING
                    par_parent.right.color = BLACK
                    par_parent.left.color = BLACK
                    if par_parent != self.root:
                        par_parent.color = RED
                    self._check_after_recolor(par_parent)
                    pass
                pass

    def _check_after_recolor(self, node):
        parent = node.parent
        if parent is None: return
        if parent.color == RED:
            par_parent = parent.parent
            if not par_parent: return
            if par_parent.value > parent.value:
                # parent is on the left
                # check right
                if par_parent.right.color != RED:
                    # TODO: ROTATE, RECOLOR
                    pass
                else:  # RED SIBLING
                    par_parent.right.color = BLACK
                    par_parent.left.color = BLACK
                    if par_parent != self.root:
                        par_parent.color = RED
                    self._check_after_recolor(par_parent)
                    pass
                pass
            else:
                # parent is on the right
                # check left
                if par_parent.left.color != RED:
                    # TODO: ROTATE, RECOLOR
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