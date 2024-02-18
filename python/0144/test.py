import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0144(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, None, 2, 3], [1, 2, 3]],
            [[], []],
            [[1], [1]],
        ]

        for i in testcases:
            lst, expected = i
            root = TreeNode.lst_to_tree(lst)
            s = Solution()
            actual = s.preorderTraversal(root)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
