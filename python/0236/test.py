import unittest
from main import Solution, TreeNode


class Test0236(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3],
            [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5],
            [[1, 2], 1, 2, 1],
        ]

        for i in testcases:
            lst, p_val, q_val, expected = i
            root = build_tree(lst)
            p = TreeNode(p_val)
            q = TreeNode(q_val)
            s = Solution()
            actual = s.lowestCommonAncestor(root, p, q).val
            self.assertEqual(expected, actual)


def build_tree(lst) -> TreeNode:
    lookup = {}
    root = None
    offset = 0
    for i, val in enumerate(lst):
        if val is None:
            offset += 1
            continue
        node = None
        if root is None:
            node = TreeNode(val)
            root = node
        else:
            node = lookup[i]
        left = 2*(i - offset) + 1
        right = 2*(i - offset) + 2
        if left < len(lst) and lst[left] is not None:
            node.left = TreeNode(lst[left])
            lookup[left] = node.left
        if right < len(lst) and lst[right] is not None:
            node.right = TreeNode(lst[right])
            lookup[right] = node.right
    return root


if __name__ == '__main__':
    unittest.main()
