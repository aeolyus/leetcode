from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        while count < len(nums):
            new_num = nums[i]
            j = (i + k) % len(nums)
            while j != i:
                old_num = nums[j]
                nums[j] = new_num
                new_num = old_num
                j = (j + k) % len(nums)
                count += 1
            if j == i:
                nums[i] = new_num
                count += 1
            i += 1
