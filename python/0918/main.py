from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        currMax = 0
        globalMax = float('-inf')
        currMin = 0
        globalMin = float('inf')
        for i in nums:
            total += i
            currMax = max(i, currMax + i)
            globalMax = max(globalMax, currMax)
            currMin = min(i, currMin + i)
            globalMin = min(globalMin, currMin)
        return max(globalMax, total - globalMin) \
            if globalMax > 0 else globalMax
