from typing import List
from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] -= 1

        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
