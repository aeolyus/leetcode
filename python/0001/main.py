from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i, n in enumerate(nums):
            map[target - n] = i
        for i, n in enumerate(nums):
            if n in map and i != map[n]:
                return [i, map[n]]
