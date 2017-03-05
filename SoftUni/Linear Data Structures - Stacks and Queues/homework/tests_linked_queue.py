import unittest
from linked_queue import LinkedQueue


class LinkedQueueTests(unittest.TestCase):
    def test_enqueue_dequeue(self):
        lq = LinkedQueue()
        element = "No-Flex Zone"
        lq.enqueue(element)
        dequeued_el = lq.dequeue()
        self.assertEqual(dequeued_el, element)
        self.assertEqual(lq.count, 0)

    def test_dequeue_empty(self):
        lq = LinkedQueue()
        with self.assertRaises(Exception):
            lq.dequeue()

    def test_dequeue_order(self):
        lq = LinkedQueue()
        for num in range(5):
            lq.enqueue(num)
            self.assertEqual(lq.count, num+1)
        for num in range(5):
            self.assertEqual(lq.count, 5-num)
            dequeued_number = lq.dequeue()
            self.assertEqual(dequeued_number, num)

    def test_to_array(self):
        lq = LinkedQueue()
        array = [0,1,2,3,4]
        for num in array:
            lq.enqueue(num)

        self.assertEqual(list(lq), array)

    def test_empty_to_array(self):
        lq = LinkedQueue()
        self.assertEqual(list(lq), [])

if __name__ == "__main__":
    unittest.main()