"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = []
        zero_cols = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows.append(row)
                    zero_cols.append(col)

        for row in zero_rows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0

        for row in range(len(matrix)):
            for col in zero_cols:
                matrix[row][col] = 0

        print(matrix)


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    matrix = [[1]]
    Solution().setZeroes(matrix)
    assert matrix == [[1]]

    matrix = [[0]]
    Solution().setZeroes(matrix)
    assert matrix == [[0]]
