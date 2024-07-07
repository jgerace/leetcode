"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:

    -10^5 <= num <= 10^5
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 10^4 calls will be made to addNum and findMedian.

Follow up:

    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
import heapq


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.median = None

    def addNum(self, num: int) -> None:
        if not self.median:
            self.median = num

        if len(self.min_heap) and num > self.min_heap[0]:
            print("appending", num, "to min_heap")
            heapq.heappush(self.min_heap, num)
        else:
            print("appending", num, "to max_heap")
            heapq.heappush(self.max_heap, -num)

        if len(self.max_heap) - len(self.min_heap) > 1:
            value = heapq.heappop(self.max_heap)
            value *= -1
            print("moving", value, "from max_heap to min_heap")
            heapq.heappush(self.min_heap, value)
        elif len(self.min_heap) - len(self.max_heap) > 1:
            value = heapq.heappop(self.min_heap)
            print("moving", value, "from min_heap to max_heap")
            heapq.heappush(self.max_heap, -value)

        print("min heap:", self.min_heap)
        print("max heap:", self.max_heap)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            self.median = float((self.min_heap[0] + (self.max_heap[0] * -1)) / 2.0)
        else:
            if len(self.min_heap) > len(self.max_heap):
                self.median = self.min_heap[0]
            else:
                self.median = (self.max_heap[0] * -1)
        print("median:", self.median)
        return self.median


if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    assert obj.findMedian() == 1.5
    obj.addNum(3)
    assert obj.findMedian() == 2.0
