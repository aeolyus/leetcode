from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for num_idx, num in enumerate(nums):
            for i in range(num_idx):
                if num > nums[i]:
                    dp[num_idx] = max(dp[num_idx], dp[i] + 1)
        return max(dp)
