import unittest
from main import Solution


class Test0001(unittest.TestCase):
    def test(self):
        testcases = [
            ["babad", "bab"],
            ["cbbd", "bb"],
            ["aacabdkacaa", "aca"],
            ["aaaaa", "aaaaa"],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.longestPalindrome(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
