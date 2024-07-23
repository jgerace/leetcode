"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation:
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

Constraints:

    n == rooms.length
    2 <= n <= 1000
    0 <= rooms[i].length <= 1000
    1 <= sum(rooms[i].length) <= 3000
    0 <= rooms[i][j] < n
    All the values of rooms[i] are unique.
"""
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        print("*****")
        num_rooms = len(rooms)
        visited = [False for _ in range(num_rooms)]

        keys = rooms[0]
        visited[0] = True
        print("starting with", keys)
        while len(keys):
            # get a key
            key = keys.pop()
            print("key", key)

            # open the room and find out what keys it gives you
            visited[key] = True
            for new_key in rooms[key]:
                print("   found key", new_key)
                if visited[new_key]:
                    print("   already visited", new_key)
                    continue
                keys.append(new_key)
            print("   key set", keys)
            print("   visited", visited)

        return all(visited)


if __name__ == "__main__":
    output = Solution().canVisitAllRooms([[1], [2], [3], []])
    assert output is True

    output = Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
    assert output is False

    output = Solution().canVisitAllRooms([[0]])
    assert output is True

    output = Solution().canVisitAllRooms([[1, 2, 3], [], [], []])
    assert output is True

    output = Solution().canVisitAllRooms([[], []])
    assert output is False

    output = Solution().canVisitAllRooms([[2], [], [1]])
    assert output is True
