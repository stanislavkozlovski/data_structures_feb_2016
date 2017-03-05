import sys
import unittest
from io import StringIO

ORIGINAL_STDOUT = sys.stdout
from binary_tree_implementation import BinaryTree

class BinaryTreeTest(unittest.TestCase):
    def binary_in_order_traversal(self):
        tree = BinaryTree("*",
                          left=BinaryTree("+",
                                          left=BinaryTree("3",iterable_strategy="inorder"),
                                          right=BinaryTree("2",iterable_strategy="inorder"),
                                          iterable_strategy="inorder"),
                          right=BinaryTree("-",
                                           left=BinaryTree("9", iterable_strategy="inorder"),
                                           right=BinaryTree("6", iterable_strategy="inorder"),
                                           iterable_strategy="inorder"),
                          iterable_strategy="inorder")
        nodes = [node for node in tree]
        expected_nodes = ["3", "+", "2", "*", "9", "-", "6"]
        self.assertEqual(expected_nodes, nodes)

    def binary_post_order_traversal(self):
        tree = BinaryTree("*",
                          left=BinaryTree("+",
                                          left=BinaryTree("3", iterable_strategy="postorder"),
                                          right=BinaryTree("2", iterable_strategy="postorder"),
                                          iterable_strategy="postorder"),
                          right=BinaryTree("-",
                                           left=BinaryTree("9", iterable_strategy="postorder"),
                                           right=BinaryTree("6", iterable_strategy="postorder"),
                                           iterable_strategy="postorder"),
                          iterable_strategy="postorder")
        nodes = [node for node in tree]
        expected_nodes = ["3", "2", "+", "9", "6", "-", "*"]
        self.assertEqual(expected_nodes, nodes)

    def print_indented_pre_order(self):
        output = StringIO()
        sys.stdout = output
        tree = BinaryTree("*",
                          left=BinaryTree("+",
                                          left=BinaryTree("3", iterable_strategy="postorder"),
                                          right=BinaryTree("2", iterable_strategy="postorder"),
                                          iterable_strategy="postorder"),
                          right=BinaryTree("-",
                                           left=BinaryTree("9", iterable_strategy="postorder"),
                                           right=BinaryTree("6", iterable_strategy="postorder"),
                                           iterable_strategy="postorder"),
                          iterable_strategy="postorder")

        try:
            tree.print()
            result = output.getvalue()
            expected_output = """*
 +
  3
  2
 -
  9
  6"""
            self.assertEqual(result, expected_output)
        finally:
            sys.stdout = ORIGINAL_STDOUT

if __name__ == '__main__':
    unittest.main()
