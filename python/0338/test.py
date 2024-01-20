import unittest
from main import Solution


class Test0338(unittest.TestCase):
    def test(self):
        testcases = [
            [2, [0, 1, 1]],
            [5, [0, 1, 1, 2, 1, 2]],
        ]

        for i in testcases:
            n, expected = i
            s = Solution()
            actual = s.countBits(n)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
