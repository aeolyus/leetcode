import unittest
from main import Solution


class Test0238(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3, 4], [24, 12, 8, 6]],
            [[-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.productExceptSelf(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
