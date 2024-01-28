import unittest
from main import Solution


class Test0004(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 3], [2], 2],
            [[1, 2], [3, 4], 2.5],
        ]

        for i in testcases:
            nums1, nums2, expected = i
            s = Solution()
            actual = s.findMedianSortedArrays(nums1, nums2)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
