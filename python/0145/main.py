from typing import Optional, List
from python.lib.tree import TreeNode


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
