from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            d = self.dist_sq(p)
            heap.append((d, p))
        heapq.heapify(heap)

        result = []
        for i in range(k):
            d, p = heapq.heappop(heap)
            result.append(p)
        return result

    def dist_sq(self, point: List[int]) -> float:
        x, y = point
        return x**2 + y**2
