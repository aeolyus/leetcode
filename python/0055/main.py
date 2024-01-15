from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 1
        for i in nums:
            gas -= 1
            if gas < 0:
                return False
            gas = max(gas, i)
        return True
