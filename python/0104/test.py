import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0104(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 9, 20, None, None, 15, 7], 3],
            [[1, None, 2], 2],
        ]

        for i in testcases:
            lst, expected = i
            root = TreeNode.lst_to_tree(lst)
            s = Solution()
            actual = s.maxDepth(root)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
