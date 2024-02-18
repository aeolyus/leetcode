import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0236(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3],
            [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5],
            [[1, 2], 1, 2, 1],
        ]

        for i in testcases:
            lst, p_val, q_val, expected = i
            root = TreeNode.lst_to_tree(lst)
            p = TreeNode(p_val)
            q = TreeNode(q_val)
            s = Solution()
            actual = s.lowestCommonAncestor(root, p, q).val
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
