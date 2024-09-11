"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:

    1 <= nums.length <= 8
    -10 <= nums[i] <= 10
"""
from collections import Counter
from typing import List

from testing import listItemsEqual


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        max_len = len(nums)
        counter = Counter(nums)

        def helper(items: List[int]):
            if len(items) == max_len:
                result.append(items)
                return
            for num in counter:
                if counter[num]:
                    counter[num] -= 1
                    helper(items + [num])
                    counter[num] += 1

        helper([])
        return result


if __name__ == "__main__":
    output = Solution().permuteUnique([1, 1, 2])
    assert listItemsEqual(output, [[1, 1, 2], [1, 2, 1], [2, 1, 1]])

    output = Solution().permuteUnique([1, 2, 3])
    assert listItemsEqual(output, [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
