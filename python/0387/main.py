from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map = defaultdict(lambda: 0)
        for c in s:
            count_map[c] += 1
        for i, c in enumerate(s):
            if count_map[c] == 1:
                return i
        return -1
