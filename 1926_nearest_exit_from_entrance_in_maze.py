"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:

Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:

Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:

Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.

Constraints:

    maze.length == m
    maze[i].length == n
    1 <= m, n <= 100
    maze[i][j] is either '.' or '+'.
    entrance.length == 2
    0 <= entrancerow < m
    0 <= entrancecol < n
    entrance will always be an empty cell.
"""
from collections import deque
from typing import List


class Solution:

    def is_entrance(self, location: List[int], entrance: List[int]) -> bool:
        return location == entrance

    def is_exit(self, location: List[int], maze: List[List[str]], entrance: List[int]) -> bool:
        return ((location[0] == 0 or location[0] == len(maze) - 1
                 or location[1] == 0 or location[1] == len(maze[0]) - 1)
                and not self.is_entrance(location, entrance))

    def get_distance_to_nearest_exit(self,
                                     maze: List[List[str]],
                                     location: List[int],
                                     entrance: List[int],
                                     visited: List[List[bool]]) -> int:
        # thought i had something here but never quite got it to work
        if self.is_exit(location, maze, entrance):
            # print("found exit at", location)
            return 0

        row = location[0]
        col = location[1]
        visited[row][col] = True
        min_dist = None
        # print("currently at", location)
        # move left
        if col > 0 and maze[row][col - 1] != "+" and not visited[row][col - 1]:
            # print("looking left")
            new_location = [row, col - 1]
            l_dist = self.get_distance_to_nearest_exit(maze,
                                                       new_location,
                                                       entrance,
                                                       visited)
            min_dist = l_dist if (min_dist is None or l_dist != -1) else min_dist
        # move right
        if col < len(maze[0]) - 1 and maze[row][col + 1] != "+" and not visited[row][col + 1]:
            # print("looking right")
            new_location = [row, col + 1]
            r_dist = self.get_distance_to_nearest_exit(maze,
                                                       new_location,
                                                       entrance,
                                                       visited)
            # print("r_dist", r_dist, "min_dist", min_dist)
            min_dist = min(r_dist, min_dist) if (min_dist is not None and min_dist != -1 and r_dist != -1) else r_dist
        # move up
        if row > 0 and maze[row - 1][col] != "+" and not visited[row - 1][col]:
            # print("looking up")
            new_location = [row - 1, col]
            u_dist = self.get_distance_to_nearest_exit(maze,
                                                       new_location,
                                                       entrance,
                                                       visited)
            min_dist = min(u_dist, min_dist) if (min_dist is not None and min_dist != -1 and u_dist != -1) else u_dist
        # move down
        if row < len(maze) - 1 and maze[row + 1][col] != "+" and not visited[row + 1][col]:
            # print("looking down")
            new_location = [row + 1, col]
            d_dist = self.get_distance_to_nearest_exit(maze,
                                                       new_location,
                                                       entrance,
                                                       visited)
            min_dist = min(d_dist, min_dist) if (min_dist is not None and min_dist != -1 and d_dist != -1) else d_dist

        visited[row][col] = False
        # print("min_dist =", min_dist, "returning", min_dist + 1 if min_dist is not None and min_dist != -1 else -1)
        return min_dist + 1 if min_dist is not None and min_dist != -1 else -1

    def get_nearest_bfs(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = "+"
        num_rows = len(maze)
        num_cols = len(maze[0])

        while len(queue) > 0:
            row, col, cur_dist = queue.popleft()
            for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row = row + drow
                new_col = col + dcol
                if (0 <= new_row < num_rows and
                        0 <= new_col < num_cols and
                        maze[new_row][new_col] != "+"):
                    if new_row == 0 or new_row == num_rows - 1 or new_col == 0 or new_col == num_cols - 1:
                        return cur_dist + 1
                    maze[new_row][new_col] = "+"
                    queue.append((new_row, new_col, cur_dist + 1))

        return -1

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        return self.get_nearest_bfs(maze, entrance)


if __name__ == "__main__":
    output = Solution().nearestExit([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
                                    [1, 2])
    assert output == 1

    output = Solution().nearestExit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]],
                                    [1, 0])
    assert output == 2

    output = Solution().nearestExit([[".", "+"]],
                                    [0, 0])
    assert output == -1

    output = Solution().nearestExit([[".", "."]],
                                    [0, 0])
    assert output == 1

    output = Solution().nearestExit([["."]],
                                    [0, 0])
    assert output == -1

    output = Solution().nearestExit(
        [
            ["+", ".", "+", "+", "+", "+", "+"],
            ["+", ".", "+", ".", ".", ".", "+"],
            ["+", ".", "+", ".", "+", ".", "+"],
            ["+", ".", ".", ".", "+", ".", "+"],
            ["+", "+", "+", "+", "+", "+", "."]],
        [0, 1])
    assert output == -1

    output = Solution().nearestExit(
        [
            [".", "+", "+", "+", ".", ".", ".", "+", "+"],
            [".", ".", "+", ".", "+", ".", "+", "+", "."],
            [".", ".", "+", ".", ".", ".", ".", ".", "."],
            [".", "+", ".", ".", "+", "+", ".", "+", "."],
            [".", ".", ".", ".", ".", ".", ".", "+", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "+", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "+"],
            ["+", ".", ".", ".", "+", ".", ".", ".", "."]],
        [5, 6])
    assert output == 2

    output = Solution().nearestExit(
        [
            [".", "+", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "+", "+", "+", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "+", "+", ".", ".", "."],
            ["+", ".", ".", ".", ".", "+", ".", ".", "."],
            [".", ".", ".", ".", ".", "+", ".", ".", "."],
            [".", "+", ".", ".", "+", "+", ".", ".", "."],
            ["+", ".", "+", "+", ".", ".", "+", ".", "."],
            [".", ".", ".", ".", ".", "+", "+", ".", "."]],
        [8, 1])
    assert output == 1
