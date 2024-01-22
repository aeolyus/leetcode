import unittest
from main import Solution


class Test1313(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3, 4], [2, 4, 4, 4]],
            [[1, 1, 2, 3], [1, 3, 3]],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.decompressRLElist(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
