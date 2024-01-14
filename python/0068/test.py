import unittest
from main import Solution


class Test0068(unittest.TestCase):
    def test(self):
        testcases = [
            [4, 2],
            [8, 2],
        ]

        for i in testcases:
            x, expected = i
            s = Solution()
            actual = s.mySqrt(x)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
