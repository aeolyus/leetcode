import unittest
from main import Solution


class Test2405(unittest.TestCase):
    def test(self):
        testcases = [
            ["abacaba", 4],
            ["ssssss", 6],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.partitionString(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
