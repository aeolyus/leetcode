from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        writeIdx = 0
        last = float('inf')
        while i < len(nums):
            num = nums[i]
            if last != num:
                nums[writeIdx] = num
                writeIdx += 1
            last = num
            i += 1
        return writeIdx
