from homework.ordered_set import OrderedSet
import unittest


class OrderedSetTests(unittest.TestCase):
    def setUp(self):
        self.ordered_set = OrderedSet()

    def test_order(self):
        self.ordered_set.add(1)
        self.ordered_set.add(13)
        self.ordered_set.add(43)
        self.ordered_set.add(100)
        self.ordered_set.add(19)
        self.ordered_set.add(5)

        expected_output = [1, 5, 13, 19, 43, 100]
        self.assertEqual(list(self.ordered_set), expected_output)

    def test_contains(self):
        self.ordered_set.add(1)
        self.ordered_set.add(13)
        self.ordered_set.add(43)
        self.ordered_set.add(100)
        self.ordered_set.add(19)
        self.ordered_set.add(5)
        self.ordered_set.add(531)
        self.ordered_set.add(50)

        self.assertTrue(self.ordered_set.contains(531))

    def test_contains_invalid_element_should_return_false(self):
        self.ordered_set.add(1)
        self.ordered_set.add(13)
        self.ordered_set.add(43)
        self.ordered_set.add(100)
        self.ordered_set.add(19)
        self.ordered_set.add(5)
        self.ordered_set.add(531)
        self.ordered_set.add(50)

        self.assertFalse(self.ordered_set.contains(1023))

    def test_remove_root_element_should_remove(self):
        self.ordered_set.add(1)
        self.ordered_set.add(13)
        self.ordered_set.add(43)
        self.ordered_set.add(100)
        self.ordered_set.add(19)
        self.ordered_set.add(5)
        self.ordered_set.remove(1)
        expected_output = [5, 13, 19, 43, 100]
        self.assertEqual(list(self.ordered_set), expected_output)

    def test_remove_biggest_element_should_remove(self):
        self.ordered_set.add(1)
        self.ordered_set.add(13)
        self.ordered_set.add(43)
        self.ordered_set.add(100)
        self.ordered_set.add(19)
        self.ordered_set.add(5)
        self.ordered_set.remove(100)
        expected_output = [1, 5, 13, 19, 43]
        self.assertEqual(list(self.ordered_set), expected_output)

    def test_remove_smallest_left_element_should_remove(self):
        self.ordered_set.add(1)
        self.ordered_set.add(13)
        self.ordered_set.add(43)
        self.ordered_set.add(100)
        self.ordered_set.add(0)
        self.ordered_set.add(19)
        self.ordered_set.add(5)
        self.ordered_set.remove(0)
        expected_output = [1, 5, 13, 19, 43, 100]
        self.assertEqual(list(self.ordered_set), expected_output)

    def test_remove_invalid_element_should_raise_exception(self):
        self.ordered_set.add(43)
        self.ordered_set.add(100)
        self.ordered_set.add(0)
        self.ordered_set.add(19)
        self.ordered_set.add(5)
        with self.assertRaises(Exception):
            self.ordered_set.remove(524)

    def test_add_remove_count_should_be_correct(self):
        for i in range(100):
            self.ordered_set.add(i)
            self.assertEqual(self.ordered_set.count, i+1)

        # should not add anything because all are duplicates
        for i in range(100):
            self.ordered_set.add(i)
            self.assertEqual(self.ordered_set.count, 100)

        for i in range(100):
            self.ordered_set.remove(i)
            self.assertEqual(self.ordered_set.count, (100-i)-1)

if __name__ == '__main__':
    unittest.main()