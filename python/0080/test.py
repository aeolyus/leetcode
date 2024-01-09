import unittest
from main import Solution


class Test0080(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 1, 2, 2, 3], [1, 1, 2, 2, 3]],
            [[0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3]],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            k = s.removeDuplicates(nums)
            self.assertEqual(expected, nums[:k])


if __name__ == '__main__':
    unittest.main()
