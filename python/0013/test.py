import unittest
from main import Solution


class Test0013(unittest.TestCase):
    def test(self):
        testcases = [
            ["III", 3],
            ["LVIII", 58],
            ["MCMXCIV", 1994],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.romanToInt(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
