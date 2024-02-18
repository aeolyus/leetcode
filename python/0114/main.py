from typing import Optional
from python.lib.tree import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        while root:
            if root.left:
                prev = root.left
                while prev.right:
                    prev = prev.right
                prev.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
