"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        maxLen = len(nums)

        def helper(input: List[int]):
            if len(input) == maxLen:
                result.append(input.copy())

            for num in nums:
                if num in input:
                    continue
                input.append(num)
                helper(input)
                input.pop()

        helper([])

        return result


if __name__ == "__main__":
    output = Solution().permute([1, 2, 3])
    assert output == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    output = Solution().permute([0, 1])
    assert output == [[0, 1], [1, 0]]

    output = Solution().permute([1])
    assert output == [[1]]
