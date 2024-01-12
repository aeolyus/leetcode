import unittest
from main import Solution


class Test0012(unittest.TestCase):
    def test(self):
        testcases = [
            [3, "III"],
            [58, "LVIII"],
            [1994, "MCMXCIV"],
        ]

        for i in testcases:
            num, expected = i
            s = Solution()
            actual = s.intToRoman(num)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
