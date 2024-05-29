'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
import math
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def majorityElementWithDict(nums: List[int]) -> int:
        # O(n) space
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for key, value in count.items():
            if value >= math.floor(len(nums)/2):
                return key

    @staticmethod
    def majorityElementWithBoyerMoore(nums: List[int]) -> int:
        # Boyer-Moore voting algorithm
        # O(1) space
        currentValue = 0
        currentInstances = 0
        for num in nums:
            if currentInstances == 0:
                currentValue = num
            if currentValue != num:
                currentInstances -= 1
            else:
                currentInstances += 1
        return currentValue


if __name__ == '__main__':
    val = Solution.majorityElementWithBoyerMoore([3, 2, 3])
    assert val == 3

    val = Solution.majorityElementWithBoyerMoore([2, 2, 1, 1, 1, 2, 2])
    assert val == 2
