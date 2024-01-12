import unittest
from main import Solution


class Test0029(unittest.TestCase):
    def test(self):
        testcases = [
            [10, 3, 3],
            [7, -3, -2],
        ]

        for i in testcases:
            dividend, divisor, expected = i
            s = Solution()
            actual = s.divide(dividend, divisor)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
