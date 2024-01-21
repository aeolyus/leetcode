import unittest
from main import Solution


class Test0350(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 2, 1], [2, 2], [2, 2]],
            [[4, 9, 5], [9, 4, 9, 8, 4], [9, 4]],
        ]

        for i in testcases:
            nums1, nums2, expected = i
            s = Solution()
            actual = s.intersect(nums1, nums2)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
