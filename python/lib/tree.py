from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def lst_to_tree(lst) -> 'TreeNode':
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

    @staticmethod
    def tree_to_lst(root: Optional['TreeNode']) -> List[int]:
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
