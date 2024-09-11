"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

Constraints:

    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def maximumGapWithSort(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()

        max_gap = 0
        for idx in range(len(nums)-1):
            gap = nums[idx+1] - nums[idx]
            max_gap = max(max_gap, gap)

        return max_gap

    def maximumGap(self, nums: List[int]) -> int:
        # TODO: can i do this without calling a python sort?
        return 0


if __name__ == "__main__":
    output = Solution().maximumGapWithSort([3, 6, 9, 1])
    assert output == 3

    output = Solution().maximumGapWithSort([10])
    assert output == 0
