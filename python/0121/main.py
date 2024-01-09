from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = float('inf')
        for price in prices:
            result = max(result, price - buy)
            buy = min(buy, price)
        return result
