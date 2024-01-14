import unittest
from main import Solution


class Test0168(unittest.TestCase):
    def test(self):
        testcases = [
            [1, "A"],
            [28, "AB"],
            [701, "ZY"],
        ]

        for i in testcases:
            columnNumber, expected = i
            s = Solution()
            actual = s.convertToTitle(columnNumber)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
