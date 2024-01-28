import unittest
from main import Solution


class Test0039(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 3, 6, 7], 7, [[2, 2, 3], [7]]],
            [[2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]],
            [[2], 1, []]
        ]

        for i in testcases:
            candidates, target, expected = i
            s = Solution()
            actual = s.combinationSum(candidates, target)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
