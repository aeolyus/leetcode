import unittest
from main import Solution


class Test0056(unittest.TestCase):
    def test(self):
        testcases = [
            [[[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]],
            [[[1, 4], [4, 5]], [[1, 5]]],
        ]

        for i in testcases:
            intervals, expected = i
            s = Solution()
            actual = s.merge(intervals)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
