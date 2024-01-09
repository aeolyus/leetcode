from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = float('inf')
        for price in prices:
            if price > buy:
                result += price - buy
            buy = price
        return result
