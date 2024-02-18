from typing import Optional
from python.lib.tree import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        count = 0
        queue = [root]
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    return count + 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count += 1
