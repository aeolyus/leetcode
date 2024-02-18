import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0112(unittest.TestCase):
    def test(self):
        testcases = [
            [[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True],
            [[1, 2, 3], 5, False],
            [[], 0, False],
        ]

        for i in testcases:
            lst, target_sum, expected = i
            root = TreeNode.lst_to_tree(lst)
            s = Solution()
            actual = s.hasPathSum(root, target_sum)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
