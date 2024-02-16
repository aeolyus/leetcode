from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
        for n in num_set:
            if (n - 1) not in num_set:
                run = 1
                while (n + run) in num_set:
                    run += 1
                result = max(result, run)
        return result
