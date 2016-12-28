import unittest
import random
from avl_tree import AvlTree

class AvlInsertTests(unittest.TestCase):
    def test_add_several_elements_should_increase_count(self):
        avl_tree = AvlTree()
        nums = [1, 2, 3]
        for num in nums:
            avl_tree.add(num)
        self.assertEqual(len(avl_tree), len(nums))

    def test_add_repeating_elements_should_not_add_duplicates(self):
        avl_tree = AvlTree()
        nums = [3, 3, 3, 3]
        for num in nums:
            avl_tree.add(num)
        self.assertEqual(len(avl_tree), len(set(nums)))

    def test_add_multiple_items_random_order_should_be_sorted(self):
        avl_tree = AvlTree()
        nums = [-50, 12, -1300, 3, 83491, 1, 0, 31]
        for num in nums:
            avl_tree.add(num)
        self.assertEqual(list(avl_tree), list(sorted(nums)))
        self.assertEqual(len(avl_tree), len(nums))

    def test_add_many_random_elements_should_return_sorted_ascending(self):
        num_count = 1000
        avl_tree = AvlTree()
        expected_items = set()
        for _ in range(num_count):
            rand_num = random.randint(0, num_count)
            avl_tree.add(rand_num)
            expected_items.add(rand_num)

        expected_items = list(sorted(expected_items))
        self.assertEqual(list(avl_tree), expected_items)
        self.assertEqual(len(avl_tree), len(expected_items))

    def test_add_multiple_items_in_balanced_way_should_be_sorted(self):
        nums = [20, 10, 30, 0, 15, 25, 40]
        avl_tree = AvlTree()
        for num in nums:
            avl_tree.add(num)

        expected_items = list(sorted(nums))
        self.assertEqual(list(avl_tree), expected_items)
        self.assertEqual(len(avl_tree), len(expected_items))

    def test_contains_added_element_should_return_true(self):
        nums = [-2, 3, 10, 0, 6, 1, 16]
        avl_tree = AvlTree()
        for num in nums:
            avl_tree.add(num)

        contains_three = 3 in avl_tree
        self.assertTrue(contains_three)

    def contains_non_added_element_should_return_false(self):
        nums = [1, 7, 3, -4, 10, 0]
        avl_tree = AvlTree()
        for num in nums:
            avl_tree.add(num)

        contains_two = 2 in avl_tree
        self.assertFalse(contains_two)

if __name__ == '__main__':
    unittest.main()