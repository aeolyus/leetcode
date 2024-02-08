import unittest
from main import Solution


class Test0680(unittest.TestCase):
    def test(self):
        testcases = [
            ["aba", True],
            ["abca", True],
            ["abc", False],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.validPalindrome(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
