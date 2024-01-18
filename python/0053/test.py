import unittest
from main import Solution


class Test0053(unittest.TestCase):
    def test(self):
        testcases = [
            [[-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],
            [[1], 1],
            [[5, 4, -1, 7, 8], 23],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.maxSubArray(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
