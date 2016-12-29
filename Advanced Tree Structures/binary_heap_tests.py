import unittest
from binary_heap import BinaryHeap


class BinaryHeapTests(unittest.TestCase):
    def build_heap_extract_all_elements_should_return_sorted_elements(self):
        nums = [3, 4, -1, 15, 2, 77, -3, 4, 12]
        heap = BinaryHeap(nums)
        result = []
        expected = [77, 15, 12, 4, 4, 3, 2, -1, -3]
        while len(heap) > 0:
            result.append(heap.extract_max())

        self.assertEqual(result, expected)

    def empty_heap_insert_extract_elements_should_return_sorted_elements(self):
        heap = BinaryHeap(nums)
        nums = [3, 4, -1, 15, 2, 77, -3, 4, 12]
        expected = [77, 15, 12, 4, 4, 3, 2, -1, -3]
        result = []
        for num in nums:
            heap.insert(num)
        while heap.count > 0:
            result.append(heap.extract_max())

        self.assertEqual(result, expected)
