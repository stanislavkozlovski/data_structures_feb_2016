import sys
import unittest
from io import StringIO

from tree_implementation import Tree

ORIGINAL_STDOUT = sys.stdout


class TreeTests(unittest.TestCase):
    def test_build_tree_for_loop_traversal(self):
        tree = Tree(7, [
            Tree(19,[
                Tree(1),
                Tree(12),
                Tree(31)
            ]),
            Tree(21),
            Tree(14,[
                Tree(23),
                Tree(6)
            ])
        ])
        nodes = []
        expected_nodes = [7, 19, 1, 12, 31, 21, 14, 23, 6]
        for node in tree:
            nodes.append(node)

        self.assertEqual(nodes, expected_nodes)

    def test_build_tree_print_tree(self):
        out = StringIO()
        sys.stdout = out
        tree = Tree(7, [
            Tree(19, [
                Tree(1),
                Tree(12),
                Tree(31)
            ]),
            Tree(21),
            Tree(14, [
                Tree(23),
                Tree(6)
            ])
        ])

        try:
            tree.print()
            output = out.getvalue().strip()
            expected_output = """7
  19
   1
   12
   31
  21
  14
   23
   6"""
            self.assertEqual(output, expected_output)

        finally:  # restore STDOUT
            sys.stdout = ORIGINAL_STDOUT

if __name__ == '__main__':
    unittest.main()