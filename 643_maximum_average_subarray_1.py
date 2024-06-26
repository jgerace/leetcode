"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

Constraints:

    n == nums.length
    1 <= k <= n <= 10^5
    -10^4 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        last_avg = sum(nums[0:k])/k
        max_avg = last_avg
        for idx in range(1, len(nums)-k+1):
            avg = ((last_avg * k) - nums[idx-1] + nums[idx+k-1]) / k
            max_avg = max(max_avg, avg)
            last_avg = avg
        return max_avg


if __name__ == "__main__":
    output = Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4)
    assert output == 12.75

    output = Solution().findMaxAverage([5], 1)
    assert output == 5.0
