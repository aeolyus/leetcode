import unittest
from main import Solution


class Test0088(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]],
            [[1], 1, [], 0, [1]],
            [[0], 0, [1], 1, [1]],
        ]

        for i in testcases:
            nums1, m, nums2, n, expected = i
            s = Solution()
            s.merge(nums1, m, nums2, n)
            self.assertEqual(expected, nums1)


if __name__ == '__main__':
    unittest.main()
