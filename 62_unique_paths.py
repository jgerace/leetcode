"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:

    1 <= m, n <= 100
"""


class Solution:
    def uniquePathsDFS(self, m: int, n: int) -> int:
        # algorithmically correct, but takes too long for relatively large m and n
        if m == 1 or n == 1:
            return 1

        down_paths = 0
        if m >= 2:
            down_paths = self.uniquePathsDFS(m-1, n)

        right_paths = 0
        if n >= 2:
            right_paths = self.uniquePathsDFS(m, n-1)

        return down_paths + right_paths

    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            matrix[row][n-1] = 1
        for col in range(n):
            matrix[m-1][col] = 1

        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                matrix[row][col] = matrix[row+1][col] + matrix[row][col+1]
        print(matrix)
        return matrix[0][0]


if __name__ == "__main__":
    output = Solution().uniquePaths(3, 7)
    assert output == 28

    output = Solution().uniquePaths(3, 2)
    assert output == 3

    output = Solution().uniquePaths(3, 1)
    assert output == 1

    output = Solution().uniquePaths(1, 3)
    assert output == 1

    output = Solution().uniquePaths(23, 12)
    assert output == 193536720
