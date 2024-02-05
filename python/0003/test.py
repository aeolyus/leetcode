import unittest
from main import Solution


class Test0003(unittest.TestCase):
    def test(self):
        testcases = [
            ["abcabcbb", 3],
            ["bbbbb", 1],
            ["pwwkew", 3],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.lengthOfLongestSubstring(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
