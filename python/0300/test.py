import unittest
from main import Solution


class Test0300(unittest.TestCase):
    def test(self):
        testcases = [
            [[10, 9, 2, 5, 3, 7, 101, 18], 4],
            [[0, 1, 0, 3, 2, 3], 4],
            [[7, 7, 7, 7, 7, 7, 7], 1],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.lengthOfLIS(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
