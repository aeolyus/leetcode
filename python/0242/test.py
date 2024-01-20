import unittest
from main import Solution


class Test0248(unittest.TestCase):
    def test(self):
        testcases = [
            ["anagram", "nagaram", True],
            ["rat", "car", False],
        ]

        for i in testcases:
            s, t, expected = i
            sol = Solution()
            actual = sol.isAnagram(s, t)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
