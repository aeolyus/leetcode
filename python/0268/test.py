import unittest
from main import Solution


class Test0268(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 0, 1], 2],
            [[0, 1], 2],
            [[9, 6, 4, 2, 3, 5, 7, 0, 1], 8],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.missingNumber(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
