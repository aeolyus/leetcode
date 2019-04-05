class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for L in enumerate(s):
            if L[1] not in chars.keys():
                chars[L[1]] = L[0]
            else:
                chars[L[1]] = -1
        res = [i for i in chars.values() if i >= 0]
        return res[0] if res else -1
