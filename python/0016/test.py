import unittest
from main import Solution


class Test0016(unittest.TestCase):
    def test(self):
        testcases = [
            [[-1, 2, 1, -4], 1, 2],
            [[0, 0, 0], 1, 0],
            [[0, 1, 2], 3, 3],
        ]

        for i in testcases:
            nums, target, expected = i
            s = Solution()
            actual = s.threeSumClosest(nums, target)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
