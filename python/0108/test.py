import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0108(unittest.TestCase):
    def test(self):
        testcases = [
            [[-10, -3, 0, 5, 9], [0, -10, 5, None, -3, None, 9]],
            [[1, 3], [1, None, 3]],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = TreeNode.tree_to_lst(s.sortedArrayToBST(nums))
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
