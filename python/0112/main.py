from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def dfs(root, count):
            if root is None:
                return False
            count += root.val
            if root.left is None and root.right is None:
                return count == targetSum
            return dfs(root.left, count) or dfs(root.right, count)
        return dfs(root, 0)
