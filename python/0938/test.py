import unittest
from main import Solution, TreeNode


class Test0938(unittest.TestCase):
    def test(self):
        testcases = [
            [[10, 5, 15, 3, 7, None, 18], 7, 15, 32],
            [[10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23],
        ]

        for i in testcases:
            lst, low, high, expected = i
            s = Solution()
            root = build_tree(lst)
            actual = s.rangeSumBST(root, low, high)
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
