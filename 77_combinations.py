"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:

    1 <= n <= 20
    1 <= k <= n
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def helper(start: int, input: List[int]):
            if len(input) == k:
                result.append(input.copy())
                return
            # input is a list of integers that begin with the value start
            # each instance of this list is a mutable combination that will be modified and
            # subsequently added to the result set if the length is correct
            # ex: [1] -> [1, 2] -> add to result if k == 2, then pop the 2 off and iterate to [1, 3]
            for idx in range(start, n+1):
                input.append(idx)
                helper(idx+1, input)
                input.pop()

        helper(1, [])

        return result


if __name__ == "__main__":
    output = Solution().combine(4, 2)
    print(output)
    assert output == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

    output = Solution().combine(1, 1)
    assert output == [[1]]
