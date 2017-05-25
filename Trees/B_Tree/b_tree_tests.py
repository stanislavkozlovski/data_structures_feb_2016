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

