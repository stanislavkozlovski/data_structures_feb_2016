from homework.balanced_ordered_set.ordered_set import OrderedSet
import unittest


class OrderedSetTests(unittest.TestCase):
    def test_add_elements_on_initialization(self):
        sorted_elements = [-4313, 1, 2, 3, 13413, 4931939]
        # add the elements through the initialization of the set
        or_set = OrderedSet([2, 13413, 3, -4313, 4931939, 1])
        # assert they're equal
        for idx, el in enumerate(or_set):
            self.assertEqual(el, sorted_elements[idx])

    def test_addition_and_order(self):
        or_set = OrderedSet()
        sorted_elements = [-1, 0, 1,2,3,4]
        or_set.add(3)
        or_set.add(0)
        or_set.add(1)
        or_set.add(2)
        or_set.add(-1)
        or_set.add(4)
        for idx, el in enumerate(or_set):
            self.assertEqual(el, sorted_elements[idx])

    def test_remove_elements(self):
        sorted_elements = [1, 2, 3, 13413]
        # add the elements through the initialization of the set
        or_set = OrderedSet([2, 13413, 3, -4313, 4931939, 1])
        or_set.remove(-4313)
        or_set.remove(4931939)
        # assert they're equal
        for idx, el in enumerate(or_set):
            self.assertEqual(el, sorted_elements[idx])

    def test_convert_to_list(self):
        sorted_elements = [-301, 100, 200, 300, 301]
        or_set = OrderedSet([300, -301, 100, 301, 200])
        self.assertEqual(list(or_set), sorted_elements)

    def test_contains(self):
        elements = ['aa', 'a', 'ba']
        or_set = OrderedSet(elements)
        for el in elements:
            self.assertTrue(or_set.contains(el))

    def test_add_remove_100_elements_three_times(self):
        or_set = OrderedSet()
        for time in range(3):
            for i in range(100):
                or_set.add(i)

        # assert elements are from 1 to 100
        hundred_elements = list(range(100))
        for idx, el in enumerate(or_set):
            self.assertEqual(el, hundred_elements[idx])

        for time in range(3):
            for i in range(100):
                or_set.remove(i)

        self.assertCountEqual(list(or_set), [])

if __name__ == '__main__':
    unittest.main()