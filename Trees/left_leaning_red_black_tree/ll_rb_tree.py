RED = 'RED'
BLACK = 'BLACK'
NIL = 'NIL'


class Node:
    def __init__(self, value, parent, color, left=None, right=None):
        self.value = value
        self.parent = parent
        self.color = color
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.color} {self.value}'

    def get_parent_and_dir(self):
        if self.parent is None:
            return None, None
        if self.parent.value > self.value:
            return self.parent, 'L'
        else:
            return self.parent, 'R'

    def get_left_sibling(self):
        if self.parent is None:
            return None
        return self.parent.left
NIL_LEAF = Node(value=None, parent=None, color=NIL)

class LLRBTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(value=val, parent=None, color=BLACK, left=NIL_LEAF, right=NIL_LEAF)
            return
        node_to_add, dir = self.__find_node_to_add(val)
        new_node = Node(value=val, parent=node_to_add, color=RED, left=NIL_LEAF, right=NIL_LEAF)
        if dir == 'L':
            node_to_add.left = new_node
        else:
            node_to_add.right = new_node
        self.try_rebalance(node_to_add, dir)
        return

    def try_rebalance(self, parent, dir):
        if dir == 'L':
            # left child was added, check it
            if parent.color == RED and parent.left.color == RED:
                # double red link => right rotation + check further up
                self.right_rotation(parent.parent, to_recolor=True)
                grandfather, dir = parent.get_parent_and_dir()
                if grandfather is not None:
                    self.try_rebalance(grandfather, dir)
        else:
            # right child was added

            # if left sibling is red, simply recolor like a bitch
            if parent.left.color == RED:
                # recolor
                parent.left.color = BLACK
                parent.right.color = BLACK
                parent.color = RED
                self.root.color = BLACK
                grandfather, dir = parent.get_parent_and_dir()
                if grandfather is not None:
                    self.try_rebalance(grandfather, dir)
            else:
                # left rotation
                self.left_rotation(parent, to_recolor=True)

    def left_rotation(self, parent, to_recolor=False):
        """
        X                         X
         \                          \
          Y - parent     ==>       Z
            \                     /
             Z                    Y
        """
        grandfather, grandfather_dir = parent.get_parent_and_dir()
        child = parent.right
        if grandfather is not None:
            if grandfather_dir == 'L':
                grandfather.left = child
            else:
                grandfather.right = child

        child.parent = grandfather
        parent.right = child.left
        child.left = parent
        parent.parent = child
        if self.root == parent:
            self.root = child
        if to_recolor:
            child.color = BLACK
            parent.color = RED

    def right_rotation(self, parent, to_recolor=False):
        """
            X                       X
           /                      /
          Y  - parent    ==>     Z
         /                        \
        Z                          Y
        :param parent:
        :return:
        """
        grandfather, grandfather_dir = parent.get_parent_and_dir()
        child = parent.left
        if grandfather is not None:
            if grandfather_dir == 'L':
                grandfather.left = child
            else:
                grandfather.right = child
        child.parent = grandfather
        parent.left = child.right
        child.right = parent
        parent.parent = child
        if self.root == parent:
            self.root = child
        if to_recolor:
            child.color = RED
            parent.color = BLACK

    def __find_node_to_add(self, val):
        """ Find a node to add to and return the direction on which we'll add to it """
        def __find(root):
            if root is None:
                return
            if val > root.value:
                # go right
                if root.right == NIL_LEAF:
                    return root, 'R'
                return __find(root.right)
            else:
                if root.left == NIL_LEAF:
                    return root, 'L'
                return __find(root.left)
        res = __find(self.root)
        print(res)
        return res
#
# root = Node(value=5, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
# left = Node(value=3, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
# right = Node(value=19, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
# root.left = left
# root.right = right
# leftleft = Node(value=1, color=RED, parent=left, left=NIL_LEAF, right=NIL_LEAF)
# left.left = leftleft
# rightleft = Node(value=18, color=RED, parent=right, left=NIL_LEAF, right=NIL_LEAF)
# right.left = rightleft
#
# tree = LLRBTree()
# tree.root = root
# tree.add(8)
print('a')

rbt = LLRBTree()
rbt.add(5)
rbt.add(12)
rbt.add(18)
rbt.add(37)
rbt.add(48)
rbt.add(60)
rbt.add(80)
print('a')
