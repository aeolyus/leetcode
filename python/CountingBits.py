from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        result_lst = []
        for n in range(num + 1):
            result = 0
            while n:
                n &= n - 1
                result += 1
            result_lst.append(result)
        return result_lst
