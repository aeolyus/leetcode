import unittest
from main import Solution


class Test0215(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 2, 1, 5, 6, 4], 2, 5],
            [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4],
        ]

        for i in testcases:
            nums, k, expected = i
            s = Solution()
            actual = s.findKthLargest(nums, k)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
