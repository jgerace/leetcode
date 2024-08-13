"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Example 1:

Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:

Input: board = [["."]]
Output: 0

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is either '.' or 'X'.

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
"""
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        num_cols = len(board[0])
        num_rows = len(board)

        ships = [[0 for col in range(num_cols)] for row in range(num_rows)]

        for col_idx in range(num_cols):
            for row_idx in range(num_rows):
                if board[row_idx][col_idx] == "X":
                    # check if you're connected to an existing ship
                    added_to_ship = False
                    for drow, dcol in [(-1, 0), (0, -1)]:
                        new_row_idx = row_idx + drow
                        new_col_idx = col_idx + dcol
                        if ships[new_row_idx][new_col_idx] > 0:
                            added_to_ship = True
                            ships[row_idx][col_idx] = ships[new_row_idx][new_col_idx]
                    if not added_to_ship:
                        count += 1
                        ships[row_idx][col_idx] = count
        return count


if __name__ == "__main__":
    board = [["X", ".", ".", "X"],
             [".", ".", ".", "X"],
             [".", ".", ".", "X"]]
    output = Solution().countBattleships(board)
    assert output == 2

    board = [["X", "X", ".", "X"],
             [".", ".", ".", "X"],
             ["X", "X", ".", "X"]]
    output = Solution().countBattleships(board)
    assert output == 3

    board = [["X", ".", ".", "X"],
             ["X", ".", ".", "X"],
             ["X", ".", ".", "X"]]
    output = Solution().countBattleships(board)
    assert output == 2

    board = [["."]]
    output = Solution().countBattleships(board)
    assert output == 0

    board = [["X"]]
    output = Solution().countBattleships(board)
    assert output == 1
