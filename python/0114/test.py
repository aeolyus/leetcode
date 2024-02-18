import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0114(unittest.TestCase):
    def test(self):
        testcases = [
            [
                [1, 2, 5, 3, 4, None, 6],
                [1, None, 2, None, 3, None, 4, None, 5, None, 6]
            ],
            [[], []],
            [[0], [0]],
        ]

        for i in testcases:
            lst, expected = i
            root = TreeNode.lst_to_tree(lst)
            s = Solution()
            s.flatten(root)
            actual = TreeNode.tree_to_lst(root)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
