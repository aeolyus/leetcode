from typing import List, Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        coords = defaultdict(lambda: defaultdict(lambda: []))
        queue = [(root, 0, 0)]
        while queue:
            node, x, y = queue.pop(0)
            if node is None:
                continue
            coords[x][y].append(node.val)
            queue.append((node.right, x + 1, y + 1))
            queue.append((node.left, x - 1, y + 1))

        result = []
        for x in sorted(coords.keys()):
            curr = []
            for y in sorted(coords[x].keys()):
                curr.extend(sorted(coords[x][y]))
            result.append(curr)
        return result
