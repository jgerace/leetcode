"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]

Constraints:

    0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""
from typing import List


class Solution:
    """
           1
         1  1
        1  2  1
       1  3  3  1
      1  4  6  4  1
     1  5 10 10  5  1
    1 6  15 20 15 6  1
    """
    def getRow(self, rowIndex: int) -> List[int]:
        result = []

        # TODO
        
        return result

    def getRowUnoptimized(self, rowIndex: int) -> List[int]:
        result = []
        len_row = 1

        for row in range(rowIndex+1):
            row_result = []
            for col in range(len_row):
                if col == 0 or col == len_row - 1:
                    row_result.append(1)
                else:
                    row_result.append(result[row - 1][col] + result[row - 1][col - 1])
            result.append(row_result)
            len_row += 1

        print(result)
        return result[rowIndex]


if __name__ == "__main__":
    output = Solution().getRow(3)
    assert output == [1, 3, 3, 1]

    output = Solution().getRow(0)
    assert output == [1]

    output = Solution().getRow(1)
    assert output == [1, 1]

    output = Solution().getRow(4)
    assert output == [1, 4, 6, 4, 1]

    output = Solution().getRow(5)
    assert output == [1, 5, 10, 10, 5, 1]
