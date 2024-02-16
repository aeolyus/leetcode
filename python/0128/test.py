import unittest
from main import Solution


class Test0128(unittest.TestCase):
    def test(self):
        testcases = [
            [[100, 4, 200, 1, 3, 2], 4],
            [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.longestConsecutive(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
