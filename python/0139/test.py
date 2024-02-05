import unittest
from main import Solution


class Test0139(unittest.TestCase):
    def test(self):
        testcases = [
            ["leetcode", ["leet", "code"], True],
            ["applepenapple", ["apple", "pen"], True],
            ["catsandog", ["cats", "dog", "sand", "and", "cat"], False],
        ]

        for i in testcases:
            s, wordDict, expected = i
            sol = Solution()
            actual = sol.wordBreak(s, wordDict)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
