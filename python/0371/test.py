import unittest
from main import Solution


class Test0371(unittest.TestCase):
    def test(self):
        testcases = [
            [1, 2, 3],
            [2, 3, 5],
        ]

        for i in testcases:
            a, b, expected = i
            s = Solution()
            actual = s.getSum(a, b)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
