import unittest
from main import Solution


class Test0035(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 3, 5, 6], 5, 2],
            [[1, 3, 5, 6], 2, 1],
            [[1, 3, 5, 6], 7, 4],
        ]

        for i in testcases:
            nums, target, expected = i
            s = Solution()
            actual = s.searchInsert(nums, target)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
