import unittest
from main import Solution


class Test1047(unittest.TestCase):
    def test(self):
        testcases = [
            ["abbaca", "ca"],
            ["azxxzy", "ay"],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.removeDuplicates(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
