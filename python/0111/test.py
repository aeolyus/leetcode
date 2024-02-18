import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0111(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 9, 20, None, None, 15, 7], 2],
            [[1, 2, 3, 4, 5], 2],
            [[2, None, 3, None, 4, None, 5, None, 6], 5],
        ]

        for i in testcases:
            lst, expected = i
            root = TreeNode.lst_to_tree(lst)
            s = Solution()
            actual = s.minDepth(root)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
