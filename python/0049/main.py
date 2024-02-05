from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(lambda: [])
        for s in strs:
            sorted_s = tuple(sorted(s))
            result[sorted_s].append(s)
        return result.values()
