"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:

    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^5
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print("*****")
        dp = {}
        for idx in range(0, len(prices) - 1):
            for jdx in range(idx + 1, len(prices)):
                profit = prices[jdx] - prices[idx]
                if profit > 0:
                    dp[(idx, jdx)] = profit

        max_profit = 0
        for interval, profit in dp.items():
            start, end = interval
            print("analyzing interval", start, end, profit)
            max_profit = max(max_profit, profit)
            for key in dp.keys():
                if key == interval:
                    continue
                key_start, key_end = key
                if key_end <= start or key_start >= end:
                    print("  comparing to", key, dp[key])
                    max_profit = max(max_profit, profit + dp[key])

        print(max_profit)
        return max_profit

    def savesies(self, prices: List[int]) -> int:
        print("*****")
        if len(prices) <= 1:
            return 0
        dp = {}  # interval -> max profit

        def get_max_profit_for_interval(start, end):
            if start == end or dp.get((start, end)):
                return
            min_price, max_price = prices[start], prices[start]
            max_profit = 0
            for idx in range(start, end):
                if prices[idx] < min_price:
                    min_price = prices[idx]
                if prices[idx] > max_price:
                    max_price = prices[idx]
                    max_profit = max(max_profit, max_price - min_price)
            print("  interval", start, end, "min:", min_price, "max", max_price, "max_profit:", max_profit)
            dp[(start, end)] = max_profit

        for idx in range(1, len(prices)):
            get_max_profit_for_interval(0, idx + 1)
            get_max_profit_for_interval(idx, len(prices))
        print(dp)

        return 0


if __name__ == "__main__":
    output = Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
    assert output == 6

    output = Solution().maxProfit([1, 2, 3, 4, 5])
    assert output == 4

    output = Solution().maxProfit([7, 6, 4, 3, 1])
    assert output == 0

    output = Solution().maxProfit([1, 2])
    assert output == 1
