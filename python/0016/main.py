from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest = float('inf')
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(target - s) < abs(target - closest):
                    closest = s
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    return s
        return closest
