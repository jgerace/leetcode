"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
"""
from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # This organizes the letters of the string in a hash map organized by row
        # It maintains a line count in a zigzag pattern and adds chars to the map according to the
        # line it's supposed to be in. Then it concatenates each line and returns the
        # resulting string
        sList = list(s)
        sMap = defaultdict(str)

        ascending = True
        line = 1
        strIdx = 0
        while strIdx < len(sList):
            sMap[line] += sList[strIdx]
            if ascending and line < numRows:
                line += 1
            elif ascending and line == numRows:
                ascending = False
                line -= 1
            elif not ascending and line > 1:
                line -= 1
            elif not ascending and line == 1:
                ascending = True
                line += 1
            strIdx += 1

        outStr = ""
        for v in sMap.values():
            outStr += v
        return outStr


if __name__ == '__main__':
    output = Solution().convert("PAYPALISHIRING", 3)
    assert output == "PAHNAPLSIIGYIR"

    output = Solution().convert("PAYPALISHIRING", 4)
    assert output == "PINALSIGYAHRPI"

    output = Solution().convert("A", 1)
    assert output == "A"
