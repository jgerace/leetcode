"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            # Assuming that if nums = [0] and you start on the first element, then you don't need to jump
            return True

        # If you can get to the last index from any previous index, then you can jump
        # But you have to recurse through the subarray to see if you can get to that previous index, etc
        can = False
        lastIdx = len(nums) - 1
        for idx in range(lastIdx-1, -1, -1):

            if nums[idx] + idx >= lastIdx and self.canJump(nums[:idx+1]):
                can = True

        return can


if __name__ == '__main__':
    val = Solution().canJump([2, 3, 1, 1, 4])
    assert val is True

    val = Solution().canJump([3, 2, 1, 0, 4])
    assert val is False

    val = Solution().canJump([3])
    assert val is True

    val = Solution().canJump([0, 3])
    assert val is False
