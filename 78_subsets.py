"""
Given an integer array nums of unique elements, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
"""
from typing import List

from testing import listItemsEqual


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        print("*****")

        def helper(start: int, input: List[int]):
            print("  input:", input)
            result.append(input)
            for idx in range(start, len(nums)):
                helper(idx+1, input + [nums[idx]])

        helper(0, [])
        print(result)
        return result


if __name__ == "__main__":
    output = Solution().subsets([1, 2, 3])
    assert listItemsEqual(output, [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    output = Solution().subsets([0])
    assert listItemsEqual(output, [[], [0]])
