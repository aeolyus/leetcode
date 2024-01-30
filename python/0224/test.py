import unittest
from main import Solution


class Test0224(unittest.TestCase):
    def test(self):
        testcases = [
            ["1 + 1", 2],
            [" 2-1 + 2 ", 3],
            ["(1+(4+5+2)-3)+(6+8)", 23],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.calculate(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
