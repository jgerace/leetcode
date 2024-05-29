'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

Constraints:

    1 <= prices.length <= 3 * 104
    0 <= prices[i] <= 104
'''
from typing import List


class Solution:

    def maxProfit(selfself, prices: List[int]) -> int:
        # Greedy
        # Add up all the increases in price
        maxProfit = 0
        if len(prices) == 1:
            return 0
        for idx in range(1, len(prices)):
            total = prices[idx] - prices[idx-1]
            if total > 0:
                maxProfit += total
        return maxProfit

    def maxProfitRecursive(self, prices: List[int]) -> int:
        # Thought I had something here that would divide the list into combinations of sublists to find the
        # max profit and add them up, but didn't get it to work
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            profit = prices[0] - prices[1]
            return profit if profit > 0 else 0

        maxProfit = 0
        for idx in range(1, len(prices)):
            profit = self.maxProfit(prices[0:idx]) + self.maxProfit(prices[idx:len(prices)])
            # print("evaluating", prices[0:idx] + prices[idx:len(prices)], "profit:", profit)
            maxProfit = profit if profit > maxProfit else maxProfit

        # print("maxProfit:", maxProfit)
        return maxProfit


if __name__ == '__main__':
    profit = Solution().maxProfit([7, 1, 5, 3, 6, 4])
    assert profit == 7

    profit = Solution().maxProfit([1, 2, 3, 4, 5])
    assert profit == 4

    profit = Solution().maxProfit([7, 6, 4, 3, 1])
    assert profit == 0

    profit = Solution().maxProfit([7, 1, 5, 6, 7, 4])
    assert profit == 6
