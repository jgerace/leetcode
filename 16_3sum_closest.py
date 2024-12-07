"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:

    3 <= nums.length <= 500
    -1000 <= nums[i] <= 1000
    -10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        print("*****")
        nums.sort()
        min_diff = abs(sum(nums[:3]) - target)
        result = sum(nums[:3])

        for ii in range(len(nums)-2):
            if ii > 0 and nums[ii] == nums[ii - 1]:
                continue
            jj = ii + 1
            kk = len(nums) - 1
            while jj < kk:
                total = nums[ii] + nums[jj] + nums[kk]
                diff = abs(total - target)
                if diff < min_diff:
                    min_diff = diff
                    result = total
                    print("found min of", abs(total - target), ":", nums[ii], nums[jj], nums[kk])
                if total > target:
                    kk -= 1
                elif total < target:
                    jj += 1
                else:
                    break

        print(result)
        return result


if __name__ == "__main__":
    output = Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1)
    assert output == 2

    output = Solution().threeSumClosest(nums=[0, 0, 0], target=1)
    assert output == 0

    output = Solution().threeSumClosest(nums=[0, 1, 2], target=3)
    assert output == 3

    output = Solution().threeSumClosest(nums=[0, 1, 2], target=0)
    assert output == 3

    output = Solution().threeSumClosest(nums=[1,1,1,0], target=100)
    assert output == 3
