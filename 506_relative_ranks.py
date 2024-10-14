"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

    The 1st place athlete's rank is "Gold Medal".
    The 2nd place athlete's rank is "Silver Medal".
    The 3rd place athlete's rank is "Bronze Medal".
    For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

Constraints:

    n == score.length
    1 <= n <= 10^4
    0 <= score[i] <= 10^6
    All the values in score are unique.
"""
import heapq
from typing import List

from testing import listItemsEqual


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        print("*****")
        heap = []
        for idx, points in enumerate(score):
            heap.append((-points, idx))
            heapq.heapify(heap)

        result = ["" for _ in range(len(score))]
        place = 1
        while heap:
            score, idx = heapq.heappop(heap)
            place_str = str(place)
            if place == 1:
                place_str = "Gold Medal"
            elif place == 2:
                place_str = "Silver Medal"
            elif place == 3:
                place_str = "Bronze Medal"
            result[idx] = place_str
            place += 1
        print(result)
        return result


if __name__ == "__main__":
    output = Solution().findRelativeRanks([5, 4, 3, 2, 1])
    assert output == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

    output = Solution().findRelativeRanks([10, 3, 8, 9, 4])
    assert output == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
