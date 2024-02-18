from typing import Optional, List
from python.lib.tree import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [(root, 0)]
        result = []
        depth = 0
        if root is None:
            return result
        while queue:
            node, level = queue.pop(0)
            if node is None:
                continue
            if level == depth:
                result.append(node.val)
                depth += 1
            queue.extend([(node.right, level + 1), (node.left, level + 1)])

        return result
