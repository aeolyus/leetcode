from typing import List


class Solution:
    def combinationSum(
            self,
            candidates: List[int],
            target: int,
    ) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        for c in candidates:
            for i in range(c, target + 1):
                for lst in dp[i - c]:
                    dp[i].append(lst + [c])
                if i == c:
                    dp[i].append([c])
        return dp[target]
