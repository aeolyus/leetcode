from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = len(nums) - 1
        while i < k + 1:
            if nums[i] == val:
                nums[i] = nums[k]
                nums[k] = ' '
                i -= 1
                k -= 1
            i += 1
        return i
