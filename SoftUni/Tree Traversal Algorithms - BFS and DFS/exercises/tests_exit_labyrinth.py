import unittest
import sys
from io import StringIO
from nearest_exit_labyrinth import main as exit_labyrinth


class LabyrinthTest(unittest.TestCase):
    def test_labyrinth_9x7(self):
        user_input = """9
7
*********
*----**--
**-*----*
*--*-*-**
*s*--*-**
**------*
*******-*"""
        expected_output = "Shortest exit: URUURRDRRRUR\n"
        output = StringIO()
        try:
            sys.stdin = StringIO(user_input)
            sys.stdout = output
            exit_labyrinth()

            self.assertEqual(output.getvalue(), expected_output)
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

    def test_labyrinth_4x3(self):
        user_input = """4
3
****
*-s*
****"""
        expected_output = "No exit!\n"
        output = StringIO()
        try:
            sys.stdin = StringIO(user_input)
            sys.stdout = output
            exit_labyrinth()

            self.assertEqual(output.getvalue(), expected_output)
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

    def test_labyrinth_4x2(self):
        user_input = """4
2
****
***s"""
        expected_output = "Start is at the exit.\n"
        output = StringIO()
        try:
            sys.stdin = StringIO(user_input)
            sys.stdout = output
            exit_labyrinth()

            self.assertEqual(output.getvalue(), expected_output)
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

    def test_labyrinth_2x2(self):
        user_input = """2
2
**
**"""
        expected_output = "No exit!\n"
        output = StringIO()
        try:
            sys.stdin = StringIO(user_input)
            sys.stdout = output
            exit_labyrinth()

            self.assertEqual(output.getvalue(), expected_output)
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
