from typing import List
from collections import defaultdict


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums = defaultdict(lambda: 0)
        for n in nums1:
            nums[n] = 1
        for n in nums2:
            if nums[n] == 1:
                result.append(n)
                nums[n] = 0
        return result
