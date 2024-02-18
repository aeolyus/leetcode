import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0226(unittest.TestCase):
    def test(self):
        testcases = [
            [[4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]],
            [[2, 1, 3], [2, 3, 1]],
            [[], []],
        ]

        for i in testcases:
            lst, expected = i
            root = TreeNode.lst_to_tree(lst)
            s = Solution()
            s.invertTree(root)
            actual = TreeNode.tree_to_lst(root)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
