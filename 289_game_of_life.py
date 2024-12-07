"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 25
    board[i][j] is 0 or 1.

Follow up:

    Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        num_rows = len(board)
        num_cols = len(board[0])

        def count_live_neighbors(r, c):
            live_neighbors = 0
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 1), (1, 0), (1, -1)]:
                new_row = r + dr
                new_col = c + dc
                if 0 <= new_row <= num_rows-1 and 0 <= new_col <= num_cols-1:
                    if board[new_row][new_col]:
                        live_neighbors += 1
            return live_neighbors

        future = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        print(future)
        for row in range(num_rows):
            for col in range(num_cols):
                live_neighbors = count_live_neighbors(row, col)
                print(f"{row} {col} has {live_neighbors} live neighbors")
                if board[row][col]:  # live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        print("  dying")
                        future[row][col] = 0
                    else:
                        print("  continuing")
                        future[row][col] = 1
                else:  # dead cell
                    if live_neighbors == 3:
                        print("  reviving!")
                        future[row][col] = 1
                    else:
                        print("  still dead")
                        future[row][col] = 0
                print("  ", future)

        for row in range(num_rows):
            for col in range(num_cols):
                board[row][col] = future[row][col]


if __name__ == "__main__":
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution().gameOfLife(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    board = [[1, 1], [1, 0]]
    Solution().gameOfLife(board)
    assert board == [[1, 1], [1, 1]]
