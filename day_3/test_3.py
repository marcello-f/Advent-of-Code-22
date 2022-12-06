import unittest
from day_3 import find_overlap

input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

input = input.splitlines()

class Test3(unittest.TestCase):

    def test_overlap(self):
        self.assertEqual(find_overlap(input[0]), 'p')
        self.assertEqual(find_overlap(input[1]), 'L')
        self.assertEqual(find_overlap(input[2]), 'P')
        self.assertEqual(find_overlap(input[3]), 'v')
        self.assertEqual(find_overlap(input[4]), 't')
        self.assertEqual(find_overlap(input[5]), 's')


if __name__ == '__main__':
    unittest.main()