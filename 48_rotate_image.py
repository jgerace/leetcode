"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
"""
import math
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(matrix: List[List[int]]) -> None:
            # swap row/col
            for row in range(len(matrix)):
                for col in range(row, len(matrix)):
                    temp = matrix[row][col]
                    matrix[row][col] = matrix[col][row]
                    matrix[col][row] = temp

        def reflect(matrix: List[List[int]]) -> None:
            # mirror across vertical midpoint
            n = len(matrix) - 1
            for row in range(n+1):
                for col in range(math.ceil(n/2)):
                    new_col = n - col
                    temp = matrix[row][col]
                    matrix[row][col] = matrix[row][new_col]
                    matrix[row][new_col] = temp

        transpose(matrix)
        reflect(matrix)


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution().rotate(matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    matrix = [[1, 2], [3, 4]]
    Solution().rotate(matrix)
    assert matrix == [[3, 1], [4, 2]]
