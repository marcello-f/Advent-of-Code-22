import unittest
from day_1 import calories

input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

input = input.splitlines()

class Test1(unittest.TestCase):

    def test_calories(self):
        seen = calories(input)
        seen_sorted = sorted(seen)

        self.assertEqual(seen[0], 6000)
        self.assertEqual(seen[1], 4000)
        self.assertEqual(seen[2], 11000)
        self.assertEqual(seen[3], 24000)
        self.assertEqual(seen[4], 10000)

        self.assertEqual(sum(seen_sorted[-3:]), 45000)

if __name__ == '__main__':
    unittest.main()
