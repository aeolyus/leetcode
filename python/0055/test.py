import unittest
from main import Solution


class Test0055(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 3, 1, 1, 4], True],
            [[3, 2, 1, 0, 4], False],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.canJump(nums)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
