import unittest
from doubly_linked_list import DoublyLinkedList


class DoublyLinkedListTests(unittest.TestCase):
    def test_add_first_empty_list_should_add_element(self):
        dll = DoublyLinkedList()
        dll.add_first(5)

        self.assertEqual(dll.count, 1)
        self.assertEqual(list(dll), [5])

    def test_add_several_first_elements(self):
        dll = DoublyLinkedList()
        dll.add_first(10)
        dll.add_first(5)
        dll.add_first(3)

        self.assertEqual(dll.count, 3)
        self.assertEqual(list(dll), [3, 5, 10])

    def test_add_last_empty_list(self):
        dll = DoublyLinkedList()
        dll.add_last(5)

        self.assertEqual(dll.count, 1)
        self.assertEqual(list(dll), [5])

    def test_add_several_last_elements(self):
        dll = DoublyLinkedList()
        dll.add_last(5)
        dll.add_last(10)
        dll.add_last(15)

        self.assertEqual(dll.count, 3)
        self.assertEqual(list(dll), [5, 10, 15])

    def test_remove_first_on_one_element_list(self):
        """ Should make the list empty """
        dll = DoublyLinkedList()
        dll.add_last(5)
        element = dll.remove_first()
        self.assertEqual(element, 5)
        self.assertEqual(dll.count, 0)
        self.assertEqual(list(dll), [])

    def test_remove_first_empty_list(self):
        """ Should throw an exception """
        with self.assertRaises(Exception) as context:
            dll = DoublyLinkedList()
            el = dll.remove_first()

    def test_remove_first_several_elements(self):
        dll = DoublyLinkedList()
        dll.add_last(5)
        dll.add_last(6)
        dll.add_last(7)
        first_el = dll.remove_first()

        self.assertEqual(first_el, 5)
        self.assertEqual(dll.count, 2)
        self.assertEqual(list(dll), [6, 7])

    def test_remove_last_one_element(self):
        """ Should make the list empty """
        dll = DoublyLinkedList()
        dll.add_first(5)
        first_el = dll.remove_last()

        self.assertEqual(first_el, 5)
        self.assertEqual(dll.count, 0)
        self.assertEqual(list(dll), [])

    def test_remove_last_empty_list(self):
        """ Should raise an exception """
        with self.assertRaises(Exception) as context:
            dll = DoublyLinkedList()
            el = dll.remove_last()

    def test_remove_last_several_elements(self):
        dll = DoublyLinkedList()
        dll.add_first(10)
        dll.add_first(9)
        dll.add_first(8)

        last_el = dll.remove_last()

        self.assertEqual(last_el, 10)
        self.assertEqual(dll.count, 2)
        self.assertEqual(list(dll), [8, 9])

    def test_cast_to_list_empty_list(self):
        dll = DoublyLinkedList()
        self.assertEqual(list(dll), [])

    def test_cast_to_list_one_element(self):
        dll = DoublyLinkedList()
        dll.add_last(5)
        self.assertEqual(list(dll), [5])

    def test_cast_to_list_multiple_elements(self):
        dll = DoublyLinkedList()
        dll.add_last("Five")
        dll.add_last("Six")
        dll.add_last("Seven")

        self.assertEqual(list(dll), ["Five", "Six", "Seven"])

    def test_iterate_multiple_elements(self):
        dll = DoublyLinkedList()
        dll.add_last("Five")
        dll.add_last("Six")
        dll.add_last("Seven")

        items = []
        for item in dll:
            items.append(item)

        self.assertEqual(items, ["Five", "Six", "Seven"])

if __name__ == "__main__":
    unittest.main()