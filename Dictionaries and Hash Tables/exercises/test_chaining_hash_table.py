import unittest
import maya
from exercises.chaining_hash_table import HashTable, KeyValue


class ChainingHashTableTests(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def test_key_value_pair(self):
        key_val = KeyValue('Man', 23)
        self.assertEqual(key_val.key, 'Man')
        self.assertEqual(key_val.value, 23)

    def test_add_empty_hash_table_no_duplicates_should_add_elements(self):
        elements = [
            KeyValue("Peter", 5),
            KeyValue("Maria", 6),
            KeyValue("George", 4),
            KeyValue("Kiril", 5)
        ]

        for element in elements:
            self.hash_table.add(element.key, element.value)

        actual_elements = list(self.hash_table)
        self.assertCountEqual(actual_elements, elements)

    def test_add_empty_hash_table_duplicates_should_throw_error(self):
        self.hash_table.add('Peter', 5)
        with self.assertRaises(Exception):
            self.hash_table.add('Peter', 10)

    def test_add_1000_elements_should_work(self):
        expected_elements = []
        for i in range(1000):
            self.hash_table.add("key " + str(i), i)
            expected_elements.append(KeyValue("key " + str(i), i))
        actual_elements = list(self.hash_table)
        self.assertCountEqual(actual_elements, expected_elements)

    def test_add_or_replace_with_duplicates_should_work(self):

        self.hash_table.add_or_replace("Peter", 555)
        self.hash_table.add_or_replace("Maria", 999)
        self.hash_table.add_or_replace("Maria", 123)
        self.hash_table.add_or_replace("Maria", 6)
        self.hash_table.add_or_replace("Peter", 5)

        expected_elements = [
            KeyValue("Maria", 6),
            KeyValue("Peter", 5)
        ]
        actual_elements = list(self.hash_table)
        self.assertCountEqual(actual_elements,)

    def test_count_add_remove_should_work(self):

        self.assertEqual(0, len(self.hash_table))

        self.hash_table.add("Peter", 555)
        self.hash_table.add_or_replace("Peter", 555)
        self.hash_table.add_or_replace('Ivan', 555)
        self.assertEqual(2, len(self.hash_table))

        self.hash_table.remove("Peter")
        self.assertEqual(1, len(self.hash_table))

        self.hash_table.remove("Peter")
        self.assertEqual(1, len(self.hash_table))

        self.hash_table.remove("Ivan")
        self.assertEqual(0, len(self.hash_table))

    def test_indexer_get_existing_element_should_return_value(self):
        self.hash_table.add(555, "Peter")
        actual_value = self.hash_table[555]

        self.assertCountEqual("Peter", actual_value)

    def test_get_non_existing_element_should_raise_exception(self):
        with self.assertRaises(KeyError):
            self.hash_table[12345]

    def test_indexer_add_replace_with_duplicates_should_work(self):

        self.hash_table["Peter"] = 555
        self.hash_table["Maria"] = 999
        self.hash_table["Maria"] = 123
        self.hash_table["Maria"] = 6
        self.hash_table["Peter"] = 5

        expected_elements = [
            KeyValue("Maria", 6),
            KeyValue("Peter", 5)
        ]
        actual_elements = list(self.hash_table)

        self.assertCountEqual(actual_elements, expected_elements)

    def test_try_get_existing_element_should_work(self):
        self.hash_table.add(555, "Peter")
        value, result = self.hash_table.try_get_value(555)
        self.assertEqual("Peter", value)
        self.assertTrue(result)

    def test_try_get_nonexisting_element_should_return_false(self):
        value, result = self.hash_table.try_get_value(555)
        self.assertFalse(result)

    def test_find_existing_element_should_return_the_element(self):
        name = "Maria"
        dt = maya.now()
        self.hash_table.add(name, dt)

        element = self.hash_table.find(name)
        expected_element = KeyValue(name, dt)
        self.assertEqual(element, expected_element)

    def test_find_non_existing_element_should_return_none(self):
        element = self.hash_table.find("Maria")
        self.assertIsNone(element)

    def test_contains_key_existing_element_should_return_true(self):
        dt = maya.now()
        self.hash_table.add(dt, 555)

        contains_key = self.hash_table.has_key(dt)
        self.assertTrue(contains_key)

    def test_contains_non_existing_element_should_return_false(self):
        contains_key = self.hash_table.has_key('Nothing')
        self.assertFalse(contains_key)

    def test_remove_existing_element_should_work(self):
        self.hash_table.add("peter", 12.5)
        self.hash_table.add("maria", 5)

        self.assertEqual(len(self.hash_table), 2)
        removed = self.hash_table.remove("peter")

        self.assertTrue(removed)
        self.assertEqual(len(self.hash_table), 1)

    def test_remove_non_existing_element_should_work(self):
        self.hash_table.add("peter", 12.5)
        self.hash_table.add("maria", 5)

        self.assertEqual(len(self.hash_table), 2)
        removed = self.hash_table.remove("George")

        self.assertFalse(removed)
        self.assertEqual(len(self.hash_table), 2)

    def test_remove_5000_elements_should_work(self):
        keys = []
        count = 5000
        for i in range(count):
            keys.append(i)
            self.hash_table.add(i, i)

        self.assertEqual(len(self.hash_table), count)

        for key in keys:
            self.hash_table.remove(key)
            count -= 1
            self.assertEqual(len(self.hash_table), count)

        expected_elements = []
        self.assertCountEqual(list(self.hash_table), expected_elements)

    def test_clear_should_work_correctly(self):
        self.assertEqual(len(self.hash_table), 0)
        self.hash_table.clear()
        self.assertEqual(len(self.hash_table), 0)

        self.hash_table.add("Peter", 5)
        self.hash_table.add("Maria", 7)
        self.hash_table.add("George", 3)
        # clear the elements and assert
        self.assertEqual(len(self.hash_table), 3)
        self.hash_table.clear()
        self.assertEqual(len(self.hash_table), 0)
        self.assertCountEqual(list(self.hash_table), [])

        self.hash_table.add("Peter", 5)
        self.hash_table.add("Maria", 7)
        self.hash_table.add("George", 3)

        self.assertEqual(len(self.hash_table), 3)

    def test_keys_should_work_correctly(self):
        self.assertEqual([], self.hash_table.keys())

        self.hash_table.add("Peter", 5)
        self.hash_table.add("Maria", 3)
        self.hash_table["George"] = 231.2

        keys = self.hash_table.keys()

        expected_keys = ["Peter", "Maria", "George"]
        self.assertCountEqual(keys, expected_keys)

    def test_values_should_work_correctly(self):
        self.assertEqual([], self.hash_table.values())

        self.hash_table.add("Peter", 5)
        self.hash_table.add("Maria", 3)
        self.hash_table["George"] = 231.2

        values = self.hash_table.values()

        expected_values = [5, 3, 231.2]

        self.assertCountEqual(values, expected_values)

if __name__ == '__main__':
    unittest.main()