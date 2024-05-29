"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:

    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.
"""
import math
from typing import List


class Solution:

    def twoSumIterative(self, numbers: List[int], target: int) -> List[int]:
        for ii in range(len(numbers) - 1):
            for jj in range(ii + 1, len(numbers)):
                if numbers[ii] + numbers[jj] == target:
                    return [ii + 1, jj + 1]

    def search(self, numbers, start, end, target) -> int:
        if end < start:
            return -1
        print("received", numbers, start, end, target)
        idx = math.floor((end + start) / 2)
        print("idx", idx)
        if numbers[idx] == target:
            print("returning", idx)
            return idx

        if target > numbers[idx]:
            print("searching right")
            return self.search(numbers, idx + 1, end, target)
        else:
            print("searching left")
            return self.search(numbers[:idx], start, idx - 1, target)

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx in range(len(numbers) - 1):
            targetIdx = self.search(numbers, 0, len(numbers) - 1, target - numbers[idx])
            if targetIdx == -1:
                continue
            if idx == targetIdx:
                targetIdx += 1
            return [idx + 1, targetIdx + 1]


if __name__ == '__main__':
    output = Solution().twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8)
    assert output == [4, 5]

    output = Solution().twoSum([2, 7, 11, 15], 9)
    assert output == [1, 2]

    output = Solution().twoSum([2, 3, 4], 6)
    assert output == [1, 3]

    output = Solution().twoSum([-1, 0], -1)
    assert output == [1, 2]
