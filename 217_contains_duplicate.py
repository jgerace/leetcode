"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]
Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def containsDuplicateWithSorting(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx-1]:
                return True
        return False


if __name__ == "__main__":
    output = Solution().containsDuplicate([1, 2, 3, 1])
    assert output is True

    output = Solution().containsDuplicate([1, 2, 3, 4])
    assert output is False

    output = Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    assert output is True
