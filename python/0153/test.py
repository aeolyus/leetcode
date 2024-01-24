import unittest
from main import Solution


class Test0153(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 4, 5, 1, 2], 1],
            [[4, 5, 6, 7, 0, 1, 2], 0],
            [[11, 13, 15, 17], 11],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.findMin(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
