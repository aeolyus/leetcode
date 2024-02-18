from typing import List, Optional
from python.lib.tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        lo = 0
        hi = len(nums) - 1
        root = TreeNode()
        stack = [(root, lo, hi)]

        while stack:
            curr, lo, hi = stack.pop()
            mid = (lo + hi)//2
            curr.val = nums[mid]
            if mid - 1 >= lo:
                left = TreeNode()
                stack.append((left, lo, mid - 1))
                curr.left = left
            if mid + 1 <= hi:
                right = TreeNode()
                stack.append((right, mid + 1, hi))
                curr.right = right

        return root
