import unittest
from main import Solution, TreeNode


class Test0100(unittest.TestCase):
    def test(self):
        testcases = [
            [[1, 2, 3], [1, 2, 3], True],
            [[1, 2], [1, None, 2], False],
            [[1, 2, 1], [1, 1, 2], False],
        ]

        for i in testcases:
            p, q, expected = i
            p_tree = build_tree(p)
            q_tree = build_tree(q)
            s = Solution()
            actual = s.isSameTree(p_tree, q_tree)
            self.assertEqual(expected, actual)


def build_tree(lst) -> TreeNode:
    root = None
    for i, val in enumerate(lst):
        node = TreeNode(val)
        if not root:
            root = node
        left = 2*i + 1
        right = 2*i + 2
        if left < len(lst):
            node.left = TreeNode(lst[left])
        if right < len(lst):
            node.right = TreeNode(lst[right])
    return root


if __name__ == '__main__':
    unittest.main()
