import unittest
from quad_tree import QuadTree, BoundableObject


class QuadTreeTests(unittest.TestCase):

    def setUp(self):
        self.tree = QuadTree(0, 0, 200, 200)

    def test_insert_should_increase_count(self):
        items = [BoundableObject(50, 50, 60, 60)] * 3
        for item in items:
            self.tree.add_object(item)

        self.assertEqual(len(self.tree), len(items))


if __name__ == '__main__':
    unittest.main()