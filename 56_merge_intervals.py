"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

    1 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^4
"""
from collections import deque
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        print("*****")
        intervals.sort(key=lambda x: x[0])

        result = []
        idx = 1
        queue = deque()
        queue.append(intervals[0])
        while len(queue) and idx <= len(intervals):
            cur_interval = queue.popleft()
            if idx == len(intervals):
                result.append(cur_interval)
                break

            if cur_interval[0] <= intervals[idx][0] <= cur_interval[1]:
                new_interval = [min(cur_interval[0], intervals[idx][0]),
                                max(cur_interval[1], intervals[idx][1])]
                queue.append(new_interval)
            else:
                result.append(cur_interval)
                queue.append(intervals[idx])
            idx += 1

        print(result)
        return result


if __name__ == "__main__":
    output = Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    assert output == [[1, 6], [8, 10], [15, 18]]

    output = Solution().merge([[1, 4], [4, 5]])
    assert output == [[1, 5]]

    output = Solution().merge([[1, 4]])
    assert output == [[1, 4]]

    output = Solution().merge([[1, 4], [5, 6]])
    assert output == [[1, 4], [5, 6]]
