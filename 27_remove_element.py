"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.


Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100
"""
from typing import List


class Solution:
    @staticmethod
    def modifyUsingRemove(nums: List[int], val: int) -> int:
        try:
            for idx in range(len(nums)):
                nums.remove(val)
        except Exception:
            pass
        print(nums)
        return len(nums)

    @staticmethod
    def modifyUsingSwap(nums: List[int], val: int) -> int:
        endPtr = len(nums) - 1
        idx = 0
        while idx < len(nums):
            if endPtr < idx:
                break
            if nums[idx] == val:
                temp = nums[idx]
                nums[idx] = nums[endPtr]
                nums[endPtr] = temp
                endPtr -= 1
                continue
            idx += 1
        return idx

    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        return Solution.modifyUsingRemove(nums, val)


if __name__ == "__main__":
    nums = [3,2,2,3]
    k = Solution.removeElement(nums, 3)
    assert k == 2
    assert nums[:k] == [2,2]

    # The two solutions above will yield different ordering for elements in nums.
    # Assert must be modified accordingly or made agnostic of order
    nums = [0,1,2,2,3,0,4,2]
    k = Solution.removeElement(nums, 2)
    assert k == 5
    assert nums[:k] == [0,1,3,0,4]
