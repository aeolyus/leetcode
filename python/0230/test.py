import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0230(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 1, 4, None, 2], 1, 1],
            [[5, 3, 6, 2, 4, None, None, 1], 3, 3],
        ]

        for i in testcases:
            lst, k, expected = i
            s = Solution()
            root = TreeNode.lst_to_tree(lst)
            actual = s.kthSmallest(root, k)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
