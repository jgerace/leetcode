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

    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            # Assuming that if nums = [0] and you start on the first element, then you don't need to jump
            return True

        # If you can get to the last index from any previous index, then you can jump
        # The greedy thing to do is to iterate backwards and find the first index that allows
        # you to jump to the last index. Then see if you can jump to that previous index, etc.
        last_idx = len(nums) - 1
        previous_idx = last_idx - 1
        while previous_idx >= 0:
            if nums[previous_idx] + previous_idx >= last_idx:
                last_idx = previous_idx
            previous_idx -= 1

        if last_idx <= 0:
            return True

        return False


if __name__ == '__main__':
    val = Solution().canJump([2, 3, 1, 1, 4])
    assert val is True

    val = Solution().canJump([3, 2, 1, 0, 4])
    assert val is False

    val = Solution().canJump([3])
    assert val is True

    val = Solution().canJump([0, 3])
    assert val is False

    val = Solution().canJump(
        [2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0,
         0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0,
         7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6])
    assert val is False
