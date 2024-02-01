from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        result = 0

        def mark_island(row: int, col: int):
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                if (r, c) in seen:
                    continue
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    if grid[r][c] == "1":
                        stack.extend([
                            (r + 1, c),
                            (r - 1, c),
                            (r, c + 1),
                            (r, c - 1),
                        ])
                    seen.add((r, c))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                coord = (row, col)
                if coord in seen:
                    continue
                if grid[row][col] == "0":
                    seen.add(coord)
                    continue
                mark_island(row, col)
                result += 1

        return result
