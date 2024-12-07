"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cur = 0
        end = len(nums) - 1  # last element of regular numbers. no iterating beyond here.
        while cur <= end:
            if nums[cur] == 0:
                nums.pop(cur)
                nums.append(0)
                end -= 1
                continue
            else:
                cur += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0]
    Solution().moveZeroes(nums)
    assert nums == [0]

    nums = [1]
    Solution().moveZeroes(nums)
    assert nums == [1]

    nums = [0, 1, 2, 0]
    Solution().moveZeroes(nums)
    assert nums == [1, 2, 0, 0]
