"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

    2 <= nums.length <= 1^04
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for idx in range(len(nums)):
            table[nums[idx]] = idx

        for idx in range(len(nums)):
            idx2 = table.get(target - nums[idx])
            if idx2 and idx != idx2:
                return [idx, idx2]


if __name__ == "__main__":
    output = Solution().twoSum([2, 7, 11, 15], 9)
    assert output == [0, 1]

    output = Solution().twoSum([3, 2, 4], 6)
    assert output == [1, 2]

    output = Solution().twoSum([3, 3], 6)
    assert output == [0, 1]

    output = Solution().twoSum([1, 3, 4, 2], 6)
    assert output == [2, 3]
