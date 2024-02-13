import unittest
from main import Solution


class Test0071(unittest.TestCase):
    def test(self):
        testcases = [
            ["/a//b////c/d//././/..", "/a/b/c"],
            ["/home/", "/home"],
            ["/../", "/"],
            ["/home//foo/", "/home/foo"],
        ]

        for i in testcases:
            path, expected = i
            s = Solution()
            actual = s.simplifyPath(path)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
