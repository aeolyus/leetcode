import unittest
from main import Solution


class Test0017(unittest.TestCase):
    def test(self):
        testcases = [
            ["23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
            ["", []],
            ["2", ["a", "b", "c"]],
        ]

        for i in testcases:
            digits, expected = i
            s = Solution()
            actual = s.letterCombinations(digits)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
