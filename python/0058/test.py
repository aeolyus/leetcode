import unittest
from main import Solution


class Test0058(unittest.TestCase):
    def test(self):
        testcases = [
            ["Hello World", 5],
            ["   fly me   to   the moon  ", 4],
            ["luffy is still joyboy", 6],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.lengthOfLastWord(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
