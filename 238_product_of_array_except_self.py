"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
from typing import List


class Solution:

    def solutionONSquared(self, nums: List[int]) -> List[int]:
        # O(n^2) - not the required time complexity, but space is O(1) (space comp doesn't include output space)
        return [self.multiplier(idx, nums) for idx in range(len(nums))]

    def multiplier(self, exceptionIdx: int, nums: List[int]) -> int:
        product = 1
        for idx in range(len(nums)):
            if idx != exceptionIdx:
                product *= nums[idx]
        return product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]  # product of all nums of index < idx
        for idx in range(1, len(nums)):
            prefixes.append(prefixes[idx-1] * nums[idx-1])

        suffixes = [1]  # product of all nums of index > idx
        for idx in range(len(nums)-2, -1, -1):
            suffixes.insert(0, suffixes[0] * nums[idx+1])

        return [prefixes[idx] * suffixes[idx] for idx in range(len(nums))]


if __name__ == '__main__':
    output = Solution().productExceptSelf([1, 2, 3, 4])
    assert output == [24, 12, 8, 6]

    output = Solution().productExceptSelf([-1, 1, 0, -3, 3])
    assert output == [0, 0, 9, 0, 0]

    output = Solution().productExceptSelf([1, 0])
    assert output == [0, 1]
