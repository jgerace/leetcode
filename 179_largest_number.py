"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 10^9
"""
import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(compare))
        result = "".join(nums)
        if result[0] == "0":
            return "0"
        return result


if __name__ == "__main__":
    output = Solution().largestNumber(nums=[10, 2])
    assert output == "210"

    output = Solution().largestNumber(nums=[3, 30, 34, 5, 9])
    assert output == "9534330"

    output = Solution().largestNumber(nums=[34323, 3432])
    assert output == "343234323"
