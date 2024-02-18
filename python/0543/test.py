import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0543(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3, 4, 5], 3],
            [[1, 2], 1],
        ]

        for i in testcases:
            lst, expected = i
            root = TreeNode.lst_to_tree(lst)
            s = Solution()
            actual = s.diameterOfBinaryTree(root)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
