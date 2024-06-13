"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums contains distinct values sorted in ascending order.
    -10^4 <= target <= 10^4
"""
import math
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        print("nums", nums, "target", target)
        start = 0
        end = len(nums) - 1

        while start <= end:
            idx = math.floor((end + start) / 2)
            print("start", start, "end", end, "idx", idx)
            if target == nums[idx]:
                return idx
            elif target < nums[idx]:
                end = idx - 1
            else:
                start = idx + 1

        return start


if __name__ == "__main__":
    output = Solution().searchInsert([1, 3, 5, 6], 5)
    assert output == 2

    output = Solution().searchInsert([1, 3, 5, 6], 2)
    assert output == 1

    output = Solution().searchInsert([1, 3, 5, 6], 7)
    assert output == 4

    output = Solution().searchInsert([1], 0)
    assert output == 0

    output = Solution().searchInsert([1, 3], 2)
    assert output == 1
