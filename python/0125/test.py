import unittest
from main import Solution


class Test0125(unittest.TestCase):
    def test(self):
        testcases = [
            ["A man, a plan, a canal: Panama", True],
            ["race a car", False],
            [" ", True],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.isPalindrome(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
