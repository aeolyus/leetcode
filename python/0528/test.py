import unittest
from main import Solution


class Test0528(unittest.TestCase):
    def test(self):
        testcases = [
            [
                ["Solution", "pickIndex"],
                [[[1]], []],
                [None, 0]
            ],
            [
                ["Solution", "pickIndex", "pickIndex",
                    "pickIndex", "pickIndex", "pickIndex"],
                [[[1, 3]], [], [], [], [], []],
                [None, 1, 1, 1, 1, 0],
            ],
        ]

        for tc in testcases:
            instrs, args, expecteds = tc
            sol: Solution = None
            for i, instr in enumerate(instrs):
                actual = None
                if instr == "Solution":
                    sol = Solution(args[i][0])
                elif instr == "pickIndex":
                    actual = sol.pickIndex()
            self.assertEqual(expecteds[i], actual)


if __name__ == '__main__':
    unittest.main()
