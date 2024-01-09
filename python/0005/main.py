class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        # Odd
        for center in range(0, len(s)):
            if len(result) < 1:
                result = s[center]
            left = center - 1
            right = center + 1
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right] and right - left + 1 > len(result):
                    result = s[left:right + 1]
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
        # Even
        for center in range(0, len(s) - 1):
            if s[center] != s[center + 1]:
                continue
            if len(result) < 2:
                result = s[center:center+2]
            left = center - 1
            right = center + 2
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right] and right - left + 1 > len(result):
                    result = s[left:right + 1]
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1

        return result
