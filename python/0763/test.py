import unittest
from main import Solution


class Test0763(unittest.TestCase):
    def test(self):
        testcases = [
            ["ababcbacadefegdehijhklij", [9, 7, 8]],
            ["eccbbbbdec", [10]],
        ]

        for i in testcases:
            s, expected = i
            sol = Solution()
            actual = sol.partitionLabels(s)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
