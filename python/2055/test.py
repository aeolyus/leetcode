import unittest
from main import Solution


class Test2055(unittest.TestCase):
    def test(self):
        testcases = [
            [
                "**|**|***|",
                [[2, 5], [5, 9]],
                [2, 3]
            ],
            [
                "***|**|*****|**||**|*",
                [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]],
                [9, 0, 0, 0, 0]
            ],
        ]

        for i in testcases:
            s, queries, expected = i
            sol = Solution()
            actual = sol.platesBetweenCandles(s, queries)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
