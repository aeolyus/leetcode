import unittest
from main import Solution


class Test0973(unittest.TestCase):
    def test(self):
        testcases = [
            [
                [[1, 3], [-2, 2]],
                1,
                [[-2, 2]]],
            [
                [[3, 3], [5, -1], [-2, 4]],
                2,
                [[3, 3], [-2, 4]],
            ],
        ]

        for i in testcases:
            points, k, expected = i
            s = Solution()
            actual = s.kClosest(points, k)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
