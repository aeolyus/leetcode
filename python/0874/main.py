from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set((x, y) for x, y in obstacles)
        result = 0
        x, y = 0, 0
        dx, dy = 0, 1
        for c in commands:
            if c == -2:
                dx, dy = -dy, dx
            elif c == -1:
                dx, dy = dy, -dx
            else:
                for _ in range(c):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x, y = x + dx, y + dy
                result = max(result, x*x + y*y)
        return result
