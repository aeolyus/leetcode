class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        current = 0
        last_word = False
        for c in s[::-1]:
            if c.isalpha():
                last_word = True
                current += 1
            else:
                if last_word:
                    return current
        return current
