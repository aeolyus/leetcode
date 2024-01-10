class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        seen = False
        sign = 0

        for c in s:
            if c.isdigit():
                seen = True
                result = result*10 + int(c)
            else:
                if sign != 0 or seen:
                    break
                else:
                    if sign == 0 and c == "-":
                        sign = -1
                    elif sign == 0 and c == "+":
                        sign = 1
                    elif c.isspace():
                        continue
                    else:
                        return 0
        if sign == 0:
            sign = 1
        return max(-2**31, min(2**31 - 1, result * sign))
