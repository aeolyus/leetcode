from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(
            self,
            root: Optional[TreeNode],
            low: int,
            high: int,
    ) -> int:
        result = 0
        if root is None:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if low <= node.val <= high:
                result += node.val
            stack.extend([node.left, node.right])
        return result
