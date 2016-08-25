#!/usr/bin/env python3


# Code

def del_unpaired_brackets(string):
    pass

def del_unpaired_brackets_re(string):
    pass


# Tests.

import unittest

class TestDelUnpairedBrackets(unittest.TestCase):

    def setUp(self):
        self.strings = {
            'qlqksq((ewwe)(pll': 'qlqksq((ewwe)',
        }

    def test_del_unpaired_brackets(self):
        for input, result in self.strings.items():
            self.assertEqual(result, del_unpaired_brackets(input))

    def test_del_unpaired_brackets_re(self):
        for input, result in self.strings.items():
            self.assertEqual(result, del_unpaired_brackets_re(input))


if __name__ == '__main__':
    unittest.main()
