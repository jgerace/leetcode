"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:

Input: citations = [1,3,1]
Output: 1

Constraints:

    n == citations.length
    1 <= n <= 5000
    0 <= citations[i] <= 1000
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxH = 0

        # For each paper, find how many other papers have >=X number of citations
        for cits in sorted(citations):

            # Number of papers with `cits` number of citations
            numPapers = 0
            for nums in citations:
                if nums >= cits:
                    numPapers += 1

            # H factor is the lesser of the two values
            if numPapers >= cits:
                h = min(numPapers, cits)
                maxH = max(maxH, h)

        return maxH


if __name__ == '__main__':
    h = Solution().hIndex([3, 0, 6, 1, 5])
    assert h == 3

    h = Solution().hIndex([1, 3, 1])
    assert h == 1

    h = Solution().hIndex([1])
    assert h == 1

    h = Solution().hIndex([3, 4, 5, 6])
    assert h == 3
