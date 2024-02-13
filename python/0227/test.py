import unittest
from main import Solution


class Test0227(unittest.TestCase):
    def test(self):
        testcases = [
            ["3+2*2", 7],
            [" 3/2 ", 1],
            [" 3+5 / 2 ", 5],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.calculate(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
