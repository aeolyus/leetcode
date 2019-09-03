class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        L = 1
        R = x
        ans = 0
        while (L <= R):
            mid = (L + R)//2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                R = mid - 1
            else:
                L = mid + 1
                ans = mid
        return ans
