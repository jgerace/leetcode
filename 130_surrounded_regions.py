"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

    Connect: A cell is connected to adjacent cells horizontally or vertically.
    Region: To form a region connect every 'O' cell.
    Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.

A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        print("*****")

        def mark_uncapturable_region(board: List[List[str]], row: int, col: int):
            num_rows = len(board)
            num_cols = len(board[0])

            board[row][col] = "."

            for drow, dcol in (1, 0), (-1, 0), (0, -1), (0, 1):
                new_row = row + drow
                new_col = col + dcol
                if (0 <= new_row < num_rows and
                        0 <= new_col < num_cols and
                        board[new_row][new_col] == "O"):
                    mark_uncapturable_region(board, new_row, new_col)

        num_rows = len(board)
        num_cols = len(board[0])
        for row in (0, num_rows-1):
            for col in range(num_cols):
                if board[row][col] == "O":
                    mark_uncapturable_region(board, row, col)

        for col in (0, num_cols-1):
            for row in range(num_rows):
                if board[row][col] == "O":
                    mark_uncapturable_region(board, row, col)

        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == ".":
                    board[row][col] = "O"
        print(board)


if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]]
    Solution().solve(board)
    assert board == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]]

    board = [["X"]]
    Solution().solve(board)
    assert board == [["X"]]

    board = [["O"]]
    Solution().solve(board)
    assert board == [["O"]]

    board = [
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"]]
    Solution().solve(board)
    assert board == [
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"]]

    board = [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]]
    Solution().solve(board)
    assert board == [
        ["O", "X", "X", "O", "X"],
        ["X", "X", "X", "X", "O"],
        ["X", "X", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]]

    board = [
        ["O", "O", "O", "O", "X", "X"],
        ["O", "O", "O", "O", "O", "O"],
        ["O", "X", "O", "X", "O", "O"],
        ["O", "X", "O", "O", "X", "O"],
        ["O", "X", "O", "X", "O", "O"],
        ["O", "X", "O", "O", "O", "O"]]
    Solution().solve(board)
    assert board == [
        ["O", "O", "O", "O", "X", "X"],
        ["O", "O", "O", "O", "O", "O"],
        ["O", "X", "O", "X", "O", "O"],
        ["O", "X", "O", "O", "X", "O"],
        ["O", "X", "O", "X", "O", "O"],
        ["O", "X", "O", "O", "O", "O"]]
