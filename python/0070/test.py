import unittest
from main import Solution


class Test0070(unittest.TestCase):
    def test(self):
        testcases = [
            [2, 2],
            [3, 3],
        ]

        for i in testcases:
            n, expected = i
            s = Solution()
            actual = s.climbStairs(n)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
