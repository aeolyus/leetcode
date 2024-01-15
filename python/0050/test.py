import unittest
import math
from main import Solution


class Test0050(unittest.TestCase):
    def test(self):
        testcases = [
            [2, 10, math.pow(2, 10)],
            [2.1, 3, math.pow(2.1, 3)],
            [2, -2, math.pow(2, -2)],
        ]

        for i in testcases:
            x, n, expected = i
            s = Solution()
            actual = s.myPow(x, n)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
