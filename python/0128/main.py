from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
        for n in nums:
            run = 0
            if n - 1 in num_set:
                continue
            else:
                while n in num_set:
                    run += 1
                    n += 1
                result = max(result, run)
        return result
