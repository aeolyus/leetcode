from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]
        j = 1
        for i in range(len(nums)):
            result[i] *= j
            j *= nums[i]

        j = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= j
            j *= nums[i]

        return result
