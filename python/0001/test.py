import unittest
from main import Solution


class Test0001(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 7, 11, 15], 9, [0, 1]],
            [[3, 2, 4], 6, [1, 2]],
            [[3, 3], 6, [0, 1]],
        ]

        for i in testcases:
            nums, target, expected = i
            s = Solution()
            actual = s.twoSum(nums, target)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
