import unittest
from main import Solution


class Test0918(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, -2, 3, -2], 3],
            [[5, -3, 5], 10],
            [[-3, -2, -3], -2],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.maxSubarraySumCircular(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
