"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

    1 <= k <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""
import heapq
from typing import List


class Solution:
    # TODO: Use quick select algo instead
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[k-1]


if __name__ == "__main__":
    output = Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
    assert output == 5

    output = Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    assert output == 4
