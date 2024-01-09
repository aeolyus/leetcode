from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            if count == 0 and result != num:
                result = num
            elif result != num:
                count -= 1
            elif result == num:
                count += 1
        return result
