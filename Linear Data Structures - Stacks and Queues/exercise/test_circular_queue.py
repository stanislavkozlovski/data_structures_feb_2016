import unittest
from circular_queue import CircularQueue


class CircularQueueTests(unittest.TestCase):
    def test_enqueue_empty_queue(self):
        """ Should add element """
        queue = CircularQueue()
        queue.enqueue(5)
        self.assertEqual(queue.count, 1)
        self.assertEqual(list(queue), [5])

    def test_enqueue_dequeue(self):
        """ Should empty queue """
        queue = CircularQueue()
        test_element = "Some value"
        queue.enqueue(test_element)
        el_from_queue = queue.dequeue()

        self.assertEqual(el_from_queue, test_element)
        self.assertEqual(queue.count, 0)

    def test_dequeue_empty_queue(self):
        """ Should throw exception """
        queue = CircularQueue()

        with self.assertRaises(Exception):
            queue.dequeue()

    def test_enqueue_dequeue_100_elements(self):
        """ Should return an empty queue """
        queue = CircularQueue()
        element_to_add = "ELEMENT"
        elements_count = 100

        # add to queue
        for _ in range(elements_count):
            queue.enqueue(element_to_add)

        # assert
        self.assertEqual(list(queue), [element_to_add] * elements_count)
        for idx in range(elements_count):
            self.assertEqual(queue.count, elements_count - idx)
            dequeued_element = queue.dequeue()
            self.assertEqual(element_to_add, dequeued_element)
            self.assertEqual(queue.count, elements_count - idx - 1)

        self.assertEqual(queue.count, 0)

    def test_enqueue_dequeue_many_chunks(self):
        """ CHUNKS_COUNT add chunks of size CHUNK_SIZE
            and check along each enqueue/dequeue call """
        queue = CircularQueue()
        chunks_count = 100

        elements_count = 1
        for i in range(chunks_count):
            self.assertEqual(queue.count, 0)
            chunk_size = i + 1

            # enqueue
            for counter in range(chunk_size):
                self.assertEqual(queue.count, elements_count-1)
                queue.enqueue("SMTH")
                self.assertEqual(queue.count, elements_count)
                elements_count += 1
            # dequeue
            for counter in range(chunk_size):
                elements_count -= 1
                self.assertEqual(queue.count, elements_count)
                queue.dequeue()
                self.assertEqual(queue.count, elements_count-1)

            self.assertEqual(queue.count, 0)

    def test_enqueue_500_elements_to_list(self):
        expected = list(range(500))
        queue = CircularQueue()
        # add the items
        for element in expected:
            queue.enqueue(element)

        self.assertEqual(list(queue), expected)

    def test_initial_capacity_1_enq_deq_20_elements(self):
        """ Set an initial capacity of 1 and add/remove 20 elements,
            checking along the way if everything works correctly.
            The list should resize itself when appropriate"""
        elements_count = 20
        initial_capacity = 1
        queue = CircularQueue(initial_capacity)
        for num in range(elements_count):
            queue.enqueue(num)

        self.assertEqual(queue.count, elements_count)
        for num in range(elements_count):
            dequeued_num = queue.dequeue()
            self.assertEqual(dequeued_num, num)

        self.assertEqual(queue.count, 0)

    def test_circular_motion(self):
        """ Add and dequeue elements in such a way that
            they will form a circular queue"""
        queue = CircularQueue(capacity=5)
        for num in range(5):
            queue.enqueue(num)
        for _ in range(3):
            queue.dequeue()
        """ Queue should now have two empty values at the start """
        queue.enqueue("CIRCLE HAS BEEN FORMED")
        self.assertEqual(queue.count, 3)
        self.assertEqual(list(queue), [3, 4, "CIRCLE HAS BEEN FORMED"])

if __name__ == '__main__':
    unittest.main()