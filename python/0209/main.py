from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        result = len(nums) + 1
        s = 0
        for right, n in enumerate(nums):
            s += n
            while left <= right and s >= target:
                result = min(result, right - left + 1)
                s -= nums[left]
                left += 1
        if result >= len(nums) + 1:
            return 0
        return result
