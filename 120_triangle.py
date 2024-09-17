"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:

Input: triangle = [[-10]]
Output: -10

Constraints:

    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -10^4 <= triangle[i][j] <= 10^4


Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
from typing import List


class Solution:
    def minimumTotalUnoptimized(self, triangle: List[List[int]]) -> int:
        print("*****")
        result = [triangle[row].copy() for row in range(len(triangle))]

        for idx_row in range(len(triangle) - 2, -1, -1):
            for idx_col in range(len(triangle[idx_row])):
                result[idx_row][idx_col] = min(result[idx_row+1][idx_col] + triangle[idx_row][idx_col],
                                               result[idx_row+1][idx_col+1] + triangle[idx_row][idx_col])
        print(result)

        return result[0][0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        result = triangle[-1].copy()

        for idx_row in range(len(triangle)-2, -1, -1):
            for idx_col in range(len(triangle[idx_row])):
                result[idx_col] = min(result[idx_col]+triangle[idx_row][idx_col],
                                      result[idx_col+1]+triangle[idx_row][idx_col])

        print(result)

        return result[0]


if __name__ == "__main__":
    output = Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    assert output == 11

    output = Solution().minimumTotal([[-10]])
    assert output == -10
