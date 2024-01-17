import unittest
from main import RandomizedSet


class Test0380(unittest.TestCase):
    def test(self):
        testcases = [
            [
                    ["RandomizedSet", "insert", "remove", "insert",
                     "getRandom", "remove", "insert", "getRandom"],
                    [[], [1], [2], [2], [], [1], [2], []],
                    [None, True, False, True, 2, True, False, 2]
            ]
        ]

        for t in testcases:
            instructions, values, expecteds = t
            r = None
            for i, instr in enumerate(instructions):
                actual = None
                if instr == "RandomizedSet":
                    r = RandomizedSet()
                elif instr == "insert":
                    actual = r.insert(values[i][0])
                elif instr == "remove":
                    actual = r.remove(values[i][0])
                elif instr == "getRandom":
                    actual = r.getRandom()
                self.assertEqual(expecteds[i], actual)


if __name__ == '__main__':
    unittest.main()
