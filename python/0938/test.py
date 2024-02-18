import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0938(unittest.TestCase):
    def test(self):
        testcases = [
            [[10, 5, 15, 3, 7, None, 18], 7, 15, 32],
            [[10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23],
        ]

        for i in testcases:
            lst, low, high, expected = i
            s = Solution()
            root = TreeNode.lst_to_tree(lst)
            actual = s.rangeSumBST(root, low, high)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
