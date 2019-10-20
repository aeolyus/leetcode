class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def helper(arr, n, target):
            memo = [[False for i in range(target + 1)] for j in range(n + 1)]
            for i in range(n + 1):
                memo[i][0] = True
            for i in range(1, n + 1):
                for j in range(1, target + 1):
                    if arr[i - 1] > j:
                        memo[i][j] = memo[i - 1][j]
                    else:
                        memo[i][j] = memo[i - 1][j] or memo[i - 1][j - arr[i - 1]]
            return memo[n][target]
        return not (sum(nums) & 1) and helper(nums, len(nums), sum(nums)//2)
