from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(lambda: 0)
        prefix_sum[0] = 1
        running_sum = 0
        result = 0
        for n in nums:
            running_sum += n
            diff = running_sum - k
            if diff in prefix_sum:
                result += prefix_sum[diff]
            prefix_sum[running_sum] += 1
        return result
