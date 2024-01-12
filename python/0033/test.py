import unittest
from main import Solution


class Test0033(unittest.TestCase):
    def test(self):
        testcases = [
            [[4, 5, 6, 7, 0, 1, 2], 0, 4],
            [[4, 5, 6, 7, 0, 1, 2], 3, -1],
            [[1], 0, -1],
        ]

        for i in testcases:
            nums, target, expected = i
            s = Solution()
            actual = s.search(nums, target)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
