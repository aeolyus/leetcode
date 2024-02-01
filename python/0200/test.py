import unittest
from main import Solution


class Test0200(unittest.TestCase):
    def test(self):
        testcases = [
            [
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"]
                ],
                1,
            ],
            [
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"]
                ],
                3,
            ],
        ]

        for i in testcases:
            grid, expected = i
            s = Solution()
            actual = s.numIslands(grid)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
