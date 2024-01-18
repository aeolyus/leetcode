from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        curr = 0
        for i in nums:
            curr = max(i, curr + i)
            result = max(result, curr)
        return result
