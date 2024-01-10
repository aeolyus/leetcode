import unittest
from main import Solution, TreeNode


class Test0111(unittest.TestCase):
    def test(self):
        testcases = [
            [[3, 9, 20, None, None, 15, 7], 2],
            [[1, 2, 3, 4, 5], 2],
            [[2, None, 3, None, 4, None, 5, None, 6], 5],
        ]

        for i in testcases:
            lst, expected = i
            root = build_tree(lst)
            s = Solution()
            actual = s.minDepth(root)
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
