import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0337(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 2, 3, None, 3, None, 1], 7],
            [[3, 4, 5, 1, 3, None, 1], 9],
        ]

        for i in testcases:
            lst, expected = i
            s = Solution()
            root = TreeNode.lst_to_tree(lst)
            actual = s.rob(root)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
