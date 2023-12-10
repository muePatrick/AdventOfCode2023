import unittest
from solution import getSolution

input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

target = 467835

class TestStringMethods(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(getSolution(input), target)

if __name__ == '__main__':
    unittest.main()
