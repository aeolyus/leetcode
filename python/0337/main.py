from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        i = self.rob(root.left) + self.rob(root.right)
        j = root.val
        if root.left:
            j += self.rob(root.left.left)
            j += self.rob(root.left.right)
        if root.right:
            j += self.rob(root.right.left)
            j += self.rob(root.right.right)
        return max(i, j)
