import unittest
from main import LRUCache


class Test0146(unittest.TestCase):
    def test(self):
        testcases = [
            [
                    ["LRUCache", "put", "put", "get", "put", "get", "put",
                     "get", "get", "get"],
                    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3],
                     [4]],
                    [None, None, None, 1, None, -1, None, -1, 3, 4],
            ],
        ]

        for tc in testcases:
            instrs, args, expected = tc
            cache: LRUCache
            for i in range(len(instrs)):
                instr = instrs[i]
                actual = None
                if instr == "LRUCache":
                    cache = LRUCache(*args[i])
                elif instr == "put":
                    actual = cache.put(*args[i])
                elif instr == "get":
                    actual = cache.get(args[i][0])
                self.assertEqual(expected[i], actual)


if __name__ == '__main__':
    unittest.main()
