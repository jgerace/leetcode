"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2



Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1].


"""
from typing import List


class Solution:

    def jump_backwards(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        minJumps = len(nums)
        lastIdx = len(nums) - 1
        for idx in range(lastIdx - 1, -1, -1):
            jumps = 0
            if nums[idx] + idx >= lastIdx:
                jumps += 1 + self.jump(nums[:idx + 1])
                if jumps < minJumps:
                    minJumps = jumps
        return minJumps

    def jump(self, nums: List[int]) -> int:
        print("*****")
        if len(nums) == 1:
            return 0

        result = 0
        end = 0
        farthest = 0
        for idx in range(len(nums)-1):
            farthest = max(farthest, nums[idx] + idx)
            if idx == end:
                result += 1
                end = farthest
            if end >= len(nums)-1:
                break
        print(result)
        return result


if __name__ == '__main__':
    val = Solution().jump([2, 3, 1, 1, 4])
    assert val == 2

    val = Solution().jump([2, 3, 0, 1, 4])
    assert val == 2

    val = Solution().jump([3])
    assert val == 0

    val = Solution().jump([1, 3])
    assert val == 1

    val = Solution().jump(
        [5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3,
         8, 5])
    assert val == 5
