class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n > 0:
            i = n//5
            result += i
            n = i
        return result
