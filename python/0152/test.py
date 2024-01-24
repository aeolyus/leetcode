import unittest
from main import Solution


class Test0152(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 3, -2, 4], 6],
            [[-2, 0, -1], 0],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.maxProduct(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
