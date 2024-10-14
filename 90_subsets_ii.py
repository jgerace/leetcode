"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
"""
from typing import List

from testing import listItemsEqual


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        print("*****")
        nums.sort()
        result = []
        seen = set()

        def helper(start: int, input: List[int]):
            if tuple(input) not in seen:
                result.append(input)
                seen.add(tuple(input))
            for idx in range(start, len(nums)):
                helper(idx + 1, input + [nums[idx]])

        helper(0, [])
        print(result)
        return result


if __name__ == "__main__":
    output = Solution().subsetsWithDup([1, 2, 2])
    assert listItemsEqual(output, [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])

    output = Solution().subsetsWithDup([0])
    assert listItemsEqual(output, [[], [0]])

    output = Solution().subsetsWithDup([4, 4, 4, 1, 4])
    assert listItemsEqual(output, [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4],
                                   [4, 4, 4, 4]])
