from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def depth(node: TreeNode):
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.result = max(self.result, left + right + 1)
            return max(left, right) + 1
        depth(root)
        return self.result - 1
