"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

    n == height.length
    1 <= n <= 2 * 10^4
    0 <= height[i] <= 10^5
"""
from collections import deque
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        print("*****")
        max_lefts = []
        max_left = 0
        for idx in range(len(height)):
            max_lefts.append(max_left)
            max_left = max(height[idx], max_left)
        print(max_lefts)
        max_rights = [0 for _ in range(len(height))]
        max_right = 0
        for idx in range(len(height)-1, -1, -1):
            max_rights[idx] = max_right
            max_right = max(height[idx], max_right)
        print(max_rights)

        total_water = 0
        for idx in range(len(height)):
            print("idx", idx, "max_left", max_lefts[idx], "max_right", max_rights[idx], "height", height[idx])
            print("adding", max(0, min(max_lefts[idx], max_rights[idx]) - height[idx]))
            total_water += max(0, min(max_lefts[idx], max_rights[idx]) - height[idx])
        print(total_water)
        return total_water


if __name__ == "__main__":
    output = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    assert output == 6

    output = Solution().trap([4, 2, 0, 3, 2, 5])
    assert output == 9
