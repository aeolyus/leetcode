import unittest
from main import Solution


class Test0001(unittest.TestCase):
    def test(self):
        testcases = [
            [[-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]],
            [[0, 1, 1], []],
            [[0, 0, 0], [[0, 0, 0]]],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = s.threeSum(nums)

            expected = list(map(lambda lst: sorted(lst), expected))
            actual = list(map(lambda lst: sorted(lst), actual))
            expected = sorted(expected)
            actual = sorted(actual)
            self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
