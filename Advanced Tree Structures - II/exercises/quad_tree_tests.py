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

    def test_report_empty_quadrant_should_return_empty(self):
        items = [
            BoundableObject(10, 0, 20, 10),
            BoundableObject(110, 0, 120, 10),
            BoundableObject(10, 110, 20, 120),
            BoundableObject(50, 0, 60, 10)
        ]
        for item in items:
            self.tree.add_object(item)
        # after 4 inserts our root splits into 4 and the third quadrant is empty
        first_quadrant = self.tree.get_subquandrant(1)
        elements = self.tree.report(first_quadrant)  # get everthing that intersects with our third quadrant
        self.assertEqual(len(elements), 0)

    def test_report_from_non_empty_quadrants_should_return_elements(self):
        expected_quadrant_items = [
            [BoundableObject(110, 101, 120, 110)],  # first quadrant
            [BoundableObject(10, 110, 20, 120)],  # second quadrant
            [BoundableObject(10, 0, 20, 10), BoundableObject(50, 0, 60, 10)],  # third quadrant
            [] # fourth quadrant
        ]
        # add the objects to the tree
        for obj in [obj for quadrant in expected_quadrant_items for obj in quadrant]:
            self.tree.add_object(obj)

        first_quadrant = self.tree.get_subquandrant(1)
        f_q_elements = self.tree.report(first_quadrant)
        self.assertEqual(f_q_elements, expected_quadrant_items[0])

        second_quadrant = self.tree.get_subquandrant(2)
        s_q_elements = self.tree.report(second_quadrant)
        self.assertEqual(s_q_elements, expected_quadrant_items[1])

        third_quadrant = self.tree.get_subquandrant(3)
        t_q_elements = self.tree.report(third_quadrant)
        self.assertEqual(t_q_elements, expected_quadrant_items[2])

        fourth_quadrant = self.tree.get_subquandrant(4)
        fourth_q_elements = self.tree.report(fourth_quadrant)
        self.assertEqual(fourth_q_elements, expected_quadrant_items[3])

if __name__ == '__main__':
    unittest.main()