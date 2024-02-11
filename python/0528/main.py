from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        curr = 0
        for weight in w:
            curr += weight
            self.weights.append(curr)
        self.total = curr

    def pickIndex(self) -> int:
        n = random.randint(1, self.total)
        return self.bin_search(self.weights, n)

    def bin_search(self, arr: List[int], k) -> int:
        lo = 0
        hi = len(arr) - 1
        while lo < hi:
            mid = (hi + lo)//2
            if arr[mid] >= k:
                hi = mid
            else:
                lo = mid + 1
        return hi


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
