from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float("-inf")
        currMax = 1
        currMin = 1
        for n in nums:
            oldMax = currMax
            currMax = max(n, currMax * n, currMin * n)
            currMin = min(n, currMin * n, oldMax * n)
            result = max(result, currMax)
        return result
