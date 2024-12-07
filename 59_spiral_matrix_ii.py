"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]

Constraints:

    1 <= n <= 20
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]

        def helper(start_idx, start_row, start_col, end_row, end_col):
            if start_row > end_row or start_col > end_col:
                return

            idx = start_idx
            for col in range(start_col, end_col + 1):
                result[start_row][col] = idx
                idx += 1
            for row in range(start_row+1, end_row + 1):
                result[row][end_col] = idx
                idx += 1
            for col in range(end_col - 1, start_col - 1, -1):
                result[end_row][col] = idx
                idx += 1
            for row in range(end_row - 1, start_row, -1):
                result[row][start_col] = idx
                idx += 1

            helper(idx, start_row + 1, start_col + 1, end_row - 1, end_col - 1)

        helper(1, 0, 0, n - 1, n - 1)
        print(result)
        return result


if __name__ == "__main__":
    output = Solution().generateMatrix(3)
    assert output == [[1, 2, 3],
                      [8, 9, 4],
                      [7, 6, 5]]

    output = Solution().generateMatrix(4)
    assert output == [[1,  2,  3,  4],
                      [12, 13, 14, 5],
                      [11, 16, 15, 6],
                      [10,  9,  8, 7]]

    output = Solution().generateMatrix(1)
    assert output == [[1]]
