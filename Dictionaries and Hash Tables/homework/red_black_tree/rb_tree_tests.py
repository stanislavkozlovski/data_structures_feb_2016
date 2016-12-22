import unittest

from rb_tree import RedBlackTree, Node, NIL_LEAF
BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'


class RbTreeTests(unittest.TestCase):
    def test_recoloring_only(self):
        """
        Create a red-black tree, add a red node such that we only have to recolor
        upwards twice
        add 4, which recolors 2 and 8 to BLACK,
                6 to RED
                    -10, 20 to BLACK
        :return:
        """
        tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None)
        # LEFT SUBTREE
        first_left = Node(value=-10, color=RED, parent=root) #OK
        left_right = Node(value=6, color=BLACK, parent=first_left) #OK
        rightest = Node(value=8, color=RED, parent=left_right, left=NIL_LEAF, right=NIL_LEAF) #OK
        rightest_left = Node(value=2, color=RED, parent=left_right, left=NIL_LEAF, right=NIL_LEAF) #OK
        left_right.left = rightest_left #OK
        left_right.right = rightest #OK
        leftest = Node(value=-20, color=BLACK, parent=first_left, left=NIL_LEAF, right=NIL_LEAF) #OK
        first_left.left = leftest #OK
        first_left.right = left_right #OK

        # RIGHT SUBTREE
        first_right = Node(value=20, color=RED, parent=root) #OK
        right_left = Node(value=15, color=BLACK, parent=first_right, left=NIL_LEAF, right=NIL_LEAF) #OK
        right_right = Node(25, color=BLACK, parent=first_right, left=NIL_LEAF, right=NIL_LEAF) #OK
        first_right.left = right_left #OK
        first_right.right = right_right #OK

        root.left = first_left #OK
        root.right = first_right #OK

        tree.root = root
        tree.add(4)
        print()#TODO parents do not get updated, see node 2/4 for reference

    def test_right_rotation(self):
        tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None)

        # LEFT SUBTREE
        leftest = Node(value=-10, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
        left_right = Node(value=7, color=RED, parent=leftest, left=NIL_LEAF, right=NIL_LEAF)
        leftest.right = left_right

        # RIGHT SUBTREE
        rightest = Node(value=20, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
        right_left = Node(value=15, color=RED, parent=rightest, left=NIL_LEAF, right=NIL_LEAF)
        rightest.left = right_left

        root.left = leftest
        root.right = rightest

        tree.root = root
        tree.add(13)
        print()

if __name__ == '__main__':
    unittest.main()