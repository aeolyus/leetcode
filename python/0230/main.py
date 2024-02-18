from typing import Optional
from python.lib.tree import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        stack = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
