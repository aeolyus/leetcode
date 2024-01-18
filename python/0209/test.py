import unittest
from main import Solution


class Test0209(unittest.TestCase):
    def test(self):
        testcases = [
            [7, [2, 3, 1, 2, 4, 3], 2],
            [4, [1, 4, 4], 1],
            [11, [1, 1, 1, 1, 1, 1, 1, 1], 0],
        ]

        for i in testcases:
            target, nums, expected = i
            s = Solution()
            actual = s.minSubArrayLen(target, nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
