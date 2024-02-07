from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [(0, 0, "")]
        while stack:
            left, right, curr = stack.pop()
            if len(curr) == 2*n:
                result.append(curr)
            if left < n:
                stack.append((left + 1, right, curr + "("))
            if right < left:
                stack.append((left, right + 1, curr + ")"))
        return result
