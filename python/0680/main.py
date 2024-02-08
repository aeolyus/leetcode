class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                skip_left = s[i + 1: j + 1]
                skip_right = s[i:j]
                return (skip_left == skip_left[::-1]
                        or skip_right == skip_right[::-1])
            i += 1
            j -= 1
        return True
