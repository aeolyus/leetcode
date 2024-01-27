import unittest
from main import Solution


class Test0041(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 0], 3],
            [[3, 4, -1, 1], 2],
            [[7, 8, 9, 11, 12], 1],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.firstMissingPositive(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
