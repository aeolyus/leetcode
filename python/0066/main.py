from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            n = digits[i]
            if i == len(digits) - 1:
                n += 1
            n += carry
            carry = n//10
            n = n % 10
            digits[i] = n
        if carry > 0:
            digits = [carry] + digits
        return digits
