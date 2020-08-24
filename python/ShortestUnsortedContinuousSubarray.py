from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        smallest = float("inf")
        biggest = float("-inf")

        for i, num in enumerate(nums):
            if self.outOfOrder(i, nums):
                smallest = min(smallest, num)
                biggest = max(biggest, num)
        if smallest == float("inf"):
            return 0
        smallestIdx = 0
        while nums[smallestIdx] <= smallest:
            smallestIdx += 1
        biggestIdx = len(nums) - 1
        while nums[biggestIdx] >= biggest:
            biggestIdx -= 1
        return biggestIdx - smallestIdx + 1

    def outOfOrder(self, index, nums) -> bool:
        if index == 0:
            return nums[1] < nums[index]
        if index == len(nums) - 1:
            return nums[index - 1] > nums[index]
        return nums[index] < nums[index - 1] or nums[index] > nums[index + 1]
