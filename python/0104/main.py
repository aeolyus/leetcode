from typing import Optional
from python.lib.tree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root, 1)]
        result = 0
        while stack:
            node, depth = stack.pop()
            result = max(result, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return result
