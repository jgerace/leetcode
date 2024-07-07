"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visit_island(grid: List[List[str]], row: int, col: int):
            row_idx = row
            col_idx = col
            num_rows = len(grid)
            num_cols = len(grid[0])
            if grid[row_idx][col_idx] == "1":
                grid[row_idx][col_idx] = "0"

            if row_idx > 0 and grid[row_idx-1][col_idx] == "1":
                # up
                visit_island(grid, row_idx - 1, col_idx)
            if row_idx < num_rows - 1 and grid[row_idx+1][col_idx] == "1":
                # down
                visit_island(grid, row_idx + 1, col_idx)
            if col_idx > 0 and grid[row_idx][col_idx-1] == "1":
                # left
                visit_island(grid, row_idx, col_idx - 1)
            if col_idx < num_cols - 1 and grid[row_idx][col_idx+1] == "1":
                # right
                visit_island(grid, row_idx, col_idx + 1)

        num_islands = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                if grid[row_idx][col_idx] == "1":
                    visit_island(grid, row_idx, col_idx)
                    num_islands += 1
        return num_islands


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    output = Solution().numIslands(grid)
    assert output == 1

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    output = Solution().numIslands(grid)
    assert output == 3

    grid = [
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    output = Solution().numIslands(grid)
    assert output == 0

    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"]
    ]
    output = Solution().numIslands(grid)
    assert output == 1
