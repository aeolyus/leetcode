class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) ^ (divisor < 0)
        sign = -1 if sign else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        i = len(range(0, dividend - divisor + 1, divisor))
        result = i * sign
        return min(max(result, -2**31), 2**31 - 1)
