"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:

    0 <= nums.length <= 20
    -2^31 <= nums[i] <= 2^31 - 1
    All the values of nums are unique.
    nums is sorted in ascending order.
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        print("*****")
        if not nums:
            return []

        nums.sort()
        ranges = []
        cur_range = [nums[0]]
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx-1] + 1:
                cur_range.append(nums[idx])
            else:
                ranges.append(cur_range)
                cur_range = [nums[idx]]
        ranges.append(cur_range)

        result = []
        for r in ranges:
            if len(r) == 1:
                result.append(str(r[0]))
            else:
                result.append(f"{r[0]}->{r[-1]}")

        print(result)
        return result


if __name__ == "__main__":
    output = Solution().summaryRanges(nums=[0, 1, 2, 4, 5, 7])
    assert output == ["0->2", "4->5", "7"]

    output = Solution().summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9])
    assert output == ["0", "2->4", "6", "8->9"]

    output = Solution().summaryRanges(nums=[])
    assert output == []
