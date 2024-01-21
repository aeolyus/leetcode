from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 == 1:
            return False

        target = total // 2
        dp = [[False for _ in range(target + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        for i in range(n):
            for j in range(target + 1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i]:
                    dp[i][j] |= dp[i-1][j - nums[i]]
        return dp[n-1][target]
