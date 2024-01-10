class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while (i >= 0 or j >= 0 or carry == 1):
            if i >= 0:
                carry += int(a[i] == '1')
                i -= 1
            if j >= 0:
                carry += int(b[j] == '1')
                j -= 1
            result += str(carry % 2)
            carry //= 2
        return result[::-1]
