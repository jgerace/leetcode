"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

    Only numbers 1 through 9 are used.
    Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Constraints:

    2 <= k <= 9
    1 <= n <= 60
"""
from typing import List

from testing import listItemsEqual


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        print("*****")
        result = set()

        def helper(used_nums: set, input: List[int], remaining_sum: int) -> None:
            print(used_nums, input, remaining_sum)
            if len(input) == k and remaining_sum == 0:
                result.add(tuple(sorted(input)))
                return
            elif len(input) == k:
                return

            for num in range(1, 10):
                if num > remaining_sum or num in used_nums:
                    continue
                used_nums.add(num)
                helper(used_nums, input + [num], remaining_sum-num)
                used_nums.remove(num)

        helper(set(), [], n)
        print([list(item) for item in result])
        return [list(item) for item in result]


if __name__ == "__main__":
    output = Solution().combinationSum3(k=3, n=7)
    assert listItemsEqual(output, [[1, 2, 4]])

    output = Solution().combinationSum3(k=3, n=9)
    assert listItemsEqual(output, [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
