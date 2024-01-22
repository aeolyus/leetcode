import unittest
from main import Solution


class Test0443(unittest.TestCase):
    def test(self):
        testcases = [
            [
                ["a", "a", "b", "b", "c", "c", "c"],
                ["a", "2", "b", "2", "c", "3"],
            ],
            [
                ["a"],
                ["a"],
            ],
            [
                ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b",
                 "b"],
                ["a", "b", "1", "2"],
            ],
        ]

        for i in testcases:
            chars, expected = i
            s = Solution()
            i = s.compress(chars)
            actual = chars[:i]
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
