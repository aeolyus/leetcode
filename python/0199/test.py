import unittest
from main import Solution
from python.lib.tree import TreeNode


class Test0199(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3, None, 5, None, 4], [1, 3, 4]],
            [[1, None, 3], [1, 3]],
            [[], []],
        ]

        for i in testcases:
            lst, expected = i
            s = Solution()
            root = TreeNode.lst_to_tree(lst)
            actual = s.rightSideView(root)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
