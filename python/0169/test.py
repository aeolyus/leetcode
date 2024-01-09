import unittest
from main import Solution


class Test0001(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 2, 3], 3],
            [[2, 2, 1, 1, 1, 2, 2], 2],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.majorityElement(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
