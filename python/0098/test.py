import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0098(unittest.TestCase):
    def test(self):
        testcases = [
            [[2, 1, 3], True],
            [[5, 1, 4, None, None, 3, 6], False],
        ]

        for i in testcases:
            lst, expected = i
            s = Solution()
            root = TreeNode.lst_to_tree(lst)
            actual = s.isValidBST(root)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
