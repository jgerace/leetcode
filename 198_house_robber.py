"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 400
"""
from collections import defaultdict
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        print("*****")
        dp = defaultdict(int)

        def partition(start_idx, end_idx):
            # print(f"analyzing subarray [{start_idx}, {end_idx}]")
            if dp[(start_idx, end_idx)] or start_idx == end_idx:
                # print("  returning")
                return

            if end_idx - start_idx == 1:
                # print("  setting to", nums[start_idx])
                dp[(start_idx, end_idx)] = nums[start_idx]
                return

            max_sum = 0
            for idx in range(start_idx, end_idx):
                # print("recursing for pivot", idx)
                prev = 0
                if idx - 2 >= 0:
                    partition(start_idx, idx - 2)
                    prev = dp[(start_idx, idx - 2)]
                next = 0
                if idx + 2 < end_idx:
                    partition(idx + 2, end_idx)
                    next = dp[(idx + 2, end_idx)]

                max_sum = max(max_sum, prev + nums[idx] + next)

            # print("  setting max to", max_sum)
            dp[(start_idx, end_idx)] = max_sum

            return

        if sum(nums) == 0:
            return 0
        partition(0, len(nums))
        print(dp)
        print("result:", dp[0, len(nums)])
        return dp[0, len(nums)]


if __name__ == "__main__":
    output = Solution().rob([1, 2, 3, 1])
    assert output == 4

    output = Solution().rob([2, 7, 9, 3, 1])
    assert output == 12

    output = Solution().rob(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    assert output == 0
