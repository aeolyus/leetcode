import unittest
from main import Solution


class Test0991(unittest.TestCase):
    def test(self):
        testcases = [
            [2, 3, 2],
            [5, 8, 2],
            [3, 10, 3],
        ]

        for i in testcases:
            startValue, target, expected = i
            s = Solution()
            actual = s.brokenCalc(startValue, target)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
