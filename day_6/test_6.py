import unittest
import day_6

input1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
input2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
input3 = "nppdvjthqldpwncqszvftbrmjlhg"
input4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
input5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

class Test6(unittest.TestCase):
    
    def test_marker(self):
        self.assertEqual(day_6.marker(input1, 4), 7)
        self.assertEqual(day_6.marker(input2, 4), 5)
        self.assertEqual(day_6.marker(input3, 4), 6)
        self.assertEqual(day_6.marker(input4, 4), 10)
        self.assertEqual(day_6.marker(input5, 4), 11)

        self.assertEqual(day_6.marker(input1, 14), 19)
        self.assertEqual(day_6.marker(input2, 14), 23)
        self.assertEqual(day_6.marker(input3, 14), 23)
        self.assertEqual(day_6.marker(input4, 14), 29)
        self.assertEqual(day_6.marker(input5, 14), 26)



if __name__ == '__main__':
    unittest.main()