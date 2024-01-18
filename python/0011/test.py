import unittest
from main import Solution


class Test0011(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49],
            [[1, 1], 1],
            [[2, 3, 4, 5, 18, 17, 6], 17],
        ]

        for i in testcases:
            height, expected = i
            s = Solution()
            actual = s.maxArea(height)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
