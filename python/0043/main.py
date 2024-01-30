class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        for c in num1:
            n1 = n1 * 10 + ord(c) - ord('0')
        for c in num2:
            n2 = n2 * 10 + ord(c) - ord('0')
        return str(n1 * n2)
