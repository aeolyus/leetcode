class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            r = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26
            result += chr(ord("A") + r)
        return result[::-1]
