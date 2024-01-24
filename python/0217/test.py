import unittest
from main import Solution


class Test0217(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3, 1], True],
            [[1, 2, 3, 4], False],
            [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.containsDuplicate(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
