import unittest
from main import MedianFinder


class Test0295(unittest.TestCase):
    def test(self):
        testcases = [
            [
                ["MedianFinder", "addNum", "addNum",
                    "findMedian", "addNum", "findMedian"],
                [[], [1], [2], [], [3], []],
                [None, None, None, 1.5, None, 2.0],
            ],
        ]

        for tc in testcases:
            instrs, args, expecteds = tc
            mf = None
            for i, instr in enumerate(instrs):
                actual = None
                if instr == "MedianFinder":
                    mf = MedianFinder()
                elif instr == "addNum":
                    mf.addNum(args[i][0])
                elif instr == "findMedian":
                    actual = mf.findMedian()
                self.assertEqual(expecteds[i], actual)


if __name__ == '__main__':
    unittest.main()
