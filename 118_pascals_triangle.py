"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

Constraints:

    1 <= numRows <= 30
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        len_row = 1

        for row in range(numRows):
            row_result = []
            for col in range(len_row):
                if col == 0 or col == len_row - 1:
                    row_result.append(1)
                else:
                    row_result.append(result[row-1][col] + result[row-1][col-1])
            result.append(row_result)
            len_row += 1

        print(result)
        return result


if __name__ == "__main__":
    output = Solution().generate(5)
    assert output == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    output = Solution().generate(1)
    assert output == [[1]]
