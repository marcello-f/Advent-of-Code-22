import unittest
from day_2 import WDL, WDL2

input = """A Y
B X
C Z
"""
input = input.splitlines()

class Test6(unittest.TestCase):
    
    def test_WDL(self):
        self.assertEqual(WDL(input[0]), 8)
        self.assertEqual(WDL(input[1]), 1)
        self.assertEqual(WDL(input[2]), 6)

    def test_WDL2(self):
        self.assertEqual(WDL2(input[0]), 4)
        self.assertEqual(WDL2(input[1]), 1)
        self.assertEqual(WDL2(input[2]), 7)


if __name__ == '__main__':
    unittest.main()