import unittest
from main import Solution


class Test0921(unittest.TestCase):
    def test(self):
        testcases = [
            ["())", 1],
            ["(((", 3],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.minAddToMakeValid(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
