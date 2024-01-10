import unittest
from main import Solution


class Test0008(unittest.TestCase):
    def test(self):
        testcases = [
            ["42", 42],
            ["   -42", -42],
            ["4193 with words", 4193],
            ["words and 987", 0],
            ["-91283472332", -2147483648],
            ["+-12", 0],
            ["  +  413", 0],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.myAtoi(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
