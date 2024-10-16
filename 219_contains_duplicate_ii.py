"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    0 <= k <= 10^5
"""
from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_indices = defaultdict(set)
        for idx in range(len(nums)):
            indices = num_to_indices[nums[idx]]
            if indices:
                for index in indices:
                    if abs(index - idx) <= k:
                        return True
            num_to_indices[nums[idx]].add(idx)

        return False


if __name__ == "__main__":
    output = Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3)
    assert output is True

    output = Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1)
    assert output is True

    output = Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2)
    assert output is False
