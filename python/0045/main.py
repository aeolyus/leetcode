from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        farthest = 0
        end = 0
        N = len(nums) - 1
        if N + 1 <= 1:
            return 0
        for i, n in enumerate(nums):
            farthest = max(farthest, i + n)
            if farthest >= N:
                result += 1
                return result
            if i == end:
                result += 1
                end = farthest
        return result
