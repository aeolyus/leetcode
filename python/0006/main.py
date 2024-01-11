class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows > len(s) or numRows == 1:
            return s
        rows = ["" for _ in range(numRows)]
        i = 0
        step = -1
        for c in s:
            rows[i] += c
            if i == 0 or i == numRows - 1:
                step *= -1
            i += step
        return "".join(rows)
