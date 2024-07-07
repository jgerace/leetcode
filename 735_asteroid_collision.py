"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Constraints:

    2 <= asteroids.length <= 10^4
    -1000 <= asteroids[i] <= 1000
    asteroids[i] != 0
"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        print("*****")

        def will_collide(rock1: int, rock2: int) -> bool:
            if not rock1 or not rock2:
                return False

            if rock1 > 0 > rock2:
                return True
            return False

        collisions = [asteroids[0]]
        for rock in asteroids[1:]:
            print("incoming rock:", rock)
            if len(collisions) > 0:
                last_rock = collisions.pop()
            else:
                print("no collision on empty list, appending", rock)
                collisions.append(rock)
                continue

            while will_collide(last_rock, rock):
                print("collision between", last_rock, rock)
                if abs(last_rock) > abs(rock):
                    print(last_rock, "survives")
                    collisions.append(last_rock)
                    break
                elif abs(last_rock) < abs(rock):
                    print(rock, "survives")
                    if len(collisions) > 0:
                        last_rock = collisions.pop()
                    else:
                        collisions.append(rock)
                        break
                else:
                    print("both rocks die")
                    break
            else:
                print("no collision, appending", rock)
                collisions.append(last_rock)
                collisions.append(rock)
                print("rocks:", collisions)
        print(collisions)
        return collisions


if __name__ == "__main__":
    output = Solution().asteroidCollision([5, 10, -5])
    assert output == [5, 10]

    output = Solution().asteroidCollision([8, -8])
    assert output == []

    output = Solution().asteroidCollision([10, 2, -5])
    assert output == [10]

    output = Solution().asteroidCollision([-2, -1, 1, 2])
    assert output == [-2, -1, 1, 2]

    output = Solution().asteroidCollision([1, -2, -2, -2])
    assert output == [-2, -2, -2]
