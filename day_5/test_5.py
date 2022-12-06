import unittest
from day_5 import stack_height, stack_parser, num_parser, rearrange, rearrange2

input = """    
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
input = input.splitlines()
input = input[1::]
print(input)

class Test5(unittest.TestCase):

    def test_stack_height(self):
        self.assertEqual(stack_height(input), 3)

    def test_parser(self):
        self.assertEqual(stack_parser(input[:4]), [['Z','N'],['M','C','D'],['P']])

    def test_num_parser(self):
        self.assertEqual(num_parser(input[5]), [1,2,1])
        self.assertEqual(num_parser(input[6]), [3,1,3])
        self.assertEqual(num_parser(input[7]), [2,2,1])
        self.assertEqual(num_parser(input[8]), [1,1,2])

    def test_rearrange(self):
        self.assertEqual(rearrange(input), "CMZ")

    def test_rearragne2(self):
        self.assertEqual(rearrange2(input), "MCD")

if __name__ == '__main__':
    unittest.main()