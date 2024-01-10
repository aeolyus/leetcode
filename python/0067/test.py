import unittest
from main import Solution


class Test0067(unittest.TestCase):
    def test(self):
        testcases = [
            ["11", "1", "100"],
            ["1010", "1011", "10101"],
        ]

        for i in testcases:
            a, b, expected = i
            s = Solution()
            actual = s.addBinary(a, b)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
