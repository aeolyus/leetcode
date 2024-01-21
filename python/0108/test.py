import unittest
from typing import Optional, List
from main import Solution, TreeNode


class Test0108(unittest.TestCase):
    def test(self):
        testcases = [
            [[-10, -3, 0, 5, 9], [0, -10, 5, None, -3, None, 9]],
            [[1, 3], [1, None, 3]],
        ]

        for i in testcases:
            nums, expected = i
            s = Solution()
            actual = tree_to_lst(s.sortedArrayToBST(nums))
            self.assertEqual(expected, actual)


def tree_to_lst(root: Optional[TreeNode]) -> List[int]:
    result = []
    queue = [root]
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
