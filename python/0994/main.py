from typing import List
from collections import defaultdict


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = defaultdict(lambda: float("inf"))
        oranges = 0
        stack = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    oranges += 1
                elif grid[row][col] == 2:
                    oranges += 1
                    stack.append((row, col))
                    seen[(row, col)] = 0

        def valid(coord: tuple[int, int]):
            row, col = coord
            return 0 <= row < len(grid) \
                and 0 <= col < len(grid[0]) \
                and grid[row][col] in [1, 2]

        while stack:
            coord = stack.pop()
            row, col = coord
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                continue
            minute = seen[coord]
            up = (row - 1, col)
            down = (row + 1, col)
            right = (row, col + 1)
            left = (row, col - 1)
            for new in [up, down, right, left]:
                if valid(new):
                    if seen[new] > minute + 1:
                        seen[new] = minute + 1
                        stack.append(new)
        if len(seen) < oranges:
            return -1
        else:
            return max(seen.values(), default=0)
