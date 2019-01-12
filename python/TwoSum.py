class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comp = {}
        le = len(nums)
        for i in range(le):
            j = target - nums[i]
            if j in comp:
                return [comp[j], i]
            else:
                comp[nums[i]]= i
