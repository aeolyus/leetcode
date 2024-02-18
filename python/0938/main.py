from typing import Optional
from python.lib.tree import TreeNode


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
