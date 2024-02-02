import unittest
from main import Solution


class Test0994(unittest.TestCase):
    def test(self):
        testcases = [
            [[[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4],
            [[[0, 2]], 0],
        ]

        for i in testcases:
            grid, expected = i
            s = Solution()
            actual = s.orangesRotting(grid)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
