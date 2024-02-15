class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        result = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            result += 1
        result += startValue - target
        return result
