from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lo = len(nums) - 1
        hi = 0

        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                lo = min(lo, stack.pop())
            stack.append(i)

        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                hi = max(hi, stack.pop())
            stack.append(i)

        return 0 if lo >= hi else hi - lo + 1
