"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

Constraints:

    1 <= k <= 10^4
    0 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    -10^4 <= val <= 10^4
    At most 10^4 calls will be made to add.
    It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""
import heapq
from typing import List


"""class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for num in nums:
            self.insert(num)
        print(self.nums)

    def heapify(self, idx):
        l_child_idx = 2 * idx + 1
        r_child_idx = 2 * idx + 2
        smallest_idx = idx
        if l_child_idx < len(self.nums) and self.nums[l_child_idx] < self.nums[idx]:
            smallest_idx = l_child_idx
        if r_child_idx < len(self.nums) and self.nums[r_child_idx] < self.nums[idx]:
            smallest_idx = r_child_idx
        if smallest_idx != idx:
            temp = self.nums[idx]
            self.nums[idx] = self.nums[smallest_idx]
            self.nums[smallest_idx] = temp
            self.heapify(smallest_idx)

    def insert(self, val: int):
        if len(self.nums) < self.k:
            self.nums.append(val)
        else:
            self.nums[self.k-1] = val
        idx = len(self.nums) - 1
        parent_idx = (idx - 1) // 2
        while idx != 0 and self.nums[idx] < self.nums[parent_idx]:
            temp = self.nums[parent_idx]
            self.nums[parent_idx] = self.nums[idx]
            self.nums[idx] = temp
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def add(self, val: int) -> int:
        self.insert(val)
        print("inserted", val, self.nums)
        return self.nums[self.k-1]
"""


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            # pop all the smallest elements until only k are left
            # because this is a min heap, the smallest, self.nums[0], is the kth largest
            heapq.heappop(self.nums)
        return self.nums[0]


if __name__ == "__main__":
    instance = KthLargest(3, [4, 5, 8, 2])
    assert instance.add(3) == 4
    assert instance.add(5) == 5
    assert instance.add(10) == 5
    assert instance.add(9) == 8
    assert instance.add(4) == 8
