class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        begin = 0
        seen = dict()
        for i, ch in enumerate(s):
            if ch in seen and seen[ch] >= begin:
                begin = seen[ch] + 1
            else:
                result = max(result, i - begin + 1)
            seen[ch] = i
        return result
