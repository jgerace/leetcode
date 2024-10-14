"""
Given an integer array nums, find a
subarray
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:

    1 <= nums.length <= 2 * 10^4
    -10 <= nums[i] <= 10
    The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List


# TODO
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        print("*****")
        if len(nums) == 1:
            return nums[0]

        num_negatives = 0
        for num in nums:
            if num < 0:
                num_negatives += 1

        max_prod = nums[0]
        cur_prod = nums[0]
        idx = 1
        num_negatives_seen = 0
        while idx < len(nums):
            cur_num = nums[idx]
            if (nums[idx - 1] == 0 or
                    nums[idx - 1] < 0 and num_negatives % 2 == 1):
                cur_prod = cur_num
            else:
                cur_prod *= cur_num
            max_prod = max(max_prod, cur_prod)
            idx += 1

        print(max_prod)
        return max_prod


if __name__ == "__main__":
    output = Solution().maxProduct(nums=[2, 3, -2, 4])
    assert output == 6

    output = Solution().maxProduct(nums=[-2, 0, -1])
    assert output == 0

    output = Solution().maxProduct(nums=[3, -1, 4])
    assert output == 4

    output = Solution().maxProduct(nums=[-3, -1, -1])
    assert output == 3

