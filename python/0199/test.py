import unittest
from main import Solution, TreeNode


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
            root = build_tree(lst)
            actual = s.rightSideView(root)
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
