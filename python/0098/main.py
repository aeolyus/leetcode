from typing import Optional
from python.lib.tree import TreeNode


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
