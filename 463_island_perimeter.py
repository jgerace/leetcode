"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

Input: grid = [[1]]
Output: 4

Example 3:

Input: grid = [[1,0]]
Output: 4

Constraints:

    row == grid.length
    col == grid[i].length
    1 <= row, col <= 100
    grid[i][j] is 0 or 1.
    There is exactly one island in grid.
"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        print("*****")
        num_rows = len(grid)
        num_cols = len(grid[0])

        def bfs(start_row: int, start_col: int) -> int:
            total_perim = 0
            if grid[start_row][start_col] == 1:
                # mark as seen
                grid[start_row][start_col] = -1

            deltas_row_col = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for drow, dcol in deltas_row_col:
                new_row = start_row + drow
                new_col = start_col + dcol
                if ((new_col == -1 or new_col == num_cols) or
                        (new_row == -1 or new_row == num_rows) or
                        grid[new_row][new_col] == 0):
                    # check the non-land neighbors
                    total_perim += 1
                elif grid[new_row][new_col] == 1:
                    # your neighbor is land. find the perimeter for all connected land
                    perim = bfs(new_row, new_col)
                    total_perim += perim

            return total_perim

        result = 0
        for idx_row in range(num_rows):
            for idx_col in range(num_cols):
                if grid[idx_row][idx_col] == 1:
                    result = bfs(idx_row, idx_col)
                    break
        print(result)
        return result


if __name__ == "__main__":
    output = Solution().islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
    assert output == 16

    output = Solution().islandPerimeter(grid=[[1]])
    assert output == 4

    output = Solution().islandPerimeter(grid=[[1, 0]])
    assert output == 4
