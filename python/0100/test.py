import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0100(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3], [1, 2, 3], True],
            [[1, 2], [1, None, 2], False],
            [[1, 2, 1], [1, 1, 2], False],
        ]

        for i in testcases:
            p, q, expected = i
            p_tree = TreeNode.lst_to_tree(p)
            q_tree = TreeNode.lst_to_tree(q)
            s = Solution()
            actual = s.isSameTree(p_tree, q_tree)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
