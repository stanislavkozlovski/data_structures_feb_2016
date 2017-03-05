"""
Write unit tests to ensure your array-based stack implementation works correctly. Test the following scenarios:
Push / pop element: create a stack of numbers; assert Count == 0; push element; assert Count == 1; pop element; assert the element is the same like the pushed element; assert Count == 0.
Push / pop 1000 elements: create a stack of strings; assert Count == 0;
    repeat 1000 times: { push element; assert the Count is correct; };
    repeat 1000 times: { pop an element; assert the element is correct; assert the Count is correct }.
    Pushing 1000 elements will indirectly test the auto-grow functionality several times.
Pop from empty stack: create a stack; pop an element; expect an exception;
Push / pop with initial capacity 1: create a stack of numbers with initial capacity of 1; assert Count == 0; push element; assert Count == 1; push another element; assert Count == 2; pop element; assert the element is correct; assert Count == 1; pop element; assert the element is correct; assert Count == 0.
ToArray(): create a stack of numbers; push a few numbers, e.g. { 3, 5, -2, 7 }; convert the stack to array; assert the results holds the pushed numbers in reversed order, e.g. { 7, -2, 5, 3 }.
Empty stack ToArray(): create a stack of dates; convert the stack to array; expect empty array.
Use as reference the unit tests for the circular queue from the exercises.
"""
import unittest
from linked_stack import LinkedStack


class LinkedStackTests(unittest.TestCase):
    def test_push_pop_elements(self):
        stack = LinkedStack()
        self.assertEqual(stack.count, 0)
        stack.push("WORST")
        el_from_stack = stack.pop()
        self.assertEqual(el_from_stack, "WORST")
        self.assertEqual(stack.count, 0)

    def test_push_pop_thousand_elements(self):
        stack = LinkedStack()
        for idx in range(1000):
            stack.push("WORST BEHAVIOR")
            self.assertEqual(stack.count, idx + 1)
        for idx in range(1000):
            self.assertEqual(stack.count, 1000-idx)
            self.assertEqual(stack.pop(), "WORST BEHAVIOR")
        self.assertEqual(stack.count, 0)

    def test_pop_empty_stack(self):
        stack = LinkedStack()
        with self.assertRaises(Exception):
            stack.pop()


    def test_to_array(self):
        stack = LinkedStack()
        stack.push(3)
        stack.push(5)
        stack.push(-2)
        stack.push(7)
        self.assertEqual(list(stack), [7, -2, 5, 3])

    def test_empty_to_array(self):
        self.assertEqual(list(LinkedStack()), [])


if __name__ == '__main__':
    unittest.main()