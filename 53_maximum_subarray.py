"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_sum = nums[0]
        current_sum = nums[0] if nums[0] > 0 else 0
        for idx in range(1, len(nums)):
            current_sum += nums[idx]
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0

        return max_sum


if __name__ == "__main__":
    output = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert output == 6

    output = Solution().maxSubArray([1])
    assert output == 1

    output = Solution().maxSubArray([5, 4, -1, 7, 8])
    assert output == 23
