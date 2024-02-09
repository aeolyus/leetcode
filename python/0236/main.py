from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
            self,
            root: TreeNode,
            p: TreeNode,
            q: TreeNode,
    ) -> TreeNode:
        def get_node_path(root: TreeNode, dest: TreeNode) -> List[TreeNode]:
            queue = [(root, [])]
            while queue:
                node, path = queue.pop(0)
                if node is None:
                    continue
                if node.val == dest.val:
                    return path + [node]
                queue.append((node.left, path + [node]))
                queue.append((node.right, path + [node]))
        p_path = get_node_path(root, p)
        q_path = get_node_path(root, q)
        lca = None
        i = 0
        while i < len(p_path) and i < len(q_path):
            if p_path[i].val == q_path[i].val:
                lca = p_path[i]
            else:
                break
            i += 1
        return lca
