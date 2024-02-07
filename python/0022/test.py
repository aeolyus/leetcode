import unittest
from main import Solution


class Test0022(unittest.TestCase):
    def test(self):
        testcases = [
            [3, ["((()))", "(()())", "(())()", "()(())", "()()()"]],
            [1, ["()"],]
        ]

        for i in testcases:
            n, expected = i
            s = Solution()
            actual = sorted(s.generateParenthesis(n))
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
