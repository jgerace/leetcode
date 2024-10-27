"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:

Input: nums = [1,1,2]
Output: [1]

Example 3:

Input: nums = [1]
Output: []

Constraints:

    n == nums.length
    1 <= n <= 10^5
    1 <= nums[i] <= n
    Each element in nums appears once or twice.
"""
from collections import defaultdict
from typing import List

from testing import listItemsEqual


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return []

        result = []
        nums.sort()
        for idx in range(1, len(nums)):
            if nums[idx-1] == nums[idx]:
                result.append(nums[idx])

        return result

        # return [key for key, value in result.items() if value == 2]


if __name__ == "__main__":
    output = Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
    assert listItemsEqual(output, [2, 3])

    output = Solution().findDuplicates([1, 1, 2])
    assert listItemsEqual(output, [1])

    output = Solution().findDuplicates([1])
    assert listItemsEqual(output, [])
