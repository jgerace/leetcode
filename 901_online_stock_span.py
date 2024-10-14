"""
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

    For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
    Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.

Implement the StockSpanner class:

    StockSpanner() Initializes the object of the class.
    int next(int price) Returns the span of the stock's price given that today's price is price.

Example 1:

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6

Constraints:

    1 <= price <= 10^5
    At most 104 calls will be made to next.
"""


class StockSpanner:

    def __init__(self):
        print("*****")
        self.stack = []

    def next(self, price: int) -> int:
        # Pretty sure this solution can be simplified
        streak = 1
        if len(self.stack) == 0 or self.stack[-1][0] > price:
            self.stack.append((price, streak))
        else:
            while len(self.stack) and self.stack[-1][0] <= price:
                item = self.stack.pop()
                streak += item[1]
            self.stack.append((price, streak))
        print("stack:", self.stack, "streak:", streak)
        return streak


if __name__ == "__main__":
    instance = StockSpanner()
    assert instance.next(100) == 1
    assert instance.next(80) == 1
    assert instance.next(60) == 1
    assert instance.next(70) == 2
    assert instance.next(60) == 1
    assert instance.next(75) == 4

    instance = StockSpanner()
    assert instance.next(31) == 1
    assert instance.next(41) == 2
    assert instance.next(48) == 3
    assert instance.next(59) == 4
    assert instance.next(79) == 5

    instance = StockSpanner()
    assert instance.next(28) == 1
    assert instance.next(14) == 1
    assert instance.next(28) == 3
    assert instance.next(35) == 4
    assert instance.next(46) == 5
    assert instance.next(53) == 6
    assert instance.next(66) == 7
    assert instance.next(80) == 8
    assert instance.next(87) == 9
    assert instance.next(88) == 10
