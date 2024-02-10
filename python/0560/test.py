import unittest
from main import Solution


class Test0560(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 1, 1], 2, 2],
            [[1, 2, 3], 3, 2],
        ]

        for i in testcases:
            nums, k, expected = i
            s = Solution()
            actual = s.subarraySum(nums, k)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
