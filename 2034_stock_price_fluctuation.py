"""
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

    Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
    Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
    Finds the maximum price the stock has been based on the current records.
    Finds the minimum price the stock has been based on the current records.

Implement the StockPrice class:

    StockPrice() Initializes the object with no price records.
    void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
    int current() Returns the latest price of the stock.
    int maximum() Returns the maximum price of the stock.
    int minimum() Returns the minimum price of the stock.

Example 1:

Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]

Explanation
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                          // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.

Constraints:

    1 <= timestamp, price <= 10^9
    At most 105 calls will be made in total to update, current, maximum, and minimum.
    current, maximum, and minimum will be called only after update has been called at least once.
"""
import heapq


# TODO: This times out on the long test case
class StockPrice:

    def __init__(self):
        self.price_at_time = {}  # time -> price
        self.max_heap = []  # (-price, timestamp)
        self.min_heap = []  # (price, timestamp)
        self.current_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        """existing_price = self.hash.get(timestamp)
        if existing_price is not None:
            self.max_heap.remove((-existing_price, timestamp))
            self.min_heap.remove((existing_price, timestamp))"""
        self.price_at_time[timestamp] = price

        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

        if timestamp >= self.current_timestamp:
            self.current_timestamp = timestamp

    def current(self) -> int:
        return self.price_at_time[self.current_timestamp]

    def maximum(self) -> int:
        while self.price_at_time[self.max_heap[0][1]] != -self.max_heap[0][0]:
            heapq.heappop(self.max_heap)
        return self.max_heap[0][0] * -1

    def minimum(self) -> int:
        while self.price_at_time[self.min_heap[0][1]] != self.min_heap[0][0]:
            heapq.heappop(self.min_heap)

        return self.min_heap[0][0]


if __name__ == "__main__":
    instance = StockPrice()
    instance.update(1, 10)
    instance.update(2, 5)
    assert instance.current() == 5
    assert instance.maximum() == 10
    instance.update(1, 3)
    assert instance.maximum() == 5
    instance.update(4, 2)
    assert instance.minimum() == 2
