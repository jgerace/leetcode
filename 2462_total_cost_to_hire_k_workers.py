"""
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

    You will run k sessions and hire exactly one worker in each session.
    In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
        For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
        In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
    If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
    A worker can only be chosen once.

Return the total cost to hire exactly k workers.

Example 1:

Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.

Example 2:

Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
- In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
- In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
The total hiring cost is 4.

Constraints:

    1 <= costs.length <= 10^5
    1 <= costs[i] <= 10^5
    1 <= k, candidates <= costs.length
"""
import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        print("*****")
        total = 0
        len_costs = len(costs)

        left_idx = 0
        right_idx = len_costs - 1
        left_heap = []
        right_heap = []

        for round in range(k):
            print("round", round)
            while len(left_heap) < candidates and left_idx <= right_idx:
                heapq.heappush(left_heap, costs[left_idx])
                left_idx += 1
            while len(right_heap) < candidates and left_idx <= right_idx:
                heapq.heappush(right_heap, costs[right_idx])
                right_idx -= 1
            print("    left heap:", left_heap, bool(left_heap))
            print("    right heap", right_heap, bool(right_heap))
            print("    left idx", left_idx, "right idx", right_idx)

            if (left_heap and not right_heap or
                    left_heap and right_heap and left_heap[0] <= right_heap[0]):
                total += left_heap[0]
                heapq.heappop(left_heap)
            elif (right_heap and not left_heap or
                  left_heap and right_heap and left_heap[0] > right_heap[0]):
                total += right_heap[0]
                heapq.heappop(right_heap)

            print("    total:", total)
        return total


if __name__ == "__main__":
    output = Solution().totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4)
    assert output == 11

    output = Solution().totalCost([1, 2, 4, 1], 3, 3)
    assert output == 4

    output = Solution().totalCost([57, 33, 26, 76, 14, 67, 24, 90, 72, 37, 30], 11, 2)
    assert output == 526

    output = Solution().totalCost([10, 1, 11, 10], 2, 1)
    assert output == 11
