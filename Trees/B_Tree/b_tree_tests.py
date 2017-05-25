from unittest import TestCase

from b_tree import BNode


class BNodeTests(TestCase):

    def assertElementsInExpectedOrder(self, expected_elements, received_elements):
        self.assertEqual(len(expected_elements), len(received_elements))
        for i in range(len(expected_elements)):
            self.assertEqual(expected_elements[i], received_elements[i])

    def test_addition_sorts(self):
        """
            Given a BTree of order 6, lets add some nodes

            10, 3, 15, 50
            should produce the following root

            3, 10, 15, 50
        """
        root = BNode(order=6)
        root.add(50); root.add(10); root.add(3); root.add(15)
        self.assertElementsInExpectedOrder([3, 10, 15, 50], root.values)

    def test_addition_splits(self):
        """
        Given a BTree of order 6, with the following elements
        10, 3, 15, 27
        """
        root = BNode(order=6)
        root.add(50); root.add(10); root.add(3); root.add(15)
        """
        Add 27 to it
        BTree should now become the following

        3|10|15|27|50 - is full

               15
             /    \
          3|10    27|50
        """
        root.add(27)

        self.assertElementsInExpectedOrder(root.values, [15])
        left_node = root.children[0]
        right_node = root.children[1]

        self.assertElementsInExpectedOrder(left_node.values, [3, 10])
        self.assertEqual(left_node.parent, root)
        self.assertElementsInExpectedOrder(right_node.values, [27, 50])
        self.assertEqual(right_node.parent, root)

    def test_addition_in_middle(self):
        """
               20|30
             /   |   \
          1     25    45
             Add 27

               20|30
             /   |   \
            1  25|27  45
        """
        root = BNode()
        root.values = [20, 30]
        left = BNode()
        left.values = [1]
        mid = BNode()
        mid.values = [25]
        right = BNode()
        right.values = [45]
        root.children = [left, mid, right]

        root.add(27)

        self.assertElementsInExpectedOrder([25, 27], mid.values)

    def test_merge_node(self):
        """
        Given two nodes

        100   |   200  | 300   (A)
       /      |        |      \
    15|20   102  (B)250|270    405
                  /    |    \
               202    260   290|299
        Merge A and B
        """
        A = BNode(order=7)
        B = BNode(order=7, parent=A)
        b_left = BNode(order=7, parent=B); b_left.values = [202]
        b_mid = BNode(order=7, parent=B); b_mid.values = [260]
        b_right = BNode(order=7, parent=B); b_right.values = [290, 299]
        B.values=[250, 270]
        B.children = [b_left, b_mid, b_right]
        a_rightest = BNode(order=7, parent=A); a_rightest.values = [405]
        a_leftest = BNode(order=7, parent=A); a_leftest.values = [15, 20]
        a_midleft = BNode(order=7, parent=A); a_midleft.values = [102]
        A.children = [a_leftest, a_midleft, B, a_rightest]
        A.values = [100, 200, 300]
        # Assert we've built it ok
        self.assertElementsInExpectedOrder(A.children[0].values, [15, 20])
        self.assertElementsInExpectedOrder(A.children[1].values, [102])
        self.assertElementsInExpectedOrder(A.children[2].values, [250, 270])
        self.assertElementsInExpectedOrder(A.children[3].values, [405])

        """
        Merging A and B should produce the following

        100    |    200    |    250    |    270    |    300   (A)
      /        |           |           |           |       \
    15|20     102         202         260       290|300    405
    (B)       (C)         (D)         (E)         (F)       (G)


        """
        A.merge_with_child(B)
        self.assertElementsInExpectedOrder([100, 200, 250, 270, 300], A.values)
        self.assertIsNone(A.parent)

        B = A.children[0]
        self.assertElementsInExpectedOrder([15, 20], B.values)
        self.assertEqual(B.parent, A)

        C = A.children[1]
        self.assertElementsInExpectedOrder([102], C.values)
        self.assertEqual(C.parent, A)

        D = A.children[2]
        self.assertElementsInExpectedOrder([202], D.values)
        self.assertEqual(D.parent, A)

        E = A.children[3]
        self.assertElementsInExpectedOrder([260], E.values)
        self.assertEqual(E.parent, A)

        F = A.children[4]
        self.assertElementsInExpectedOrder([290, 299], F.values)
        self.assertEqual(F.parent, A)

        G = A.children[5]
        self.assertElementsInExpectedOrder([405], G.values)
        self.assertEqual(G.parent, A)

    def test_addition_splits_into_parent(self):
        root = BNode(order=6)
        root.add(50); root.add(10); root.add(3); root.add(15); root.add(27); root.add(60); root.add(70)
        """
               15 (A)
             /    \
     (B)  3|10    27|50|60|70| (C)
        """
        # assert we have what we expect
        A = root
        B = root.children[0]
        C = root.children[1]
        self.assertElementsInExpectedOrder([27, 50, 60, 70], C.values)
        """
        Add 80, our C node gets full, as such splits and goes to the top
               15 (A)
             /    \
     (B)  3|10    27|50|60|70|80| (C)
        This is what should happen
            15 | 60 (A)
          /    |        \
     (B)3|10 (C)27|50   (D)70|80
        """
        A.add(80)
        C = A.children[1]
        D = A.children[2]

        self.assertElementsInExpectedOrder([27, 50], C.values)
        self.assertEqual(A, C.parent)
        self.assertFalse(C._BNode__has_children())
        self.assertElementsInExpectedOrder([70, 80], D.values)
        self.assertEqual(A, D.parent)
        self.assertFalse(D._BNode__has_children())
