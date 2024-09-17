"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:

    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1.
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])
        paths = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        hit_obstacle = False
        for col_idx in range(num_cols):
            if obstacleGrid[0][col_idx] == 1:
                hit_obstacle = True
            paths[0][col_idx] = 1 if not hit_obstacle else 0

        hit_obstacle = False
        for row_idx in range(num_rows):
            if obstacleGrid[row_idx][0] == 1:
                hit_obstacle = True
            paths[row_idx][0] = 1 if not hit_obstacle else 0

        for row_idx in range(1, num_rows):
            for col_idx in range(1, num_cols):
                if obstacleGrid[row_idx][col_idx]:
                    paths[row_idx][col_idx] = 0
                else:
                    paths[row_idx][col_idx] = paths[row_idx - 1][col_idx] + paths[row_idx][col_idx - 1]
        print(paths)
        return paths[num_rows - 1][num_cols - 1]


if __name__ == "__main__":
    output = Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    assert output == 2

    output = Solution().uniquePathsWithObstacles([[0, 1], [0, 0]])
    assert output == 1

    output = Solution().uniquePathsWithObstacles([[1, 0]])
    assert output == 0

    output = Solution().uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]])
    assert output == 0
