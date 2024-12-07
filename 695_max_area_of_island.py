"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        print("*****")
        max_area = 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        def get_area_of_island(row_idx, col_idx) -> int:
            if grid[row_idx][col_idx] == 0:
                return 0

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
            area = 1
            grid[row_idx][col_idx] = 0  # mark this as visited
            for drow, dcol in directions:
                new_row = row_idx + drow
                new_col = col_idx + dcol
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                    area += get_area_of_island(new_row, new_col)
            return area

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    area = get_area_of_island(row, col)
                    max_area = max(max_area, area)

        print(max_area)
        return max_area


if __name__ == "__main__":
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    output = Solution().maxAreaOfIsland(grid)
    assert output == 6

    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    output = Solution().maxAreaOfIsland(grid)
    assert output == 0

    grid = [[0, 0, 0, 1, 1, 1, 0, 0]]
    output = Solution().maxAreaOfIsland(grid)
    assert output == 3
