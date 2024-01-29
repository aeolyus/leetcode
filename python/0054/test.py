import unittest
from main import Solution


class Test0054(unittest.TestCase):
    def test(self):
        testcases = [
            # [
            #     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            #     [1, 2, 3, 6, 9, 8, 7, 4, 5]
            # ],
            # [
            #     [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            #     [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            # ],
            [[[6, 9, 7]], [6, 9, 7]],
        ]

        for i in testcases:
            matrix, expected = i
            s = Solution()
            actual = s.spiralOrder(matrix)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
