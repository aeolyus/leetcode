import unittest
from main import Solution


class Test0066(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3], [1, 2, 4]],
            [[4, 3, 2, 1], [4, 3, 2, 2]],
            [[9], [1, 0]],
        ]

        for i in testcases:
            digits, expected = i
            s = Solution()
            actual = s.plusOne(digits)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
