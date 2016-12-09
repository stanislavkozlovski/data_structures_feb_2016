import unittest
from unittest.mock import patch
from traverse_graph_find_connected_components import main as traverse_graph
import sys
from io import StringIO


class TraverseGraphTests(unittest.TestCase):
    def test_graph_connected_components_nine_nodes(self):
        user_input = """9
        3 6
        3 4 5 6
        8
        0 1 5
        1 6
        1 3
        0 1 4

        2"""
        expected_output = """Connected components: 6 4 5 1 3 0
Connected components: 8 2
Connected components: 7
"""
        output = StringIO()
        try:
            sys.stdin = StringIO(user_input)
            sys.stdout = output
            traverse_graph()
            self.assertEqual(output.getvalue(), expected_output)
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

    def test_graph_connected_components_1_node(self):
        user_input = """1
0"""
        expected_output = """Connected components: 0
"""
        output = StringIO()

        try:
            sys.stdin = StringIO(user_input)
            sys.stdout = output
            traverse_graph()
            self.assertEqual(output.getvalue(), expected_output)
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

    def test_graph_connected_components_0_nodes(self):
        user_input = """0
"""
        expected_output = ""
        output = StringIO()

        try:
            sys.stdin = StringIO(user_input)
            sys.stdout = output
            traverse_graph()
            self.assertEqual(output.getvalue(), expected_output)
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

    def test_graph_connected_components_7_nodes(self):
        user_input = """7

2 6
1
4
3

1
"""
        expected_output = """Connected components: 0
Connected components: 2 6 1
Connected components: 4 3
Connected components: 5
"""
        output = StringIO()

        try:
            sys.stdin = StringIO(user_input)
            sys.stdout = output
            traverse_graph()
            self.assertEqual(output.getvalue(), expected_output)
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

    def test_graph_connected_components_4_vertices(self):
        user_input = """4
1 2 3
0 1 2 3
0 1 3
1 2"""
        expected_output = """Connected components: 3 2 1 0
"""
        output = StringIO()

        try:
            sys.stdin = StringIO(user_input)
            sys.stdout = output
            traverse_graph()
            self.assertEqual(output.getvalue(), expected_output)
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
if __name__ == '__main__':
    unittest.main()