from typing import Optional, List
from python.lib.tree import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            for n in [node.right, node.left]:
                if n:
                    stack.append(n)
        return result
