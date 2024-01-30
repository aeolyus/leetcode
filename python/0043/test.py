import unittest
from main import Solution


class Test0043(unittest.TestCase):
    def test(self):
        testcases = [
            ["2", "3", "6"],
            ["123", "456", "56088"],
            ["0", "0", "0"],
        ]

        for i in testcases:
            num1, num2, expected = i
            s = Solution()
            actual = s.multiply(num1, num2)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
