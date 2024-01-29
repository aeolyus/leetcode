from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        n = 0
        s = len(matrix) - 1
        w = 0
        e = len(matrix[0]) - 1

        while n <= s and w <= e:
            for i in range(w, e + 1):
                result.append(matrix[n][i])
            n += 1
            for i in range(n, s + 1):
                result.append(matrix[i][e])
            e -= 1
            if n <= s:
                for i in range(e, w - 1, -1):
                    result.append(matrix[s][i])
                s -= 1
            if w <= e:
                for i in range(s, n - 1, -1):
                    result.append(matrix[i][w])
                w += 1
        return result
