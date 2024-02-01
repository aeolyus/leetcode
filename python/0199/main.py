from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
