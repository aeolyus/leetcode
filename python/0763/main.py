from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        result = []
        end = 0
        i = 0
        while i < len(s):
            end = last[s[i]]
            j = i + 1
            while j < end:
                end = max(end, last[s[j]])
                j += 1
            result.append(end - i + 1)
            i = end + 1
        return result
