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
        for i, w in enumerate(self.weights):
            if n <= w:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
