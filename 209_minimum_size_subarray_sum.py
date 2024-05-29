"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0



Constraints:

    1 <= target <= 10^9
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4

"""
from typing import List


class Solution:
    def savsies(self, target: int, nums: List[int]) -> int:
        print("called with", target, nums)
        for num in nums:
            if num >= target:
                return 1

        start = 0
        end = 1
        minLen = len(nums) + 1
        sum = nums[start] + nums[end]
        while start < end < len(nums):
            print("start", start, "end", end)
            if sum < target:
                end += 1
                sum += nums[end]
            elif sum >= target:
                minLen = min(minLen, end - start + 1)
                start += 1
                sum -= nums[start - 1]
            print("minLen", minLen)
        if minLen == len(nums)+1:
            return 0
        else:
            return minLen

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for num in nums:
            if num >= target:
                return 1

        start = 0
        end = 1
        minLen = len(nums) + 1
        curLen = 1
        sum = nums[start]
        while start < end < len(nums):
            if end - start + 1 > curLen:
                sum += nums[end]
            else:
                sum -= nums[start - 1]
            curLen = end - start + 1

            if sum < target:
                end += 1
            elif sum >= target:
                minLen = min(minLen, end - start + 1)
                start += 1

        if minLen == len(nums)+1:
            return 0
        else:
            return minLen


if __name__ == '__main__':
    output = Solution().minSubArrayLen(4, [4])
    assert output == 1

    output = Solution().minSubArrayLen(4, [3])
    assert output == 0

    output = Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    assert output == 2

    output = Solution().minSubArrayLen(4, [1, 4, 4])
    assert output == 1

    output = Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1])
    assert output == 0
