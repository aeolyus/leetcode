import unittest
from main import Solution


class Test0006(unittest.TestCase):
    def test(self):
        testcases = [
            ["PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"],
            ["PAYPALISHIRING", 4, "PINALSIGYAHRPI"],
            ["A", 1, "A"],
        ]

        for i in testcases:
            s, numRows, expected = i
            sol = Solution()
            actual = sol.convert(s, numRows)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
