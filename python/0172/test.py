import unittest
from main import Solution


class Test0172(unittest.TestCase):
    def test(self):
        testcases = [
            [3, 0],
            [5, 1],
            [0, 0],
        ]

        for i in testcases:
            n, expected = i
            s = Solution()
            actual = s.trailingZeroes(n)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
