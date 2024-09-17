"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])
        seen = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        print("*****")

        def dfs(start_row: int, start_col: int, cur_word: str) -> bool:
            if cur_word == word:
                return True
            if (start_row >= num_rows or
                    start_col >= num_cols or
                    start_row < 0 or
                    start_col < 0 or
                    seen[start_row][start_col]):
                return False
            if cur_word and cur_word[-1] != word[len(cur_word)-1]:
                return False
            print("  row:", start_row, "col:", start_col, "cur_word:", cur_word)

            seen[start_row][start_col] = True
            for drow, dcol in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                result = dfs(start_row + drow, start_col + dcol, cur_word + board[start_row][start_col])
                if result:
                    return result
            seen[start_row][start_col] = False
            return False

        for idx_row in range(num_rows):
            for idx_col in range(num_cols):
                if board[idx_row][idx_col] == word[0]:
                    print("starting dfs on", idx_row, idx_col)
                    result = dfs(idx_row, idx_col, f"")
                    if result:
                        return True

        return False


if __name__ == "__main__":
    output = Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                              word="ABCCED")
    assert output is True

    output = Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                              word="SEE")
    assert output is True

    output = Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                              word="ABCB")
    assert output is False
