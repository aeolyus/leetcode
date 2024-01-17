import unittest
from main import Solution


class Test0274(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 0, 6, 1, 5], 3],
            [[1, 3, 1], 1],
        ]

        for i in testcases:
            citations, expected = i
            s = Solution()
            actual = s.hIndex(citations)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
