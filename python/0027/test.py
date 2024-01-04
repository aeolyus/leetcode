import unittest
from main import Solution


class Test00027(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 2, 2, 3], 3, [2, 2]],
            [[0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 4, 0, 3]],
        ]

        for i in testcases:
            nums, val, expected = i
            s = Solution()
            k = s.removeElement(nums, val)
            self.assertEqual(expected, nums[:k])


if __name__ == '__main__':
    unittest.main()
