from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map_set = [set() for _ in range(len(board))]
        col_map_set = [set() for _ in range(len(board[0]))]
        grid_map_set = [
            [set() for _ in range(len(board[0])//3)]
            for _ in range(len(board)//3)
        ]
        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val == ".":
                    continue
                if val in row_map_set[row] \
                        or val in col_map_set[col] \
                        or val in grid_map_set[row//3][col//3]:
                    return False
                row_map_set[row].add(val)
                col_map_set[col].add(val)
                grid_map_set[row//3][col//3].add(val)
        return True
