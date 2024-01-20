import unittest
from main import Solution


class Test0387(unittest.TestCase):
    def test(self):
        testcases = [
            ["leetcode", 0],
            ["loveleetcode", 2],
            ["aabb", -1],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.firstUniqChar(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
