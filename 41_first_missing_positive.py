"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:

    1 <= nums.length <= 10^5
    -2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash = [0] * len(nums)

        n = len(nums)
        for num in nums:
            if num < 1 or num > n:
                continue
            hash[num - 1] = num

        for idx in range(len(hash)):
            if hash[idx] == 0:
                return idx+1
        return n + 1


if __name__ == "__main__":
    output = Solution().firstMissingPositive([1, 2, 0])
    assert output == 3

    output = Solution().firstMissingPositive([3, 4, -1, 1])
    assert output == 2

    output = Solution().firstMissingPositive([7, 8, 9, 11, 12])
    assert output == 1

    output = Solution().firstMissingPositive([1, 2, 3])
    assert output == 4
