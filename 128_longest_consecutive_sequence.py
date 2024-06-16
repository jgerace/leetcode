"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashed_nums = set(nums)

        max_len = 0
        for num in hashed_nums:
            # is this number in the middle of an existing sequence? if yes, we don't need
            # to look at the length
            if num - 1 in hashed_nums:
                continue
            # treat this number as the beginning of a new sequence and find out how long it is
            temp_num = num
            cur_len = 0
            while temp_num in hashed_nums:
                cur_len += 1
                temp_num += 1
            max_len = max(max_len, cur_len)

        return max_len


if __name__ == "__main__":
    output = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
    assert output == 4

    output = Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    assert output == 9

    output = Solution().longestConsecutive([0])
    assert output == 1

    output = Solution().longestConsecutive([100, 400, 200, 1, 5, 7])
    assert output == 1

    output = Solution().longestConsecutive([100, 4, 1, 1, 3, 2])
    assert output == 4

    output = Solution().longestConsecutive([1, 1, 1, 1])
    assert output == 1
