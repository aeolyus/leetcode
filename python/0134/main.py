from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        result = 0
        fuel = 0
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                result = i + 1
                fuel = 0
        return result
