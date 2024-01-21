from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        curr = root
        stack = []
        while curr or stack:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if prev is not None and prev >= curr.val:
                    return False
                prev = curr.val
                curr = curr.right
        return True
