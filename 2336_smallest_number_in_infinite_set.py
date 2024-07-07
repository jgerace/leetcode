"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

    SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
    int popSmallest() Removes and returns the smallest integer contained in the infinite set.
    void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

Constraints:

    1 <= num <= 1000
    At most 1000 calls will be made in total to popSmallest and addBack.
"""
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.next_int = 1
        self.added_back = []

    def popSmallest(self) -> int:
        if len(self.added_back):
            val = heapq.heappop(self.added_back)
        else:
            val = self.next_int
            self.next_int += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.next_int and num not in self.added_back:
            heapq.heappush(self.added_back, num)


if __name__ == "__main__":
    obj = SmallestInfiniteSet()
    obj.addBack(2)
    assert obj.popSmallest() == 1
    assert obj.popSmallest() == 2
    assert obj.popSmallest() == 3
    obj.addBack(1)
    obj.addBack(5)
    assert obj.popSmallest() == 1
    assert obj.popSmallest() == 4
    assert obj.popSmallest() == 5
    obj.addBack(2)
    assert obj.popSmallest() == 2
