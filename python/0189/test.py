import unittest
from main import Solution


class Test0001(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]],
            [[-1, -100, 3, 99], 2, [3, 99, -1, -100]],
        ]

        for i in testcases:
            nums, k, expected = i
            s = Solution()
            s.rotate(nums, k)
            self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main()
