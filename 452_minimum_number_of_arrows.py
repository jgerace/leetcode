"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:

    1 <= points.length <= 10^5
    points[i].length == 2
    -2^31 <= xstart < xend <= 2^31 - 1
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        print("*****")
        sorted_points = sorted(points, key=lambda x: x[0])
        print("sorted points:", sorted_points)
        count = 0
        idx_start = 0
        idx_end = 0
        while idx_start <= idx_end < len(points):
            point = sorted_points[idx_start]
            print("analyzing", point)
            max_start = point[0]
            min_end = point[1]
            while (idx_end < len(points) and
                   max_start <= sorted_points[idx_end][0] <= min_end):
                max_start = max(max_start, sorted_points[idx_end][0])
                min_end = min(min_end, sorted_points[idx_end][1])
                print("   point", sorted_points[idx_end], "overlaps")
                idx_end += 1
            idx_start = idx_end
            count += 1

        print("count:", count)
        return count


if __name__ == "__main__":

    output = Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
    assert output == 2

    output = Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]])
    assert output == 4

    output = Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]])
    assert output == 2

    output = Solution().findMinArrowShots(
        [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]])
    assert output == 2
