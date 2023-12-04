import unittest
from solution import getSolution

input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

target = 142

class TestStringMethods(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(getSolution(input), target)

if __name__ == '__main__':
    unittest.main()
