import unittest
from main import Solution


class Test0347(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 1, 1, 2, 2, 3], 2, [1, 2]],
            [[1], 1, [1]],
        ]

        for i in testcases:
            nums, k, expected = i
            s = Solution()
            actual = s.topKFrequent(nums, k)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
