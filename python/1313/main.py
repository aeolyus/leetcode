from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            count = nums[i]
            n = nums[i + 1]
            result.extend([n]*count)
        return result
