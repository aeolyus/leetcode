import unittest
from typing import Optional, List
from main import Solution, TreeNode


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
            root = build_tree(lst)
            s = Solution()
            s.flatten(root)
            actual = tree_to_lst(root)
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


def tree_to_lst(root: Optional[TreeNode]) -> List[int]:
    result = []
    queue = []
    if root:
        queue.append(root)

    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(node)
            continue
        result.append(node.val)
        if node.left is not None or node.right is not None:
            queue.extend((node.left, node.right))
    return result


if __name__ == '__main__':
    unittest.main()
