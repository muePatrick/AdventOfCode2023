import unittest
from solution import getSolution

input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

target = 281

class TestStringMethods(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(getSolution(input), target)

if __name__ == '__main__':
    unittest.main()
