import unittest
from main import Solution


class Test0057(unittest.TestCase):
    def test(self):
        testcases = [
            [
                [[1, 3], [6, 9]],
                [2, 5],
                [[1, 5], [6, 9]],
            ],
            [
                [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                [4, 8],
                [[1, 2], [3, 10], [12, 16]],
            ],
        ]

        for i in testcases:
            intervals, newInterval, expected = i
            s = Solution()
            actual = s.insert(intervals, newInterval)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
