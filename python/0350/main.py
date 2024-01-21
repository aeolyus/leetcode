from typing import List
from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1_map = defaultdict(lambda: 0)
        nums2_map = defaultdict(lambda: 0)
        for n in nums1:
            nums1_map[n] += 1
        for n in nums2:
            nums2_map[n] += 1
        for n in nums2:
            count = min(nums1_map[n], nums2_map[n])
            result.extend([n] * count)
            nums2_map[n] = 0
        return result
