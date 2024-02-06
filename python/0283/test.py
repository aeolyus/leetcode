import unittest
from main import Solution


class Test0283(unittest.TestCase):
    def test(self):
        testcases = [
            [[0, 1, 0, 3, 12], [1, 3, 12, 0, 0]],
            [[0], [0]],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            s.moveZeroes(nums)
            self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main()
