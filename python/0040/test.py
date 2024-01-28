import unittest
from main import Solution


class Test0040(unittest.TestCase):
    def test(self):
        testcases = [
            [
                [10, 1, 2, 7, 6, 1, 5],
                8,
                [
                    [1, 1, 6],
                    [1, 2, 5],
                    [1, 7],
                    [2, 6],
                ],
            ],
            [
                [2, 5, 2, 1, 2],
                5,
                [
                    [1, 2, 2],
                    [5],
                ],
            ],
        ]

        for i in testcases:
            candidates, target, expected = i
            s = Solution()
            actual = s.combinationSum2(candidates, target)
            expected = set(tuple(i) for i in expected)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
