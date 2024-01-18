class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        for c in t:
            if si >= len(s):
                return True
            elif s[si] == c:
                si += 1
        if si >= len(s):
            return True
        return False
