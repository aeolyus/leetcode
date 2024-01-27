from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        stack = []
        curr = root
        while curr or stack:
            while curr:
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.right and stack and stack[-1] == curr.right:
                stack.pop()
                stack.append(curr)
                curr = curr.right
            else:
                result.append(curr.val)
                curr = None
        return result
