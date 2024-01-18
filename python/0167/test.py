import unittest
from main import Solution


class Test0167(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 7, 11, 15], 9, [1, 2]],
            [[2, 3, 4], 6, [1, 3]],
            [[-1, 0], -1, [1, 2]],
        ]

        for i in testcases:
            nums, target, expected = i
            s = Solution()
            actual = s.twoSum(nums, target)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
