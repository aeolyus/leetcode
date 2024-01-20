from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for rowNum in range(numRows):
            row = []
            for i in range(rowNum + 1):
                if rowNum - 1 >= 0 and i - 1 >= 0 and i < rowNum:
                    row.append(result[rowNum-1][i - 1] + result[rowNum - 1][i])
                else:
                    row.append(1)
            result.append(row)
        return result
