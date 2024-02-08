import unittest
from main import Solution


class Test1249(unittest.TestCase):
    def test(self):
        testcases = [
            ["lee(t(c)o)de)", "lee(t(c)o)de"],
            ["a)b(c)d", "ab(c)d"],
            ["))((", ""],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.minRemoveToMakeValid(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
