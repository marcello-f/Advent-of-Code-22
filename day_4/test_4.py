import unittest
from day_4 import parser, check_full, check_part

input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
input = input.splitlines()

class Test4(unittest.TestCase):

    def test_parser(self):
        self.assertEqual(parser(input[0]), [2,4,6,8])
        self.assertEqual(parser(input[1]), [2,3,4,5])
        self.assertEqual(parser(input[2]), [5,7,7,9])
        self.assertEqual(parser(input[3]), [2,8,3,7])
        self.assertEqual(parser(input[4]), [6,6,4,6])
        self.assertEqual(parser(input[5]), [2,6,4,8])

    def test_check_full(self):
        self.assertEqual(check_full(input[0]), False)
        self.assertEqual(check_full(input[1]), False)
        self.assertEqual(check_full(input[2]), False)
        self.assertEqual(check_full(input[3]), True)
        self.assertEqual(check_full(input[4]), True)
        self.assertEqual(check_full(input[5]), False)

    def test_check_part(self):
        self.assertEqual(check_part(input[0]), False)
        self.assertEqual(check_part(input[1]), False)
        self.assertEqual(check_part(input[2]), True)
        self.assertEqual(check_part(input[3]), True)
        self.assertEqual(check_part(input[4]), True)
        self.assertEqual(check_part(input[5]), True)

if __name__ == '__main__':
    unittest.main()