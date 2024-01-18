import unittest
from main import Solution


class Test0134(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 3, 4], [3, 4, 3], -1],
            [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3],
        ]

        for i in testcases:
            gas, cost, expected = i
            s = Solution()
            actual = s.canCompleteCircuit(gas, cost)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
