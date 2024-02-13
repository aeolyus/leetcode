from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        stack: List[int] = []
        num = 0
        prev_op = "+"
        for c in s + "+":
            if c.isdigit():
                num = 10 * num + int(c)
            elif c in "+-*/":
                if prev_op == "+":
                    stack.append(num)
                elif prev_op == "-":
                    stack.append(-num)
                elif prev_op == "*":
                    stack.append(stack.pop() * num)
                elif prev_op == "/":
                    stack.append(int(stack.pop() / num))
                prev_op = c
                num = 0
        return sum(stack)
