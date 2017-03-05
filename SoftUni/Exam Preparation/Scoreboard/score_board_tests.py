import unittest
import sys
from StringIO import StringIO
from score_board import System
import re

from datetime import datetime


def log_actions(f):
    def _log(*args):
        start = datetime.now()
        expected_output, output, self = f(*args)
        end = datetime.now()
        print('TIME ELAPSED: {}'.format(end - start))
        self.validate_output(expected_output.getvalue(), output)

    return _log

class ScoreBoardTests(unittest.TestCase):
    def setUp(self):
        self.system = System()

    @log_actions
    def test_000001_input(self):
        output = self.execute_test('./Judge-Tests/test.000.001.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.000.001.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_001_input(self):
        output = self.execute_test('./Judge-Tests/test.001.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.001.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_002_input(self):
        output = self.execute_test('./Judge-Tests/test.002.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.002.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_003_input(self):
        output = self.execute_test('./Judge-Tests/test.003.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.003.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_004_input(self):
        output = self.execute_test('./Judge-Tests/test.004.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.004.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_005_input(self):
        output = self.execute_test('./Judge-Tests/test.005.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.005.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_006_input(self):
        output = self.execute_test('./Judge-Tests/test.006.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.006.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_007_input(self):
        output = self.execute_test('./Judge-Tests/test.007.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.007.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_008_input(self):
        output = self.execute_test('./Judge-Tests/test.008.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.008.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_009_input(self):
        output = self.execute_test('./Judge-Tests/test.009.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.009.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_010_input(self):
        output = self.execute_test('./Judge-Tests/test.010.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.010.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_011_input(self):
        output = self.execute_test('./Judge-Tests/test.011.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.011.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_012_input(self):
        output = self.execute_test('./Judge-Tests/test.012.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.012.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_013_input(self):
        output = self.execute_test('./Judge-Tests/test.013.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.013.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_014_input(self):
        output = self.execute_test('./Judge-Tests/test.014.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.014.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_015_input(self):
        output = self.execute_test('./Judge-Tests/test.015.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.015.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_016_input(self):
        output = self.execute_test('./Judge-Tests/test.016.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.016.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_017_input(self):
        output = self.execute_test('./Judge-Tests/test.017.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.017.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_018_input(self):
        output = self.execute_test('./Judge-Tests/test.018.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.018.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_019_input(self):
        output = self.execute_test('./Judge-Tests/test.019.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.019.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_020_input(self):
        output = self.execute_test('./Judge-Tests/test.020.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.020.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_021_input(self):
        output = self.execute_test('./Judge-Tests/test.021.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.021.out.txt', 'r').read())
        return expected_output, output, self

    @log_actions
    def test_022_input(self):
        output = self.execute_test('./Judge-Tests/test.022.in.txt')
        expected_output = StringIO(open('./Judge-Tests/test.022.out.txt', 'r').read())
        return expected_output, output, self

    def validate_output(self, expected, result):
        print('VALIDATING')
        expected_output = [unicode(part) for part in re.split(r'[\r\n]', expected) if part]
        result_output = [part for part in re.split(r'[\r\n]', result) if part]
        for idx, _ in enumerate(expected_output):
            self.assertEqual(expected_output[idx], result_output[idx])

    def execute_test(self, path):
            output = ''
            with open(path, 'r') as commands:
                for command in commands:
                    command = command.rstrip()
                    output_line = self.system.command_controller(command)
                    if output_line:
                        output += output_line + '\n'

            return output


if __name__ == '__main__':
    unittest.main()
