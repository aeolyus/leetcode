from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, {})

    def helper(self, root, dp):
        if root is None:
            return 0
        if root in dp:
            return dp[root]
        i = self.helper(root.left, dp) + self.helper(root.right, dp)
        j = root.val
        if root.left:
            j += self.helper(root.left.left, dp)
            j += self.helper(root.left.right, dp)
        if root.right:
            j += self.helper(root.right.left, dp)
            j += self.helper(root.right.right, dp)
        dp[root] = max(i, j)
        return dp[root]
