class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if nums:
            mid = len(nums)//2
            t = TreeNode(nums[mid])
            t.left = self.sortedArrayToBST(nums[:mid])
            t.right = self.sortedArrayToBST(nums[mid + 1:])
            return t
        return None
