from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            lo_num = nums[lo]
            hi_num = nums[hi]
            mid = (lo + hi) // 2
            mid_num = nums[mid]
            if mid_num > hi_num:
                lo = mid + 1
            elif mid_num < lo_num:
                hi = mid
            else:
                return min(lo_num, hi_num)
        return nums[lo]
