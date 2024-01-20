from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        result = ""
        while True:
            prefix = None
            for s in strs:
                if i < len(s):
                    if prefix is None:
                        prefix = s[i]
                    elif prefix != s[i]:
                        return result
                else:
                    return result
            result += prefix
            i += 1
        return result
