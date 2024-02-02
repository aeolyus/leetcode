import unittest
from main import Solution


class Test0819(unittest.TestCase):
    def test(self):
        testcases = [
            [
                "Bob hit a ball, the hit BALL flew far after it was hit.",
                ["hit"],
                "ball",
            ],
            ["a.", [], "a"],
        ]

        for i in testcases:
            paragraph, banned, expected = i
            s = Solution()
            actual = s.mostCommonWord(paragraph, banned)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
