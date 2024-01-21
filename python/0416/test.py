import unittest
from main import Solution


class Test0416(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 5, 11, 5], True],
            [[1, 2, 3, 5], False],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.canPartition(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
