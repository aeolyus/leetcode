import unittest
from main import Solution


class Test0045(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 3, 1, 1, 4], 2],
            [[2, 3, 0, 1, 4], 2],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.jump(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
