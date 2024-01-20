from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = defaultdict(lambda: 0)
        for c in s:
            table[c] += 1
        for c in t:
            if c not in table:
                return False
            table[c] -= 1
        for v in table.values():
            if v != 0:
                return False
        return True
