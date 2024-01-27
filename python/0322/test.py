import unittest
from main import Solution


class Test0322(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 5], 11, 3],
            [[2], 3, -1],
            [[1], 0, 0],
        ]

        for i in testcases:
            coins, amount, expected = i
            s = Solution()
            actual = s.coinChange(coins, amount)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
