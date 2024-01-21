from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ring = 0
        n = len(matrix)
        while ring < n//2:
            for i in range(ring, n - ring - 1):
                a = matrix[ring][i]
                b = matrix[i][-ring - 1]
                c = matrix[-ring - 1][-i - 1]
                d = matrix[- i - 1][ring]

                matrix[ring][i] = d
                matrix[i][-ring - 1] = a
                matrix[-ring - 1][-i - 1] = b
                matrix[-i - 1][ring] = c

            ring += 1
