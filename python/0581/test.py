import unittest
from main import Solution


class Test0581(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 6, 4, 8, 10, 9, 15], 5],
            [[1, 2, 3, 4], 0],
            [[1], 0],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.findUnsortedSubarray(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
