import unittest
from main import Solution


class Test0014(unittest.TestCase):
    def test(self):
        testcases = [
            [["flower", "flow", "flight"], "fl"],
            [["dog", "racecar", "car"], ""],
        ]

        for i in testcases:
            strs, expected = i
            s = Solution()
            actual = s.longestCommonPrefix(strs)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
