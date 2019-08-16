# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    prev = None
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                prev = root.left
                while prev.right:
                    prev = prev.right
                prev.right = root.right
                root.right, root.left = root.left, None
            root = root.right
