import unittest
from main import Solution


class Test0392(unittest.TestCase):
    def test(self):
        testcases = [
            ["abc", "ahbgdc", True],
            ["axc", "ahbgdc", False],
        ]

        for i in testcases:
            s, t, expected = i
            sol = Solution()
            actual = sol.isSubsequence(s, t)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
