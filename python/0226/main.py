from typing import Optional
from python.lib.tree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            node.left, node.right = node.right, node.left
            stack.extend([node.left, node.right])
        return root
