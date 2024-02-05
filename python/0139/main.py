from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i: j] in wordDict:
                    dp[j] = dp[i] or dp[j]
        return dp[len(s)]
