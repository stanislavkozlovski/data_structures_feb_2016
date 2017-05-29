import unittest
from R_Tree import *


class RTreeTests(unittest.TestCase):
    def test_rectangle_contains(self):
        rect_1 = Rectangle(10, 10, 40, -10)
        rect_2 = Rectangle(10, 10, 20, 0)
        self.assertTrue(rect_1.contains(rect_2))

    def test_rectangle_contains_2(self):
        rect_1 = Rectangle(10, 10, 40, -10)
        rect_2 = Rectangle(30, -2, 38, -11)
        self.assertFalse(rect_1.contains(rect_2))
        self.assertFalse(rect_2.contains(rect_1))

    def test_r_tree_addition(self):
        """
        Given this rectangle
 10,10  ____________________
        |                  |
        |                  |
        |                  |
        |                  |
        |                  |
        |                  |
        |                  |
        ____________________ 40,-10
        Add 3 objects that will fit in it
        """
        tree = RTree(10, 10, 40, -10, max_order=6)
        gas_station = RObject(10, 10, 20, 0, "Shell")
        restaurant = RObject(30, -2, 38, -10, "Happy")
        church = RObject(28, 5, 38, 0, "Some Church")
        tree.add(gas_station)
        tree.add(restaurant)
        tree.add(church)

        self.assertEqual(len(tree.root.children), 3)
        self.assertIn(gas_station, tree.root.children)
        self.assertIn(church, tree.root.children)
        self.assertIn(restaurant, tree.root.children)

    def test_r_tree_split(self):
        """
            Given this rectangle
     10,10  ____________________
            |                  |
            |                  |
            |                  |
            |                  |
            |                  |
            |                  |
            |                  |
            ____________________ 40,-10
            Add 6 objects that overflow the maximum children count
            It should split into 2 RNodes which will hold the objects
    10,10  ____________________
            |  ____            |
            |  | R |           |
            |  |Nod|           | Only for display purposes
            |  _____           |
            |    _________     |
            |    | RNod2 |     |
            |    _________     |
            ____________________ 40,-10
        """
        tree = RTree(10, 10, 40, -10, max_order=6)
        gas_station = RObject(10, 10, 20, 0, "Shell")
        restaurant = RObject(30, -2, 38, -10, "Happy")
        church = RObject(28, 5, 38, 0, "Some Church")
        university = RObject(10, 0, 15, -5, "Software University")
        shop = RObject(16, -3, 25, -5, "Lidl")
        coffee_bar = RObject(34, 10, 36, 6, "Starbucks")
        all_objects = [gas_station, restaurant, church, university, shop, coffee_bar]

        tree.add(gas_station)
        tree.add(restaurant)
        tree.add(church)
        tree.add(university)
        tree.add(shop)
        tree.add(coffee_bar)
        # Should split them into two RNodes which both contain 3 points
        self.assertEqual(len(tree.root.children), 2)
        self.assertTrue(all(isinstance(ch, RNode) for ch in tree.root.children))
        first_node = tree.root.children[0]
        sec_node = tree.root.children[1]
        for f_ch in first_node.children:
            self.assertTrue(first_node.contains(f_ch))
            all_objects.remove(f_ch)

        for s_ch in sec_node.children:
            self.assertTrue(sec_node.contains(s_ch))
            all_objects.remove(s_ch)

        self.assertEqual(len(all_objects), 0)  # should have went through each object exactly once
        print(first_node.x1, first_node.y1, first_node.x2, first_node.y2)
        print(sec_node.x1, sec_node.y1, sec_node.x2, sec_node.y2)
