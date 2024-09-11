"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:

    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]
"""
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        print("*****")
        n = len(isConnected)
        seen = [False for _ in range(n)]
        num_provinces = 0

        def dfs(city) -> None:
            for idx in range(n):
                if isConnected[city][idx] and not seen[idx]:
                    print("  city", city, "connected to", idx)
                    seen[idx] = True
                    dfs(idx)

        for c in range(n):
            print("Looking at city", c)
            if not seen[c]:
                print("  new city", c)
                seen[c] = True
                num_provinces += 1
                dfs(c)
        print(num_provinces)
        return num_provinces


if __name__ == "__main__":
    output = Solution().findCircleNum([[1, 1, 0],
                                       [1, 1, 0],
                                       [0, 0, 1]])
    assert output == 2

    output = Solution().findCircleNum([[1, 0, 0],
                                       [0, 1, 0],
                                       [0, 0, 1]])
    assert output == 3

    output = Solution().findCircleNum([[1, 0, 0, 1],
                                       [0, 1, 1, 0],
                                       [0, 1, 1, 1],
                                       [1, 0, 1, 1]])
    assert output == 1

    output = Solution().findCircleNum([[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
    assert output == 8
