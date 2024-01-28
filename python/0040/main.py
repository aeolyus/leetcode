from typing import List


class Solution:
    def combinationSum2(
            self,
            candidates: List[int],
            target: int,
    ) -> List[List[int]]:
        dp = [set() for _ in range(target + 1)]
        for c in sorted(candidates):
            for i in reversed(range(c, target + 1)):
                for seq in dp[i - c]:
                    dp[i].add(seq + (c,))
                if i == c:
                    dp[i].add((c,))
        return dp[target]
