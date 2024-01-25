import unittest
from main import Solution


class Test0435(unittest.TestCase):
    def test(self):
        testcases = [
            [[[1, 2], [2, 3], [3, 4], [1, 3]], 1],
            [[[1, 2], [1, 2], [1, 2]], 2],
            [[[1, 2], [2, 3]], 0],
        ]

        for i in testcases:
            intervals, expected = i
            s = Solution()
            actual = s.eraseOverlapIntervals(intervals)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
