"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""
from typing import List


class Solution:
    def helper(self, startRow, startCol, endRow, endCol, matrix) -> List[int]:
        print("input:", startRow, startCol, endRow, endCol)
        output = []
        numCols = len(matrix[0])
        numRows = len(matrix)

        if startRow > endRow or startCol > endCol:
            print("returning")
            return []

        # right
        if startCol <= endCol and startCol < numCols:
            print("right")
            for colIdx in range(startCol, endCol+1):
                output.append(matrix[startRow][colIdx])

        # down
        if startRow+1 <= endRow and startRow+1 < numRows:
            print("down")
            for rowIdx in range(startRow+1, endRow+1):
                output.append(matrix[rowIdx][endCol])

        # left
        if startRow < endRow and endCol-1 >= startCol:
            print("left")
            for colIdx in range(endCol-1, startCol-1, -1):
                output.append(matrix[endRow][colIdx])

        # up - not including startRow since we already did that in the RIGHT section
        if startRow+1 < endRow and startCol < endCol and startRow+1 < numRows:
            print("up")
            for rowIdx in range(endRow-1, startRow, -1):
                output.append(matrix[rowIdx][startCol])

        output.extend(self.helper(startRow+1, startCol+1, endRow-1, endCol-1, matrix))

        return output

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = self.helper(0, 0, len(matrix)-1, len(matrix[0])-1, matrix)
        print(output)
        return output


if __name__ == '__main__':
    output = Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert output == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    output = Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    assert output == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    output = Solution().spiralOrder([[1, 2, 3], [4, 5, 6]])
    assert output == [1, 2, 3, 6, 5, 4]

    output = Solution().spiralOrder([[1, 2], [3, 4], [5, 6]])
    assert output == [1, 2, 4, 6, 5, 3]

    output = Solution().spiralOrder([[1, 2, 3, 4]])
    assert output == [1, 2, 3, 4]

    output = Solution().spiralOrder([[1], [2], [3], [4]])
    assert output == [1, 2, 3, 4]

    output = Solution().spiralOrder([[1]])
    assert output == [1]
