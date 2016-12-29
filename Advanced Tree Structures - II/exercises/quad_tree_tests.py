import unittest
import random

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

    def test_foreach_dfs_should_fuck_you(self):
        items = [BoundableObject(2, 2, 3, 3)] * 100
        for item in items:
            self.tree.add_object(item)

        def assert_function(_, __, depth):
            self.assertEqual(self.tree.max_depth, depth)

        self.tree.foreach_dfs(assert_function)

    def test_report_many_random_elements_should_return_all_colliders(self):
        object_count = 10000
        shepherd = BoundableObject(10, 20, 20, 30)
        items = []
        self.tree.add_object(shepherd)
        for _ in range(object_count):
            x = random.randint(0, self.tree.x2-11)
            x2 = x + 10
            y = random.randint(0, self.tree.y2-11)
            y2 = y + 10
            obj = BoundableObject(x, y, x2, y2)
            items.append(obj)
            self.tree.add_object(obj)

        expected_collisions = self.search_for_collisions_in_a_list(shepherd, items)
        result_collisions = self.search_for_collisions_in_a_tree(shepherd)

        self.assertEqual(len(expected_collisions), len(result_collisions))
        print(expected_collisions)
        self.assertCountEqual(expected_collisions, result_collisions)

    def search_for_collisions_in_a_tree(self, shepherd):
        result = []
        collision_candidates = self.tree.report(shepherd)
        for col_candidate in collision_candidates:
            if col_candidate.intersects(shepherd) and col_candidate != shepherd:
                result.append(col_candidate)

        return result

    def search_for_collisions_in_a_list(self, shepherd, objs):
        result = []

        for obj in objs:
            if shepherd.intersects(obj) and shepherd != obj:
                result.append(obj)

        return result

if __name__ == '__main__':
    unittest.main()