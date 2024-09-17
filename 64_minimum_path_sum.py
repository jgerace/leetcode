"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 200
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        for idx_col in range(1, num_cols):
            grid[0][idx_col] += grid[0][idx_col-1]
        for idx_row in range(1, num_rows):
            grid[idx_row][0] += grid[idx_row-1][0]

        for idx_row in range(1, num_rows):
            for idx_col in range(1, num_cols):
                grid[idx_row][idx_col] += min(grid[idx_row-1][idx_col], grid[idx_row][idx_col-1])
        print(grid)
        return grid[-1][-1]



if __name__ == "__main__":
    output = Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    assert output == 7

    output = Solution().minPathSum([[1, 2, 3], [4, 5, 6]])
    assert output == 12
