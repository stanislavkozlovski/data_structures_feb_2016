import unittest

from homework.red_black_tree.rb_tree import RedBlackTree, Node, NIL_LEAF
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
        """ This should trigger two recolors.
            2 and 8 should turn to black,
            6 should turn to red,
            -10 and 20 should turn to black"""
        node_2 = rightest_left
        node_8 = rightest
        self.assertEqual(node_2.color, BLACK)
        self.assertEqual(node_8.color, BLACK)

        node_6 = left_right
        self.assertEqual(node_6.color, RED)

        node_m10 = first_left
        node_20 = leftest
        self.assertEqual(node_m10.color, BLACK)
        self.assertEqual(node_20.color, BLACK)

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

        """ this should cause a right rotation on 20-15-13 to 15-20-13"""
        self.assertEqual(right_left.color, BLACK)  # this should be the parent of both now
        node_20 = right_left.right
        self.assertEqual(node_20.value, 20)
        self.assertEqual(node_20.color, RED)

        node_13 = right_left.left
        self.assertEqual(node_13.value, 13)
        self.assertEqual(node_13.color, RED)

    def test_left_rotation_no_sibling(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
        # LEFT SUBTREE
        node_7 = Node(value=7, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
        node_8 = Node(value=8, color=RED, parent=node_7, left=NIL_LEAF, right=NIL_LEAF)
        node_7.right = node_8

        # RIGHT SUBTREE
        rightest = Node(value=20, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
        root.left = node_7
        root.right = rightest

        rb_tree.root = root
        rb_tree.add(9)
        """
                 -->     10B                                10B
        ORIGINAL -->  7B    20B  --LEFT ROTATION-->       8B   20B
                 -->    8R                              7R  9R
                 -->     9R
        We add 9, which is the right child of 8 and causes a red-red relationship
        this calls for a left rotation, so 7 becomes left child of 8 and 9 the right child of 8
        8 is black, 7 and 9 are red
        """
        node_9 = node_8.right

        self.assertEqual(node_8.parent.value, 10)
        self.assertEqual(node_8.color, BLACK)
        self.assertEqual(node_8.left.value, 7)
        self.assertEqual(node_8.right.value, 9)

        self.assertEqual(node_7.color, RED)
        self.assertEqual(node_7.parent.value, 8)
        self.assertEqual(node_7.left.color, NIL)
        self.assertEqual(node_7.right.color, NIL)
        self.assertEqual(node_9.value, 9)
        self.assertEqual(node_9.color, RED)
        self.assertEqual(node_9.parent.value, 8)
        self.assertEqual(node_9.left.color, NIL)
        self.assertEqual(node_9.right.color, NIL)

    def test_right_rotation_no_sibling_left_subtree(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
        # LEFT SUBTREE
        node_m10 = Node(value=-10, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
        node_m11 = Node(value=-11, color=RED, parent=node_m10, left=NIL_LEAF, right=NIL_LEAF)
        node_m10.left = node_m11
        # RIGHT SUBTREE
        rightest = Node(value=20, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
        right_left = Node(value=15, color=RED, parent=rightest, left=NIL_LEAF, right=NIL_LEAF)
        rightest.left = right_left

        root.left = node_m10
        root.right = rightest
        rb_tree.root = root
        rb_tree.add(-12)
        """
        red-red relationship with -11 -12, so we do a right rotation where -12 becomes the left child of -11,
                                                                            -10 becomes the right child of -11
        -11's parent is root, -11 is black, -10,-12 are RED
        """
        node_m12 = node_m11.left
        self.assertEqual(node_m12.value, -12)
        self.assertEqual(node_m12.color, RED)
        self.assertEqual(node_m12.parent.value, -11)
        self.assertEqual(node_m12.left.color, NIL)
        self.assertEqual(node_m12.right.color, NIL)

        self.assertEqual(node_m11.color, BLACK)
        self.assertEqual(node_m11.parent.value, 10)  # root parent
        self.assertEqual(node_m11.left.value, -12)
        self.assertEqual(node_m11.right.value, -10)

        self.assertEqual(node_m10.color, RED)
        self.assertEqual(node_m10.parent.value, -11)
        self.assertEqual(node_m10.left.color, NIL)
        self.assertEqual(node_m10.right.color, NIL)

    def test_left_right_rotation_no_sibling(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
        # LEFT PART
        leftest = Node(value=-10, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
        left_right = Node(value=7, color=RED, parent=leftest, left=NIL_LEAF, right=NIL_LEAF)
        leftest.right = left_right

        # RIGHT PART
        rightest = Node(value=20, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
        right_left = Node(value=15, color=RED, parent=rightest, left=NIL_LEAF, right=NIL_LEAF)
        rightest.left = right_left

        root.left=leftest
        root.right=rightest

        rb_tree.root = root
        rb_tree.add(17)
        """
        15-17 should do a left rotation so 17 is now the parent of 15.
        Then, a right rotation should be done so 17 is the parent of 20(15's prev parent)
        Also, a recoloring should be done such that 17 is now black and his children are red
        """
        node_15 = right_left
        node_20 = rightest
        node_17 = node_15.parent
        self.assertEqual(node_17.value, 17)
        self.assertEqual(node_17.color, BLACK)
        self.assertEqual(node_17.parent.value, 10)
        self.assertEqual(node_17.parent.right.value, 17)
        self.assertEqual(node_17.left.value, 15)
        self.assertEqual(node_17.right.value, 20)

        self.assertEqual(node_20.parent.value, 17)
        self.assertEqual(node_20.color, RED)
        self.assertEqual(node_20.left.color, NIL)
        self.assertEqual(node_20.right.color, NIL)

        self.assertEqual(node_15.parent.value, 17)
        self.assertEqual(node_15.color, RED)
        self.assertEqual(node_15.left.color, NIL)
        self.assertEqual(node_15.right.color, NIL)

    def test_right_left_rotation_no_sibling(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None, left=NIL_LEAF, right=NIL_LEAF)
        # LEFT PART
        nodem10 = Node(value=-10, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
        node_7 = Node(value=7, color=RED, parent=nodem10, left=NIL_LEAF, right=NIL_LEAF)
        nodem10.right = node_7

        # RIGHT PART
        node_20 = Node(value=20, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=RED, parent=node_20, left=NIL_LEAF, right=NIL_LEAF)
        node_20.left = node_15

        root.left = nodem10
        root.right = node_20

        rb_tree.root = root
        rb_tree.add(2)
        """
        2 goes as left to 7, but both are red so we do a RIGHT-LEFT rotation
        First a right rotation should happen, so that 2 becomes the parent of 7 [2 right-> 7]
        Second a left rotation should happen, so that 2 becomes the parent of -10 and 7
        2 is black, -10 and 7 are now red. 2's parent is the root - 10
        """
        node_2 = node_7.parent
        self.assertEqual(node_2.parent.value, 10)
        self.assertEqual(node_2.color, BLACK)
        self.assertEqual(node_2.left.value, -10)
        self.assertEqual(node_2.right.value, 7)

        self.assertEqual(node_7.color, RED)
        self.assertEqual(node_7.parent.value, 2)

        self.assertEqual(nodem10.color, RED)
        self.assertEqual(nodem10.parent.value, 2)

    def test_recolor_lr(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None)
        # RIGHT SUBTREE
        node_m10 = Node(value=-10, color=RED, parent=root, left=NIL_LEAF, right=NIL_LEAF)
        node_m20 = Node(value=-20, color=BLACK, parent=node_m10, left=NIL_LEAF, right=NIL_LEAF)
        node_m10.left = node_m20
        node_6 = Node(value=6, color=BLACK, parent=node_m10, left=NIL_LEAF, right=NIL_LEAF)
        node_m10.right = node_6
        node_1 = Node(value=1, color=RED, parent=node_6, left=NIL_LEAF, right=NIL_LEAF)
        node_6.left = node_1
        node_9 = Node(value=9, color=RED, parent=node_6, left=NIL_LEAF, right=NIL_LEAF)
        node_6.right = node_9

        # LEFT SUBTREE
        node_20 = Node(value=20, color=BLACK, parent=root, left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=RED, parent=node_20, left=NIL_LEAF, right=NIL_LEAF)
        node_20.left = node_15
        node_30 = Node(value=30, color=RED, parent=node_20, left=NIL_LEAF, right=NIL_LEAF)
        node_20.right = node_30

        root.left = node_m10
        root.right = node_20
        rb_tree.root = root
        rb_tree.add(4)
        """
        Adding 4, we recolor once, then we check upwards and see that there's a black sibling.
        We see that our direction is RightLeft (RL) and do a Left Rotation followed by a Right Rotation
        -10 becomes 6's left child and 1 becomes -10's right child
        After the left rotation,
        _____6_____ becomes the root
      -10R       10R  are his children
    -20B  1B   9B  20B
                 15R 30R
        """
        self.assertEqual(rb_tree.root.value, 6)
        self.assertEqual(rb_tree.root.parent, None)
        self.assertEqual(rb_tree.root.left.value, -10)
        self.assertEqual(rb_tree.root.right.value, 10)

        self.assertEqual(node_m10.parent.value, 6)
        self.assertEqual(node_m10.color, RED)
        self.assertEqual(node_m10.left.value, -20)
        self.assertEqual(node_m10.right.value, 1)

        node_10 = rb_tree.root.right
        self.assertEqual(node_10.color, RED)
        self.assertEqual(node_10.parent.value, 6)
        self.assertEqual(node_10.left.value, 9)
        self.assertEqual(node_10.right.value, 20)

        self.assertEqual(node_m20.color, BLACK)
        self.assertEqual(node_m20.parent.value, -10)
        self.assertEqual(node_m20.left.color, NIL)
        self.assertEqual(node_m20.right.color, NIL)

        self.assertEqual(node_1.color, BLACK)
        self.assertEqual(node_1.parent.value, -10)
        self.assertEqual(node_1.left.color, NIL)
        self.assertEqual(node_1.right.color, RED)
        node_4 = node_1.right
        self.assertEqual(node_4.value, 4)
        self.assertEqual(node_4.color, RED)

    def test_build_tree(self):
        rb_tree = RedBlackTree()
        rb_tree.add(2)
        self.assertEqual(rb_tree.root.value, 2)
        self.assertEqual(rb_tree.root.color, BLACK)
        node_2 = rb_tree.root
        """ 2 """
        rb_tree.add(1)
        """
            2B
           1R
        """
        node_1 = rb_tree.root.left
        self.assertEqual(node_1.value, 1)
        self.assertEqual(node_1.color, RED)

        rb_tree.add(4)
        """
            2B
          1R  4R
        """
        node_4 = rb_tree.root.right
        self.assertEqual(node_4.value, 4)
        self.assertEqual(node_4.color, RED)
        self.assertEqual(node_4.left.color, NIL)
        self.assertEqual(node_4.right.color, NIL)

        rb_tree.add(5)
        """
            2B                              2B
          1R  4R    ---CAUSES RECOLOR-->  1B  4B
               5R                              5R
        """
        node_5 = node_4.right
        self.assertEqual(node_5.value, 5)
        self.assertEqual(node_4.color, BLACK)
        self.assertEqual(node_1.color, BLACK)
        self.assertEqual(node_5.color, RED)

        rb_tree.add(9)
        """
            2B                                           __2B__
          1B  4B        ---CAUSES LEFT ROTATION-->     1B     5B
                5R                                          4R  9R
                 9R
        """
        node_9 = node_5.right
        self.assertEqual(node_9.value, 9)
        self.assertEqual(node_9.color, RED)
        self.assertEqual(node_9.left.color, NIL)
        self.assertEqual(node_9.right.color, NIL)

        self.assertEqual(node_4.color, RED)
        self.assertEqual(node_4.left.color, NIL)
        self.assertEqual(node_4.right.color, NIL)
        self.assertEqual(node_4.parent.value, 5)

        self.assertEqual(node_5.parent.value, 2)
        self.assertEqual(node_5.color, BLACK)
        self.assertEqual(node_5.left.value, 4)
        self.assertEqual(node_5.right.value, 9)

        rb_tree.add(3)
        """
            __2B__                                  __2B__
          1B      5B     ---CAUSES RECOLOR-->     1B      5R
                4R  9R                                  4B  9B
               3R                                      3R
        """
        node_3 = node_4.left
        self.assertEqual(node_3.value, 3)
        self.assertEqual(node_3.color, RED)
        self.assertEqual(node_3.left.color, NIL)
        self.assertEqual(node_3.right.color, NIL)
        self.assertEqual(node_3.parent.value, 4)

        self.assertEqual(node_4.color, BLACK)
        self.assertEqual(node_4.right.color, NIL)
        self.assertEqual(node_4.parent.value, 5)

        self.assertEqual(node_9.color, BLACK)
        self.assertEqual(node_9.parent.value, 5)

        self.assertEqual(node_5.color, RED)
        self.assertEqual(node_5.left.value, 4)
        self.assertEqual(node_5.right.value, 9)

        rb_tree.add(6)
        """
        Nothing special
           __2B__
         1B      5R___
               4B    _9B
              3R    6R
        """
        node_6 = node_9.left
        self.assertEqual(node_6.value, 6)
        self.assertEqual(node_6.color, RED)
        self.assertEqual(node_6.parent.value, 9)
        self.assertEqual(node_6.left.color, NIL)
        self.assertEqual(node_6.right.color, NIL)

        rb_tree.add(7)
        """
                   __2B__                                                    __2B__
                 1B      ___5R___             ---LEFT  ROTATION TO-->       1B   ___5R___
                       4B      _9B_                                             4B      9B
                     3R       6R                                               3R      7R
                               7R                                                     6B
            RIGHT ROTATION (RECOLOR) TO
                 __2B__
               1B    ___5R___
                    4B      7B
                   3R     6R  9R
        """
        node_7 = node_5.right
        self.assertEqual(node_7.value, 7)
        self.assertEqual(node_7.color, BLACK)
        self.assertEqual(node_7.left.value, 6)
        self.assertEqual(node_7.right.value, 9)
        self.assertEqual(node_7.parent.value, 5)

        self.assertEqual(node_5.color, RED)
        self.assertEqual(node_5.right.value, 7)

        self.assertEqual(node_6.color, RED)
        self.assertEqual(node_6.left.color, NIL)
        self.assertEqual(node_6.right.color, NIL)
        self.assertEqual(node_6.parent.value, 7)

        self.assertEqual(node_9.color, RED)
        self.assertEqual(node_9.left.color, NIL)
        self.assertEqual(node_9.right.color, NIL)
        self.assertEqual(node_9.parent.value, 7)

        rb_tree.add(15)
        """
                    __2B__                                         __2B__
               1B    ___5R___                                    1B    ___5R___
                    4B      7B       ---RECOLORS TO-->                4B       7R
                   3R     6R  9R                                     3R       6B 9B
                               15R                                                15R
                Red-red relationship on 5R-7R. 7R's sibling is BLACK, so we need to rotate.
                7 is the right child of 5, 5 is the right child of 2, so we have RR => L: Left rotation with recolor
                What we get is:

                            ___5B___
                        __2R__      7R
                      1B     4B    6B 9B
                            3R         15R
        """
        node_15 = node_9.right
        self.assertEqual(node_15.color, RED)
        self.assertEqual(node_15.parent.value, 9)
        self.assertEqual(node_15.left.color, NIL)
        self.assertEqual(node_15.right.color, NIL)

        self.assertEqual(node_9.color, BLACK)
        self.assertEqual(node_9.left.color, NIL)
        self.assertEqual(node_9.right.value, 15)
        self.assertEqual(node_9.parent.value, 7)

        self.assertEqual(node_6.color, BLACK)

        self.assertEqual(node_7.color, RED)
        self.assertEqual(node_7.left.value, 6)
        self.assertEqual(node_7.right.value, 9)

        self.assertEqual(rb_tree.root.value, 5)
        self.assertIsNone(node_5.parent)
        self.assertEqual(node_5.right.value, 7)
        self.assertEqual(node_5.left.value, 2)

        self.assertEqual(node_2.color, RED)
        self.assertEqual(node_2.parent.value, 5)
        self.assertEqual(node_2.left.value, 1)
        self.assertEqual(node_2.right.value, 4)

        self.assertEqual(node_4.parent.value, 2)
        self.assertEqual(node_4.color, BLACK)
        self.assertEqual(node_4.left.value, 3)
        self.assertEqual(node_4.right.color, NIL)


if __name__ == '__main__':
    unittest.main()