from typing import Optional
from collections import defaultdict
from python.lib.tree import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root, False)]
        values = defaultdict(lambda: 0)
        result = float("-inf")
        while stack:
            node, seen = stack.pop()
            if node is None:
                continue
            if not seen:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
            else:
                left = values[node.left]
                right = values[node.right]
                v = max(left, right, 0) + node.val
                values[node] = v
                result = max(
                    result,
                    left + node.val + right,
                    left + node.val,
                    right + node.val,
                    node.val)
        return result
