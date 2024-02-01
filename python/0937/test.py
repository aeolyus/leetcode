import unittest
from main import Solution


class Test0937(unittest.TestCase):
    def test(self):
        testcases = [
            [
                [
                    "dig1 8 1 5 1",
                    "let1 art can", "dig2 3 6",
                    "let2 own kit dig",
                    "let3 art zero",
                ],
                [
                    "let1 art can",
                    "let3 art zero",
                    "let2 own kit dig",
                    "dig1 8 1 5 1",
                    "dig2 3 6",
                ],
            ],
            [
                [
                    "a1 9 2 3 1",
                    "g1 act car",
                    "zo4 4 7",
                    "ab1 off key dog",
                    "a8 act zoo",
                ],
                [
                    "g1 act car",
                    "a8 act zoo",
                    "ab1 off key dog",
                    "a1 9 2 3 1",
                    "zo4 4 7",
                ],
            ],
        ]

        for i in testcases:
            logs, expected = i
            s = Solution()
            actual = s.reorderLogFiles(logs)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
