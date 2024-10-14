"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]

Constraints:

    1 <= nums.length <= 5 * 10^4
    -10^9 <= nums[i] <= 10^9

Follow up: Could you solve the problem in linear time and in O(1) space?
"""
from collections import defaultdict
import math
from typing import List

from testing import listItemsEqual


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # TODO: not an O(1) space solution
        min_occurrences = math.floor(len(nums) / 3)
        occurrences = defaultdict(int)
        result = set()
        for num in nums:
            occurrences[num] += 1
            if occurrences[num] > min_occurrences:
                result.add(num)
        return list(result)


if __name__ == "__main__":
    output = Solution().majorityElement(nums=[3, 2, 3])
    assert listItemsEqual(output, [3])

    output = Solution().majorityElement(nums=[1])
    assert listItemsEqual(output, [1])

    output = Solution().majorityElement(nums=[1, 2])
    assert listItemsEqual(output, [1, 2])
