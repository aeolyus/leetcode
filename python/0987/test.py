import unittest
from main import Solution, TreeNode


class Test0987(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]],
            [[1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]],
            [[1, 2, 3, 4, 6, 5, 7], [[4], [2], [1, 5, 6], [3], [7]]],
        ]

        for i in testcases:
            lst, expected = i
            s = Solution()
            root = TreeNode.lst_to_tree(lst)
            actual = s.verticalTraversal(root)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
