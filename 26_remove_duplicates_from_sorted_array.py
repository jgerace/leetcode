'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.


Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
'''

from typing import List


class Solution:
    @staticmethod
    def removeDuplicatesWithSet(nums: List[int]) -> int:
        output = set(nums)
        idx = 0
        for val in output:
            nums[idx] = val
            idx += 1
        return len(output)

    @staticmethod
    def removeDuplicatesWithSwap(nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        curVal = nums[0]
        curPtr = 1
        for idx in range(1, len(nums)):
            if nums[idx] != curVal:
                nums[curPtr] = nums[idx]
                curVal = nums[idx]
                curPtr += 1
        return curPtr


if __name__ == "__main__":
    nums = [1,1,2]
    k = Solution.removeDuplicatesWithSwap(nums)
    assert k == 2
    assert nums[:k] == [1,2]

    nums = [0,0,1,1,1,2,2,3,3,4]
    k = Solution.removeDuplicatesWithSwap(nums)
    assert k == 5
    assert nums[:k] == [0,1,2,3,4]

    nums = [0]
    k = Solution.removeDuplicatesWithSwap(nums)
    assert k == 1
    assert nums[:k] == [0]

    nums = [0, 0, 0]
    k = Solution.removeDuplicatesWithSwap(nums)
    assert k == 1
    assert nums[:k] == [0]
